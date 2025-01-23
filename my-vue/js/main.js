// 确保 ELEMENT 已经被正确加载
if (typeof ELEMENT === 'undefined') {
    console.error('Element UI 未正确加载！');
}

// 使用 Element UI
Vue.use(ELEMENT);

new Vue({
    el: '#app',
    data() {
        return {
            activeIndex: '1'
        }
    },
    methods: {
        handleSelect(key, keyPath) {
            console.log(key, keyPath);
        },
        goToSurvey() {
            window.location.href = 'survey.html';
        },
        showSolutions() {
            this.$message({
                message: '正在开发中...',
                type: 'info'
            });
        }
    },
    mounted() {
        console.log('Vue 实例已挂载');
    }
}); 