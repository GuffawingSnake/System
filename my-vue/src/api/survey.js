import axios from 'axios'

// 使用相对路径，让代理配置生效
const API_URL = '/api'

export const submitSurvey = async (surveyData) => {
  try {
    const response = await axios.post(`${API_URL}/visitor/survey`, surveyData)
    return response.data
  } catch (error) {
    console.error('提交问卷失败:', error)
    throw error
  }
}

export const getSurveys = async () => {
  try {
    const response = await axios.get(`${API_URL}/survey/list`)
    return response.data
  } catch (error) {
    console.error('获取问卷列表失败:', error)
    throw error
  }
} 
