from app import db
from datetime import datetime

class Chat(db.Model):
    __tablename__ = 'chat'
    
    id = db.Column(db.Integer, primary_key=True)
    visitor_id = db.Column(db.Integer, db.ForeignKey('visitors.id'), nullable=True)
    interaction_id = db.Column(db.Integer, db.ForeignKey('expert_interaction.id'))
    content = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(10), nullable=False)  # 'user' 或 'ai'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow) 
