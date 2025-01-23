from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os
from pathlib import Path
from dotenv import load_dotenv

# 加载环境变量
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # 打印环境变量
    print(f"DASHSCOPE_API_KEY: {os.getenv('DASHSCOPE_API_KEY')[:8]}...")
    
    # 确保数据库目录存在
    db_path = Path(app.config['DB_PATH'])
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 初始化扩展
    db.init_app(app)
    migrate.init_app(app, db)
    
    # 注册所有蓝图
    from app.routes.visitor import visitor_bp
    from app.routes.chat import chat_bp
    from app.routes.health import health_bp
    
    app.register_blueprint(visitor_bp, url_prefix='/api/visitor')
    app.register_blueprint(chat_bp, url_prefix='/api/chat')
    app.register_blueprint(health_bp, url_prefix='/api/health')
    
    # 创建数据库表
    with app.app_context():
        # 删除所有表（按正确顺序）
        try:
            # 先删除有外键约束的表
            if db.metadata.tables.get('surveys'):
                db.session.execute('DROP TABLE IF EXISTS surveys')
            if db.metadata.tables.get('chat'):
                db.session.execute('DROP TABLE IF EXISTS chat')
            if db.metadata.tables.get('expert_interaction'):
                db.session.execute('DROP TABLE IF EXISTS expert_interaction')
            # 再删除被引用的表
            if db.metadata.tables.get('visitors'):
                db.session.execute('DROP TABLE IF EXISTS visitors')
            db.session.commit()
        except Exception as e:
            print(f"删除表时出错: {e}")
            db.session.rollback()
        
        # 创建所有表
        db.create_all()
        print("数据库表已重新创建")
    
    return app 
