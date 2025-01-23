from app import create_app, db
from app.models.visitor import Visitor
from app.models.survey import Survey

def check_database():
    app = create_app()
    with app.app_context():
        print("\n=== 数据库检查 ===")
        
        # 检查表是否存在
        print("\n表信息:")
        tables = db.engine.table_names()
        print(f"存在的表: {tables}")
        
        # 检查访客数据
        print("\n访客数据:")
        visitors = Visitor.query.all()
        for visitor in visitors:
            print(f"访客ID: {visitor.id}, IP: {visitor.ip_address}, 访问时间: {visitor.visit_time}")
        
        # 检查问卷数据
        print("\n问卷数据:")
        surveys = Survey.query.all()
        for survey in surveys:
            print(f"\n问卷ID: {survey.id}")
            print(f"访客ID: {survey.visitor_id}")
            print(f"提交时间: {survey.submit_time}")
            print("日常生活照护:")
            print(f"  进食能力: {survey.daily_eating}")
            print(f"  穿衣能力: {survey.daily_dressing}")
            print(f"  如厕能力: {survey.daily_toileting}")
            print(f"  洗澡能力: {survey.daily_bathing}")
            print(f"  室内活动: {survey.daily_indoor}")
            print(f"  户外活动: {survey.daily_outdoor}")
            
            print("精神行为问题:")
            print(f"  记忆力: {survey.mental_memory}")
            print(f"  情绪状态: {survey.mental_emotion}")
            print(f"  睡眠情况: {survey.mental_sleep}")
            print(f"  沟通能力: {survey.mental_communication}")
            print(f"  行为状态: {survey.mental_behavior}")
            print(f"  认知能力: {survey.mental_cognition}")
            
            print("安全风险问题:")
            print(f"  跌倒风险: {survey.safety_falling}")
            print(f"  走失风险: {survey.safety_wandering}")
            print(f"  用药安全: {survey.safety_medication}")
            print(f"  自伤风险: {survey.safety_selfHarm}")
            print(f"  意外风险: {survey.safety_accident}")
            print(f"  紧急求助: {survey.safety_emergency}")
            
            print("居住环境评估:")
            print(f"  室内布局: {survey.environment_layout}")
            print(f"  照明条件: {survey.environment_lighting}")
            print(f"  通风条件: {survey.environment_ventilation}")
            print(f"  安全设施: {survey.environment_safety}")
            print(f"  卫生条件: {survey.environment_hygiene}")
            print(f"  无障碍设施: {survey.environment_accessibility}")

if __name__ == '__main__':
    check_database() 
