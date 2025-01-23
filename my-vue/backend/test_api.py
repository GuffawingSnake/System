import os
import requests
from dotenv import load_dotenv
from pathlib import Path
import json

# 加载环境变量
env_path = Path(__file__).parent / '.env'
load_dotenv(env_path)

def test_api():
    api_key = os.getenv('DASHSCOPE_API_KEY')
    if not api_key:
        print(f"错误: 未找到API密钥。请检查 {env_path} 文件")
        return
        
    print(f"使用API密钥: {api_key[:8]}...")
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    # 测试API连接
    url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation'
    
    data = {
        "model": "qwen-plus",
        "input": {
            "messages": [
                {
                    "role": "user",
                    "content": "你好"
                }
            ]
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"\nAPI响应状态码: {response.status_code}")
        print(f"API响应内容: {response.text}")
    except Exception as e:
        print(f"请求失败: {str(e)}")

def test_api_key(api_key):
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "qwen-turbo",
        "input": {
            "prompt": "你好"
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"请求失败: {str(e)}")
        return False

if __name__ == '__main__':
    test_api()
    api_key = "sk-b41166d0344849d9a1531142960f992e"  # 您的API密钥
    if test_api_key(api_key):
        print("API密钥有效且已激活")
    else:
        print("API密钥无效或未激活") 
