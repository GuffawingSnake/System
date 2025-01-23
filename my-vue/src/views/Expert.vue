<template>
  <div class="expert">
    <h2>专家互动</h2>
    <el-card class="chat-box">
      <div class="message-list">
        <!-- 消息列表 -->
      </div>
      <div class="message-input">
        <el-input
          v-model="message"
          placeholder="请输入消息"
          type="textarea"
          :rows="3"
        ></el-input>
        <el-button type="primary" @click="sendMessage">发送</el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'Expert',
  data () {
    return {
      message: ''
    }
  },
  methods: {
    sendMessage () {
      if (this.message.trim()) {
        // 处理发送消息
        this.message = ''
      }
    }
  }
}
</script>

<style scoped>
.expert {
  padding: 20px;
}

.chat-box {
  margin: 20px 0;
}

.message-list {
  min-height: 300px;
  margin-bottom: 20px;
}

.message-input {
  display: flex;
  gap: 10px;
}

.message-input .el-button {
  align-self: flex-end;
}
</style>
