<template>
  <div class="page-background" :style="backgroundStyle">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'PageBackground',
  props: {
    image: {
      type: String,
      default: '/images/background.jpg'
    }
  },
  computed: {
    backgroundStyle () {
      return {
        backgroundImage: `linear-gradient(rgba(245, 247, 250, 0.92), rgba(245, 247, 250, 0.92)), url(${this.image})`
      }
    }
  }
}
</script>

<style scoped>
.page-background {
  min-height: 100vh;
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  position: relative;
  padding: 30px;
}

@media screen and (max-width: 768px) {
  .page-background {
    padding: 16px;
  }
}
</style>
