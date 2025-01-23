import axios from 'axios'

const API_URL = process.env.VUE_APP_API_URL || '/api'

export const getAIResponse = async (message) => {
  try {
    const visitorId = localStorage.getItem('visitorId')
    console.log('发送请求:', {
      message,
      visitor_id: visitorId
    });
    
    const response = await axios.post(`${API_URL}/chat/message`, {
      message,
      visitor_id: visitorId
    })
    
    console.log('API响应:', response.data);
    
    // 保存新的visitorId（如果是新访客）
    if (response.data.visitor_id && !visitorId) {
      localStorage.setItem('visitorId', response.data.visitor_id)
    }
    
    return response.data.response
  } catch (error) {
    console.error('AI服务调用错误:', error)
    if (error.response?.data?.error) {
      throw new Error(error.response.data.error)
    }
    throw new Error('AI服务暂时不可用，请稍后重试')
  }
}

export const getChatHistory = async () => {
  try {
    const visitorId = localStorage.getItem('visitorId')
    if (!visitorId) {
      return []
    }
    
    const response = await axios.get(`${API_URL}/chat/history`, {
      params: { visitor_id: visitorId }
    })
    return response.data
  } catch (error) {
    console.error('获取聊天记录失败:', error)
    throw new Error('获取聊天记录失败，请稍后重试')
  }
}
