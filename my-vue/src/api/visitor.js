import axios from 'axios'

// 强制使用相对路径，确保走代理
const API_URL = '/api'

// 创建axios实例
const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json'
  },
  // 添加这些选项
  withCredentials: true,
  timeout: 10000
})

export const trackVisitor = async () => {
  try {
    console.log('发送访客追踪请求到:', `${API_URL}/visitor/track`)
    const response = await apiClient.post('/visitor/track')
    console.log('访客追踪响应:', response.data)
    
    if (response.data && response.data.visitor_id) {
      localStorage.setItem('visitor_id', response.data.visitor_id)
      return response.data.visitor_id
    }
    throw new Error('未收到有效的访客ID')
  } catch (error) {
    console.error('访客追踪失败:', {
      message: error.message,
      response: error.response?.data,
      status: error.response?.status
    })
    throw error
  }
}

export const trackLeave = async () => {
  try {
    const visitor_id = localStorage.getItem('visitor_id')
    if (visitor_id) {
      await apiClient.post('/visitor/leave', { visitor_id })
    }
  } catch (error) {
    console.error('记录离开时间失败:', error)
  }
} 
