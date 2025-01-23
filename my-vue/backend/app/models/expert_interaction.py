from app import db
from datetime import datetime

class ExpertInteraction(db.Model):
    __tablename__ = 'expert_interaction'
    
    id = db.Column(db.Integer, primary_key=True)
    visitor_id = db.Column(db.Integer, db.ForeignKey('visitors.id'), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='active')  # active, completed, cancelled
    question_count = db.Column(db.Integer, default=0)  # 添加问题计数字段
    
    # 关联
    chats = db.relationship('Chat', backref='interaction', lazy=True) 
