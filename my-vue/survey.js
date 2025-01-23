new Vue({
    el: '#app',
    data() {
        return {
            formData: {
                eating: '',
                toilet: '',
                bathing: '',
                anxiety: '',
                depression: '',
                sleep: '',
                falling: '',
                medication: '',
                chronic_disease: '',
                lighting: '',
                bathroom_safety: '',
                emergency_device: '',
                environment_order: ''
            }
        }
    },
    methods: {
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    // 计算总分
                    let totalScore = 0;
                    for (let key in this.formData) {
                        totalScore += parseInt(this.formData[key]);
                    }

                    // 生成建议
                    let recommendation = '';
                    if (totalScore <= 20) {
                        recommendation = '低风险：建议定期评估，保持现有照护方式';
                    } else if (totalScore <= 30) {
                        recommendation = '中等风险：建议增加照护频率，注意预防措施';
                    } else {
                        recommendation = '高风险：建议寻求专业医疗照护支持，制定详细照护计划';
                    }

                    // 使用Element UI的消息框显示结果
                    this.$alert(
                        `总评分：${totalScore}\n初步建议：${recommendation}`, 
                        '评估完成', 
                        {
                            confirmButtonText: '确定',
                            callback: action => {
                                // 可以在这里添加后续处理
                            }
                        }
                    );
                }
            });
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
        }
    }
}); 