<template>
  <el-menu :default-active="activeIndex" class="nav-menu" mode="horizontal" router>
    <el-menu-item index="/">首页</el-menu-item>
    <el-menu-item index="/records">我的记录</el-menu-item>
    <el-menu-item index="/expert-chat">专家互动</el-menu-item>
  </el-menu>
</template>

<script>
export default {
  name: 'NavMenu',
  data() {
    return {
      activeIndex: this.$route.path
    }
  }
}
</script>

<style scoped>
.nav-menu {
  padding: 0 20px;
}
</style> 
