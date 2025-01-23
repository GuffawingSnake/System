<template>
  <div class="clock-container">
    <div class="clock">
      <div class="time">{{ timeString }}</div>
      <div class="date">{{ dateString }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DigitalClock',
  data () {
    return {
      time: new Date(),
      timer: null
    }
  },
  computed: {
    timeString () {
      return this.time.toLocaleTimeString('zh-CN', {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
      })
    },
    dateString () {
      return this.time.toLocaleDateString('zh-CN', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        weekday: 'long'
      })
    }
  },
  mounted () {
    this.timer = setInterval(() => {
      this.time = new Date()
    }, 1000)
  },
  beforeDestroy () {
    if (this.timer) {
      clearInterval(this.timer)
    }
  }
}
</script>

<style scoped>
.clock-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.clock {
  background: linear-gradient(135deg, #409EFF, #66b1ff);
  padding: 24px 48px;
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(64, 158, 255, 0.2);
  text-align: center;
  color: white;
  transition: all 0.3s ease;
}

.clock:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 28px rgba(64, 158, 255, 0.3);
}

.time {
  font-size: 48px;
  font-weight: 600;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  font-family: 'Helvetica Neue', Arial, sans-serif;
  letter-spacing: 2px;
}

.date {
  font-size: 18px;
  margin-top: 8px;
  opacity: 0.9;
  font-weight: 500;
}

@media screen and (max-width: 768px) {
  .clock {
    padding: 16px 32px;
  }
  .time {
    font-size: 36px;
  }
  .date {
    font-size: 16px;
  }
}
</style>
