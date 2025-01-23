from flask import Blueprint, jsonify
from app import db
from app.models import ExpertInteraction, Visitor, Chat
from datetime import datetime

health_bp = Blueprint('health', __name__)

@health_bp.route('/', methods=['GET'])
def root():
    return jsonify({
        'status': 'ok',
        'message': '后端服务运行正常'
    })

@health_bp.route('/health', methods=['GET'])
def health_check():
    try:
        # 检查数据库连接
        ExpertInteraction.query.first()
        return jsonify({
            'status': 'healthy',
            'database': 'connected',
            'timestamp': datetime.utcnow().isoformat()
        })
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': datetime.utcnow().isoformat()
        }), 500

@health_bp.route('/stats', methods=['GET'])
def get_stats():
    try:
        # 获取基本统计信息
        visitor_count = Visitor.query.count()
        interaction_count = ExpertInteraction.query.count()
        chat_count = Chat.query.count()
        
        # 获取最近的访客
        recent_visitors = Visitor.query.order_by(Visitor.visit_time.desc()).limit(5)
        visitors = [{
            'ip': v.ip_address,
            'visit_time': v.visit_time.strftime('%Y-%m-%d %H:%M:%S'),
            'leave_time': v.leave_time.strftime('%Y-%m-%d %H:%M:%S') if v.leave_time else None
        } for v in recent_visitors]
        
        # 获取最近的对话
        recent_chats = Chat.query.order_by(Chat.timestamp.desc()).limit(5)
        chats = [{
            'type': c.type,
            'content': c.content,
            'time': c.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        } for c in recent_chats]
        
        return jsonify({
            'statistics': {
                'total_visitors': visitor_count,
                'total_interactions': interaction_count,
                'total_messages': chat_count
            },
            'recent_visitors': visitors,
            'recent_chats': chats
        })
        
    except Exception as e:
        print("获取统计信息失败:", str(e))
        return jsonify({
            'error': '获取统计信息失败',
            'message': str(e)
        }), 500 
