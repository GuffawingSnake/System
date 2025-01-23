from app import db
from datetime import datetime

class Survey(db.Model):
    __tablename__ = 'surveys'
    
    id = db.Column(db.Integer, primary_key=True)
    visitor_id = db.Column(db.Integer, db.ForeignKey('visitors.id'), nullable=False)
    submit_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # 日常生活照护问题
    daily_eating = db.Column(db.Integer, nullable=False)
    daily_dressing = db.Column(db.Integer, nullable=False)
    daily_toileting = db.Column(db.Integer, nullable=False)
    daily_bathing = db.Column(db.Integer, nullable=False)
    daily_indoor = db.Column(db.Integer, nullable=False)
    daily_outdoor = db.Column(db.Integer, nullable=False)
    
    # 精神行为问题
    mental_memory = db.Column(db.Integer, nullable=False)
    mental_emotion = db.Column(db.Integer, nullable=False)
    mental_sleep = db.Column(db.Integer, nullable=False)
    mental_communication = db.Column(db.Integer, nullable=False)
    mental_behavior = db.Column(db.Integer, nullable=False)
    mental_cognition = db.Column(db.Integer, nullable=False)
    
    # 安全风险问题
    safety_falling = db.Column(db.Integer, nullable=False)
    safety_wandering = db.Column(db.Integer, nullable=False)
    safety_medication = db.Column(db.Integer, nullable=False)
    safety_selfHarm = db.Column(db.Integer, nullable=False)
    safety_accident = db.Column(db.Integer, nullable=False)
    safety_emergency = db.Column(db.Integer, nullable=False)
    
    # 居住环境评估
    environment_layout = db.Column(db.Integer, nullable=False)
    environment_lighting = db.Column(db.Integer, nullable=False)
    environment_ventilation = db.Column(db.Integer, nullable=False)
    environment_safety = db.Column(db.Integer, nullable=False)
    environment_hygiene = db.Column(db.Integer, nullable=False)
    environment_accessibility = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Survey {self.id} by Visitor {self.visitor_id}>'
