import os
import requests
from dotenv import load_dotenv
from pathlib import Path
import time

# 加载环境变量
env_path = Path(__file__).parent.parent.parent / '.env'
print(f"尝试加载环境变量文件: {env_path}")
load_dotenv(env_path)

class QianwenService:
    def __init__(self):
        self.api_key = os.getenv('DASHSCOPE_API_KEY')
        if not self.api_key:
            raise Exception(f"未找到 DASHSCOPE_API_KEY 环境变量。请检查 {env_path} 文件")
            
        # 清理API密钥格式
        self.api_key = self.api_key.strip()  # 移除空白字符
        if not self.api_key.startswith('sk-'):
            self.api_key = f'sk-{self.api_key}'  # 确保有sk-前缀
            
        print(f"成功加载API密钥: {self.api_key[:8]}...")
        
        # 设置认证头和API URL
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',  # 使用Bearer认证格式
            'Content-Type': 'application/json'
        }
        self.url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation'
        
    def get_response(self, messages):
        """获取AI响应"""
        max_retries = 3
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                print("\n=== API请求信息 ===")
                print(f"使用API密钥: {self.api_key[:8]}...")
                print(f"Headers: {self.headers}")
                print(f"Messages: {messages}")
                
                # 构造请求数据
                data = {
                    "model": "qwen-turbo",
                    "input": {
                        "messages": messages
                    }
                }
                
                # 发送请求
                response = requests.post(self.url, headers=self.headers, json=data)
                
                print("\n=== API响应信息 ===")
                print(f"Status Code: {response.status_code}")
                print(f"Response: {response.text}")
                
                if response.status_code == 200:
                    result = response.json()
                    return result['output']['text']
                elif response.status_code == 401:
                    raise Exception(f"API密钥无效。响应内容: {response.text}")
                elif response.status_code == 429:
                    retry_count += 1
                    time.sleep(2 ** retry_count)
                    continue
                else:
                    raise Exception(f"API调用失败 ({response.status_code}): {response.text}")
                    
            except Exception as e:
                if retry_count < max_retries - 1:
                    retry_count += 1
                    time.sleep(2 ** retry_count)
                    continue
                raise e
                
        raise Exception("请求失败，请稍后重试")

# 创建服务实例
qianwen_service = QianwenService()

# 测试代码
if __name__ == '__main__':
    try:
        response = qianwen_service.get_response([{
            "role": "user",
            "content": "你好"
        }])
        print(f"AI响应: {response}")
    except Exception as e:
        print(f"测试失败: {str(e)}")
      