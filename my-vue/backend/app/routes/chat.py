from flask import Blueprint, request, jsonify
from app import db
from app.models import Chat, ExpertInteraction
from app.models.visitor import Visitor
from app.services.qianwen_service import qianwen_service
import os
import time
from datetime import datetime, timedelta
import threading

# 添加请求限制控制
class RateLimiter:
    def __init__(self):
        self.requests = {}
        self.lock = threading.Lock()
        self.max_requests = 2  # 每分钟最大请求数
        self.window_size = 60  # 时间窗口大小（秒）
        
    def can_make_request(self, visitor_id):
        now = datetime.now()
        with self.lock:
            if visitor_id not in self.requests:
                self.requests[visitor_id] = []
            
            # 清理过期的请求记录
            self.requests[visitor_id] = [
                req_time for req_time in self.requests[visitor_id]
                if (now - req_time) < timedelta(seconds=self.window_size)
            ]
            
            # 检查是否超过限制
            if len(self.requests[visitor_id]) >= self.max_requests:
                return False
                
            self.requests[visitor_id].append(now)
            return True
            
    def wait_time(self, visitor_id):
        if visitor_id not in self.requests or not self.requests[visitor_id]:
            return 0
        oldest_request = min(self.requests[visitor_id])
        wait_seconds = self.window_size - (datetime.now() - oldest_request).total_seconds()
        return max(0, int(wait_seconds))

rate_limiter = RateLimiter()

def get_ai_response(message, interaction_id=None):
    """获取AI响应的辅助函数"""
    try:
        # 获取历史对话记录
        messages = []
        if interaction_id:
            history = Chat.query.filter_by(interaction_id=interaction_id)\
                .order_by(Chat.timestamp.asc())\
                .limit(10)\
                .all()
            
            for chat in history:
                role = 'assistant' if chat.type == 'ai' else 'user'
                messages.append({
                    'role': role,
                    'content': chat.content
                })
        
        # 添加系统提示和当前消息
        messages = [
            {
                'role': 'system',
                'content': '你是一个专业的老年照护AI助手，请用专业且友善的语气回答问题。'
            }
        ] + messages + [
            {
                'role': 'user',
                'content': message
            }
        ]
        
        return qianwen_service.get_response(messages)
        
    except Exception as e:
        print(f"AI服务错误: {str(e)}")
        raise Exception(f"AI服务错误: {str(e)}")

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        visitor_id = data.get('visitor_id')
        message = data.get('message')
        
        print(f"收到请求: visitor_id={visitor_id}, message={message}")
        
        # 如果没有visitor_id，创建新访客
        if not visitor_id:
            visitor = Visitor(
                ip_address=request.remote_addr,
                user_agent=request.headers.get('User-Agent', '')
            )
            db.session.add(visitor)
            db.session.commit()
            visitor_id = visitor.id
            
        # 检查请求频率
        if not rate_limiter.can_make_request(visitor_id):
            wait_time = rate_limiter.wait_time(visitor_id)
            return jsonify({
                'error': f'请求过于频繁，请等待 {wait_time} 秒后重试'
            }), 429
            
        # 创建或获取互动记录
        interaction = ExpertInteraction.query.filter_by(
            visitor_id=visitor_id,
            end_time=None
        ).first()
        
        if not interaction:
            interaction = ExpertInteraction(
                visitor_id=visitor_id,
                question_count=0,
                status='active'
            )
            db.session.add(interaction)
            db.session.commit()
            
        try:
            # 保存用户消息
            user_message = Chat(
                visitor_id=visitor_id,
                interaction_id=interaction.id,
                content=message.strip(),  # 清理消息内容
                type='user'
            )
            db.session.add(user_message)
            db.session.commit()  # 先提交用户消息
            
            print(f"已保存用户消息: {user_message.id}")
            
            # 获取AI响应
            messages = [{
                'role': 'user',
                'content': message
            }]
            ai_response = qianwen_service.get_response(messages)
            
            # 保存AI响应
            ai_message = Chat(
                visitor_id=visitor_id,
                interaction_id=interaction.id,
                content=ai_response.strip(),  # 清理响应内容
                type='ai'
            )
            db.session.add(ai_message)
            
            # 更新互动记录
            interaction.question_count = (interaction.question_count or 0) + 1
            db.session.commit()  # 提交AI响应和计数更新
            
            print(f"已保存AI响应: {ai_message.id}")
            
            return jsonify({
                'response': ai_response,
                'visitor_id': visitor_id,
                'chat_id': ai_message.id  # 返回消息ID
            })
            
        except Exception as e:
            db.session.rollback()
            print(f"AI服务错误: {str(e)}")
            return jsonify({
                'error': f"AI服务错误: {str(e)}"
            }), 500
            
    except Exception as e:
        db.session.rollback()
        print(f"处理消息错误: {str(e)}")
        return jsonify({'error': str(e)}), 500

@chat_bp.route('/history', methods=['GET'])
def get_chat_history():
    try:
        visitor_id = request.args.get('visitor_id')
        if not visitor_id:
            return jsonify({'error': '缺少访客ID'}), 400
            
        chats = Chat.query.filter_by(visitor_id=visitor_id)\
            .order_by(Chat.timestamp.desc())\
            .all()
        
        history = [{
            'id': chat.id,
            'content': chat.content,
            'type': chat.type,
            'time': chat.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        } for chat in chats]
        
        return jsonify(history)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500 
