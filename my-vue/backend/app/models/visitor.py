from app import db
from datetime import datetime

class Visitor(db.Model):
    __tablename__ = 'visitors'
    
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(50), nullable=False)
    user_agent = db.Column(db.String(200))
    visit_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    leave_time = db.Column(db.DateTime)
    
    # 添加关系
    surveys = db.relationship('Survey', backref='visitor', lazy=True)
    chats = db.relationship('Chat', backref='visitor', lazy=True)
    interactions = db.relationship('ExpertInteraction', backref='visitor', lazy=True)
    
    def __repr__(self):
        return f'<Visitor {self.id}: {self.ip_address}>'
