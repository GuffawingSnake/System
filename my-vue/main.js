// 创建Vue实例并使用Element UI
Vue.use(ElementUI);

new Vue({
    el: '#app',
    data() {
        return {
            activeIndex: '/'
        }
    },
    methods: {
        goToSurvey() {
            window.location.href = 'survey.html';
        },
        showSolutions() {
            this.$message({
                message: '正在开发中...',
                type: 'info'
            });
        }
    }
}); 