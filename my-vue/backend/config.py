import os
from pathlib import Path

# 获取当前文件所在目录
basedir = Path(__file__).parent

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    
    # 数据库配置
    DB_PATH = basedir / 'app.db'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    
    # 通义千问配置
    DASHSCOPE_API_KEY = os.environ.get('DASHSCOPE_API_KEY')
    
    # SQLite配置
    SQLALCHEMY_ENGINE_OPTIONS = {
        'isolation_level': None,  # 让SQLAlchemy管理事务
        'connect_args': {
            'check_same_thread': False,  # 允许多线程访问
            'timeout': 30  # 连接超时时间
        }
    }
