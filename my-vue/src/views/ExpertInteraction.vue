<template>
  <div class="expert-interaction">
    <el-card class="chat-container">
      <div slot="header" class="chat-header">
        <h2>AI 智慧照护专家</h2>
        <p class="subtitle">24小时在线，为您解答照护问题</p>
      </div>

      <div class="chat-content" ref="chatContent">
        <div v-for="(message, index) in chatHistory" :key="index"
          :class="['message', message.type === 'user' ? 'user-message' : 'ai-message']">
          <div class="avatar">
            <i :class="message.type === 'user' ? 'el-icon-user' : 'el-icon-service'"></i>
          </div>
          <div class="message-content">
            <p v-html="formatMessage(message.content)"></p>
            <span class="time">{{ message.time }}</span>
          </div>
        </div>
      </div>

      <div class="chat-input">
        <el-input
          v-model="userInput"
          type="textarea"
          :rows="3"
          placeholder="请输入您的问题，AI专家将为您解答..."
          @keyup.enter.native="sendMessage"
          :disabled="loading || cooldown > 0"
        ></el-input>
        <div class="button-group">
          <el-button 
            type="primary" 
            @click="sendMessage" 
            :loading="loading"
            :disabled="!userInput.trim() || cooldown > 0"
          >
            {{ cooldown > 0 ? `请等待 ${cooldown} 秒` : '发送' }}
          </el-button>
          <el-button @click="clearChat">清空对话</el-button>
        </div>
      </div>

      <div class="quick-questions">
        <h3>常见问题快速提问：</h3>
        <el-button
          v-for="(question, index) in quickQuestions"
          :key="index"
          size="small"
          @click="askQuickQuestion(question)">{{ question }}</el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
import { getAIResponse } from '@/api/ai'
import { debounce } from 'lodash'

export default {
  name: 'ExpertInteraction',
  data () {
    return {
      chatHistory: [],
      userInput: '',
      loading: false,
      cooldown: 0,
      cooldownTimer: null,
      quickQuestions: [
        '如何应对老人的睡眠问题？',
        '老人不愿意吃饭怎么办？',
        '如何预防老人跌倒？',
        '老人出现幻觉该怎么办？'
      ]
    }
  },
  methods: {
    formatMessage (text) {
      return text.replace(/\n/g, '<br>')
    },
    startCooldown(seconds) {
      this.cooldown = seconds
      if (this.cooldownTimer) {
        clearInterval(this.cooldownTimer)
      }
      this.cooldownTimer = setInterval(() => {
        if (this.cooldown > 0) {
          this.cooldown--
        } else {
          clearInterval(this.cooldownTimer)
        }
      }, 1000)
    },
    async sendMessage () {
      if (!this.userInput.trim() || this.loading || this.cooldown > 0) return

      this.addMessage(this.userInput, 'user')
      const question = this.userInput
      this.userInput = ''
      this.loading = true

      try {
        console.log('发送问题:', question)
        const response = await getAIResponse(question)
        console.log('收到回答:', response)
        this.addMessage(response, 'ai')
      } catch (error) {
        console.error('发送消息错误:', error)
        // 检查是否是频率限制错误
        if (error.message.includes('请等待')) {
          const seconds = parseInt(error.message.match(/\d+/)[0])
          this.startCooldown(seconds)
          this.$message.warning(error.message)
        } else {
          this.$message.error(error.message || '抱歉，服务出现异常，请稍后重试')
          this.addMessage('抱歉，系统暂时无法回答您的问题。请稍后再试。', 'ai')
        }
      } finally {
        this.loading = false
        this.$nextTick(() => {
          this.scrollToBottom()
        })
      }
    },
    addMessage (content, type) {
      this.chatHistory.push({
        content,
        type,
        time: new Date().toLocaleTimeString()
      })
    },
    scrollToBottom () {
      const chatContent = this.$refs.chatContent
      chatContent.scrollTop = chatContent.scrollHeight
    },
    clearChat () {
      this.$confirm('确定要清空所有对话记录吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.chatHistory = []
        this.$message.success('对话记录已清空')
      })
    },
    askQuickQuestion (question) {
      this.userInput = question
      this.sendMessage()
    },
    async getAIResponse (question) {
      try {
        const response = await getAIResponse(question)
        return response
      } catch (error) {
        console.error('AI Response Error:', error)
        return '抱歉,系统暂时无法回答您的问题。请稍后再试或换个方式提问。'
      }
    }
  },
  beforeDestroy() {
    if (this.cooldownTimer) {
      clearInterval(this.cooldownTimer)
    }
  },
  mounted () {
    this.addMessage('您好！我是AI智慧照护专家，很高兴为您服务。您可以询问任何关于老年照护的问题，我会尽力为您解答。', 'ai')
  }
}
</script>

<style scoped>
.expert-interaction {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

.chat-container {
  min-height: 600px;
  display: flex;
  flex-direction: column;
}

.chat-header {
  text-align: center;
}

.chat-header h2 {
  color: #409EFF;
  margin-bottom: 10px;
}

.subtitle {
  color: #606266;
  margin: 0;
}

.chat-content {
  flex: 1;
  min-height: 400px;
  max-height: 600px;
  overflow-y: auto;
  padding: 20px;
  background: #f5f7fa;
  border-radius: 4px;
  margin-bottom: 20px;
}

.message {
  display: flex;
  margin-bottom: 20px;
  align-items: flex-start;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 10px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.avatar i {
  font-size: 20px;
  color: #409EFF;
}

.message-content {
  flex: 1;
  padding: 10px 15px;
  border-radius: 4px;
  position: relative;
  max-width: 80%;
}

.user-message .message-content {
  background: #409EFF;
  color: #fff;
}

.ai-message .message-content {
  background: #fff;
  color: #303133;
}

.message-content p {
  margin: 0;
  line-height: 1.6;
}

.time {
  font-size: 12px;
  color: #909399;
  position: absolute;
  bottom: -20px;
  right: 0;
}

.chat-input {
  margin-bottom: 20px;
}

.button-group {
  margin-top: 10px;
  text-align: right;
}

.button-group .el-button {
  margin-left: 10px;
}

.quick-questions {
  border-top: 1px solid #EBEEF5;
  padding-top: 20px;
}

.quick-questions h3 {
  margin-bottom: 15px;
  color: #303133;
}

.quick-questions .el-button {
  margin: 5px;
}

.chat-content::-webkit-scrollbar {
  width: 6px;
}

.chat-content::-webkit-scrollbar-thumb {
  background: #909399;
  border-radius: 3px;
}

.chat-content::-webkit-scrollbar-track {
  background: #f5f7fa;
}
</style>
