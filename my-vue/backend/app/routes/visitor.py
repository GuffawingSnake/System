from flask import Blueprint, request, jsonify, current_app
from app import db
from app.models.visitor import Visitor
from app.models.survey import Survey
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
import sqlite3

visitor_bp = Blueprint('visitor', __name__)

# 启用SQLite外键支持
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

@visitor_bp.route('/track', methods=['POST'])
def track_visitor():
    try:
        print("\n=== 开始访客追踪 ===")
        
        # 获取访客IP
        ip_address = request.remote_addr or request.headers.get('X-Forwarded-For', 'unknown')
        print(f"访客IP: {ip_address}")
        
        # 检查是否已存在相同IP的未离开访客
        existing_visitor = Visitor.query.filter_by(
            ip_address=ip_address,
            leave_time=None
        ).first()
        
        if existing_visitor:
            print(f"找到现有访客，ID: {existing_visitor.id}")
            return jsonify({
                'success': True,
                'visitor_id': existing_visitor.id
            })
        
        # 创建新访客记录
        visitor = Visitor(ip_address=ip_address)
        db.session.add(visitor)
        db.session.commit()
        
        print(f"新访客记录创建成功，ID: {visitor.id}")
        
        # 验证数据是否保存成功
        saved_visitor = Visitor.query.get(visitor.id)
        if not saved_visitor:
            raise Exception("访客记录保存失败")
        
        return jsonify({
            'success': True,
            'visitor_id': visitor.id
        })
        
    except Exception as e:
        print(f"访客追踪失败: {str(e)}")
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@visitor_bp.route('/survey', methods=['POST'])
def submit_survey():
    try:
        print("\n=== 开始提交问卷 ===")
        data = request.get_json()
        print("收到的问卷数据:", data)
        
        # 验证访客ID
        visitor_id = data.get('visitor_id')
        if not visitor_id:
            raise ValueError('缺少访客ID')
        
        print(f"正在查找访客ID: {visitor_id}")
        visitor = Visitor.query.get(visitor_id)
        if not visitor:
            raise ValueError(f'访客ID {visitor_id} 不存在')
        
        print(f"找到访客记录: {visitor.id}")
        
        # 构建问卷数据
        survey_data = {
            'visitor_id': visitor_id,
            'submit_time': datetime.utcnow()
        }
        
        # 验证并收集所有字段数据
        for section in ['daily', 'mental', 'safety', 'environment']:
            if section not in data:
                print(f"错误：缺少{section}部分的数据")
                raise ValueError(f'缺少{section}部分的数据')
            
            section_data = data[section]
            print(f"处理{section}部分数据:", section_data)
            
            for field, value in section_data.items():
                try:
                    int_value = int(value) if value is not None else None
                    if int_value is None or int_value < 0 or int_value > 2:
                        print(f"错误：字段 {section}.{field} 的值无效: {value}")
                        raise ValueError(f'字段 {section}.{field} 的值无效')
                    survey_data[f'{section}_{field}'] = int_value
                except (TypeError, ValueError) as e:
                    print(f"错误：字段 {section}.{field} 的值类型错误: {value}")
                    raise ValueError(f'字段 {section}.{field} 的值类型错误')
        
        print("问卷数据验证通过，准备保存:", survey_data)
        
        # 创建新的问卷记录
        survey = Survey(**survey_data)
        db.session.add(survey)
        db.session.commit()
        
        print(f"问卷保存成功，ID: {survey.id}")
        
        # 验证数据是否保存成功
        saved_survey = Survey.query.get(survey.id)
        if not saved_survey:
            raise Exception("问卷保存失败")
        
        return jsonify({
            'success': True,
            'message': '问卷提交成功',
            'survey_id': survey.id
        }), 201
        
    except Exception as e:
        print(f"问卷提交失败: {str(e)}")
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': str(e)
        }), 400 if isinstance(e, ValueError) else 500

@visitor_bp.route('/', methods=['GET'])
def visitor_index():
    return jsonify({
        'message': '访客服务正在运行',
        'endpoints': {
            'track': '/api/visitor/track',
            'survey': '/api/visitor/survey',
            'leave': '/api/visitor/leave'
        }
    }) 
