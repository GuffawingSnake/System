<template>
  <div class="care-plan">
    <el-card class="plan-container">
      <div slot="header">
        <h2>个性化照护方案</h2>
      </div>

      <div class="no-plan" v-if="!hasSurveyData">
        <el-empty description="暂无评估数据">
          <el-button type="primary" @click="$router.push('/survey')">
            去做评估
          </el-button>
        </el-empty>
      </div>

      <div class="plan-content" v-else>
        <el-collapse v-model="activeNames">
          <el-collapse-item title="日常生活照护建议" name="1">
            <div class="plan-section">
              <h4>进食照护</h4>
              <ul>
                <li>根据评估结果定制进食协助方案</li>
                <li>选择适合的餐具和食物形态</li>
                <li>建立规律的用餐时间</li>
              </ul>

              <h4>如厕照护</h4>
              <ul>
                <li>制定个性化如厕协助计划</li>
                <li>安装必要的安全扶手</li>
                <li>保持卫生间的安全和整洁</li>
              </ul>
            </div>
          </el-collapse-item>

          <el-collapse-item title="情绪与行为管理" name="2">
            <div class="plan-section">
              <h4>情绪管理</h4>
              <ul>
                <li>建立情绪观察记录</li>
                <li>制定情绪波动应对策略</li>
                <li>营造安全舒适的环境</li>
              </ul>

              <h4>行为引导</h4>
              <ul>
                <li>保持生活规律性</li>
                <li>适当的社交活动安排</li>
                <li>制定行为干预计划</li>
              </ul>
            </div>
          </el-collapse-item>

          <el-collapse-item title="安全与预防措施" name="3">
            <div class="plan-section">
              <h4>跌倒预防</h4>
              <ul>
                <li>居家环境安全评估和改造建议</li>
                <li>适当的运动计划</li>
                <li>必要的辅助器具使用</li>
              </ul>

              <h4>意外防范</h4>
              <ul>
                <li>紧急联系人制度</li>
                <li>用药安全管理</li>
                <li>意外处理流程</li>
              </ul>
            </div>
          </el-collapse-item>
        </el-collapse>

        <div class="plan-actions">
          <el-button type="primary" @click="printPlan">打印方案</el-button>
          <el-button type="success" @click="savePlan">保存方案</el-button>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'CarePlan',
  data () {
    return {
      activeNames: ['1'],
      hasSurveyData: false // 这里应该根据实际评估数据来设置
    }
  },
  methods: {
    printPlan () {
      window.print()
    },
    savePlan () {
      this.$message.success('方案已保存')
    }
  },
  mounted () {
    // 这里应该获取评估数据
    // 暂时mock一个数据
    this.hasSurveyData = true
  }
}
</script>

<style scoped>
.care-plan {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

.plan-container {
  margin-bottom: 20px;
}

.plan-container h2 {
  color: #409EFF;
  text-align: center;
  margin: 0;
}

.no-plan {
  padding: 40px 0;
}

.plan-section {
  padding: 10px;
}

.plan-section h4 {
  color: #409EFF;
  margin: 15px 0 10px;
}

.plan-section ul {
  padding-left: 20px;
  margin: 10px 0;
}

.plan-section li {
  line-height: 1.8;
  color: #606266;
}

.plan-actions {
  margin-top: 20px;
  text-align: center;
}

.plan-actions .el-button {
  margin: 0 10px;
}

@media print {
  .plan-actions {
    display: none;
  }
}
</style>
