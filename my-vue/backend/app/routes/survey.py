from flask import Blueprint, request, jsonify
from app import db
from app.models.survey import Survey

survey_bp = Blueprint('survey', __name__)

@survey_bp.route('/submit', methods=['POST'])
def submit_survey():
    try:
        data = request.get_json()
        print("收到的问卷数据:", data)  # 添加调试日志
        
        # 创建新的问卷记录
        survey = Survey(
            visitor_id=data.get('visitor_id'),  # 添加访客ID
            
            # 日常生活照护问题
            daily_eating=data['daily']['eating'],
            daily_dressing=data['daily']['dressing'],
            daily_toileting=data['daily']['toileting'],
            daily_bathing=data['daily']['bathing'],
            daily_indoor=data['daily']['indoor'],
            daily_outdoor=data['daily']['outdoor'],
            
            # 精神行为问题
            mental_memory=data['mental']['memory'],
            mental_emotion=data['mental']['emotion'],
            mental_sleep=data['mental']['sleep'],
            mental_communication=data['mental']['communication'],
            mental_behavior=data['mental']['behavior'],
            mental_cognition=data['mental']['cognition'],
            
            # 安全风险问题
            safety_falling=data['safety']['falling'],
            safety_wandering=data['safety']['wandering'],
            safety_medication=data['safety']['medication'],
            safety_selfHarm=data['safety']['selfHarm'],
            safety_accident=data['safety']['accident'],
            safety_emergency=data['safety']['emergency'],
            
            # 居住环境评估
            environment_layout=data['environment']['layout'],
            environment_lighting=data['environment']['lighting'],
            environment_ventilation=data['environment']['ventilation'],
            environment_safety=data['environment']['safety'],
            environment_hygiene=data['environment']['hygiene'],
            environment_accessibility=data['environment']['accessibility']
        )
        
        db.session.add(survey)
        db.session.commit()
        
        return jsonify({
            'message': '问卷提交成功',
            'survey_id': survey.id
        }), 201
        
    except Exception as e:
        print(f"提交问卷失败: {str(e)}")  # 添加错误日志
        db.session.rollback()
        return jsonify({'message': f'提交失败: {str(e)}'}), 500

@survey_bp.route('/list', methods=['GET'])
def get_surveys():
    try:
        surveys = Survey.query.order_by(Survey.submit_time.desc()).all()
        return jsonify([{
            'id': s.id,
            'submit_time': s.submit_time.strftime('%Y-%m-%d %H:%M:%S'),
            'daily': {
                'eating': s.daily_eating,
                'dressing': s.daily_dressing,
                'toileting': s.daily_toileting,
                'bathing': s.daily_bathing,
                'indoor': s.daily_indoor,
                'outdoor': s.daily_outdoor
            },
            'mental': {
                'memory': s.mental_memory,
                'emotion': s.mental_emotion,
                'sleep': s.mental_sleep,
                'communication': s.mental_communication,
                'behavior': s.mental_behavior,
                'cognition': s.mental_cognition
            },
            'safety': {
                'falling': s.safety_falling,
                'wandering': s.safety_wandering,
                'medication': s.safety_medication,
                'selfHarm': s.safety_selfHarm,
                'accident': s.safety_accident,
                'emergency': s.safety_emergency
            },
            'environment': {
                'layout': s.environment_layout,
                'lighting': s.environment_lighting,
                'ventilation': s.environment_ventilation,
                'safety': s.environment_safety,
                'hygiene': s.environment_hygiene,
                'accessibility': s.environment_accessibility
            }
        } for s in surveys])
        
    except Exception as e:
        print(f"获取问卷列表失败: {str(e)}")
        return jsonify({'message': '获取失败'}), 500 
