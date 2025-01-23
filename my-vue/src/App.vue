<template>
  <div id="app">
    <nav-menu></nav-menu>
    <router-view></router-view>
  </div>
</template>

<script>
import NavMenu from '@/components/NavMenu'
import { trackVisitor } from '@/api/visitor'

export default {
  name: 'App',
  components: {
    NavMenu
  },
  async created() {
    try {
      // 在应用创建时追踪访客
      await trackVisitor()
    } catch (error) {
      console.error('访客追踪失败:', error)
    }
  }
}
</script>

<style>
#app {
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
