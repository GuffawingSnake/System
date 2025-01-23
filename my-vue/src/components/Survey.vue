<!-- 问卷调查组件：处理评估问卷 -->
<template>
  <page-background>
    <div class="survey-container">
      <el-card class="survey-card">
        <div slot="header">
          <h2>照护需求评估问卷</h2>
        </div><el-steps :active="activeStep" finish-status="success" align-center class="survey-steps">
          <el-step title="日常生活照护"></el-step>
          <el-step title="精神行为状况"></el-step>
          <el-step title="安全风险评估"></el-step>
          <el-step title="居住环境评估"></el-step>
        </el-steps>

        <!-- 日常生活照护评估 -->
        <el-form v-if="activeStep === 0" :model="dailyLifeForm" :rules="dailyLifeRules" ref="dailyLifeForm" label-width="180px">
          <h3>日常生活照护评估</h3>
          <el-form-item label="进食能力" prop="eating">
            <el-radio-group v-model="dailyLifeForm.eating">
              <el-radio :label="0">完全自理</el-radio>
              <el-radio :label="1">需要部分帮助</el-radio>
              <el-radio :label="2">完全依赖</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="穿衣能力" prop="dressing">
            <el-radio-group v-model="dailyLifeForm.dressing">
              <el-radio :label="0">完全自理</el-radio>
              <el-radio :label="1">需要部分帮助</el-radio>
              <el-radio :label="2">完全依赖</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="如厕能力" prop="toileting">
            <el-radio-group v-model="dailyLifeForm.toileting">
              <el-radio :label="0">完全自理</el-radio>
              <el-radio :label="1">需要部分帮助</el-radio>
              <el-radio :label="2">完全依赖</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="洗漱能力" prop="washing">
            <el-radio-group v-model="dailyLifeForm.washing">
              <el-radio :label="0">完全自理</el-radio>
              <el-radio :label="1">需要部分帮助</el-radio>
              <el-radio :label="2">完全依赖</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="活动能力" prop="mobility">
            <el-radio-group v-model="dailyLifeForm.mobility">
              <el-radio :label="0">行动自如</el-radio>
              <el-radio :label="1">需要辅助工具</el-radio>
              <el-radio :label="2">需要他人搀扶</el-radio>
            </el-radio-group>
          </el-form-item>
        </el-form>

        <!-- 精神行为状况评估 -->
        <el-form v-if="activeStep === 1" :model="mentalForm" :rules="mentalRules" ref="mentalForm" label-width="180px">
          <h3>精神行为状况评估</h3>
          <el-form-item label="记忆力状况" prop="memory">
            <el-radio-group v-model="mentalForm.memory">
              <el-radio :label="0">记忆力正常</el-radio>
              <el-radio :label="1">轻度遗忘</el-radio>
              <el-radio :label="2">严重遗忘</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="情绪状态" prop="emotion">
            <el-radio-group v-model="mentalForm.emotion">
              <el-radio :label="0">情绪稳定</el-radio>
              <el-radio :label="1">偶有波动</el-radio>
              <el-radio :label="2">情绪不稳定</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="沟通能力" prop="communication">
            <el-radio-group v-model="mentalForm.communication">
              <el-radio :label="0">表达清晰</el-radio>
              <el-radio :label="1">表达困难</el-radio>
              <el-radio :label="2">无法表达</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="行为异常" prop="behavior">
            <el-radio-group v-model="mentalForm.behavior">
              <el-radio :label="0">无异常行为</el-radio>
              <el-radio :label="1">偶有异常</el-radio>
              <el-radio :label="2">频繁异常</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="睡眠质量" prop="sleep">
            <el-radio-group v-model="mentalForm.sleep">
              <el-radio :label="0">睡眠正常</el-radio>
              <el-radio :label="1">偶有失眠</el-radio>
              <el-radio :label="2">严重失眠</el-radio>
            </el-radio-group>
          </el-form-item>
        </el-form>

        <!-- 安全风险评估 -->
        <el-form v-if="activeStep === 2" :model="safetyForm" :rules="safetyRules" ref="safetyForm" label-width="180px">
          <h3>安全风险评估</h3>
          <el-form-item label="跌倒风险" prop="fallRisk">
            <el-radio-group v-model="safetyForm.fallRisk">
              <el-radio :label="0">无风险</el-radio>
              <el-radio :label="1">中等风险</el-radio>
              <el-radio :label="2">高风险</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="走失风险" prop="wanderingRisk">
            <el-radio-group v-model="safetyForm.wanderingRisk">
              <el-radio :label="0">无风险</el-radio>
              <el-radio :label="1">偶尔走失</el-radio>
              <el-radio :label="2">频繁走失</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="误食风险" prop="swallowRisk">
            <el-radio-group v-model="safetyForm.swallowRisk">
              <el-radio :label="0">无风险</el-radio>
              <el-radio :label="1">偶有噎食</el-radio>
              <el-radio :label="2">高风险</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="用药安全" prop="medicationSafety">
            <el-radio-group v-model="safetyForm.medicationSafety">
              <el-radio :label="0">用药规范</el-radio>
              <el-radio :label="1">偶有遗漏</el-radio>
              <el-radio :label="2">用药混乱</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="自伤风险" prop="selfHarmRisk">
            <el-radio-group v-model="safetyForm.selfHarmRisk">
              <el-radio :label="0">无风险</el-radio>
              <el-radio :label="1">偶有倾向</el-radio>
              <el-radio :label="2">高风险</el-radio>
            </el-radio-group>
          </el-form-item>
        </el-form>

        <!-- 居住环境评估 -->
        <el-form v-if="activeStep === 3" :model="environmentForm" :rules="environmentRules" ref="environmentForm" label-width="180px">
          <h3>居住环境评估</h3>
          <el-form-item label="室内安全设施" prop="safeFacilities">
            <el-radio-group v-model="environmentForm.safeFacilities">
              <el-radio :label="0">设施完善</el-radio>
              <el-radio :label="1">部分缺失</el-radio>
              <el-radio :label="2">严重不足</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="居住环境整洁度" prop="cleanliness">
            <el-radio-group v-model="environmentForm.cleanliness">
              <el-radio :label="0">整洁</el-radio>
              <el-radio :label="1">一般</el-radio>
              <el-radio :label="2">脏乱</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="无障碍设施" prop="accessibility">
            <el-radio-group v-model="environmentForm.accessibility">
              <el-radio :label="0">设施完善</el-radio>
              <el-radio :label="1">部分具备</el-radio>
              <el-radio :label="2">严重缺乏</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="采光通风" prop="ventilation">
            <el-radio-group v-model="environmentForm.ventilation">
              <el-radio :label="0">良好</el-radio>
              <el-radio :label="1">一般</el-radio>
              <el-radio :label="2">差</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="居住空间" prop="livingSpace">
            <el-radio-group v-model="environmentForm.livingSpace">
              <el-radio :label="0">宽敞</el-radio>
              <el-radio :label="1">适中</el-radio>
              <el-radio :label="2">拥挤</el-radio>
            </el-radio-group>
          </el-form-item>
        </el-form>

        <!-- 操作按钮 -->
        <div class="survey-buttons">
          <el-button v-if="activeStep > 0" @click="prevStep">上一步</el-button>
          <el-button v-if="activeStep < 3" type="primary" @click="nextStep">下一步</el-button>
          <el-button v-if="activeStep === 3" type="success" @click="submitSurvey">提交评估</el-button>
        </div>
      </el-card>
    </div>
  </page-background>
</template>

<script>
export default {
  name: 'Survey',
  data () {
    return {
      activeStep: 0,
      // 日常生活照护表单
      dailyLifeForm: {
        eating: '',
        dressing: '',
        toileting: '',
        washing: '',
        mobility: ''
      },
      // 精神行为状况表单
      mentalForm: {
        memory: '',
        emotion: '',
        communication: '',
        behavior: '',
        sleep: ''
      },
      // 安全风险表单
      safetyForm: {
        fallRisk: '',
        wanderingRisk: '',
        swallowRisk: '',
        medicationSafety: '',
        selfHarmRisk: ''
      },
      // 居住环境表单
      environmentForm: {
        safeFacilities: '',
        cleanliness: '',
        accessibility: '',
        ventilation: '',
        livingSpace: ''
      },
      // 表单验证规则
      dailyLifeRules: {
        eating: [{ required: true, message: '请选择进食能力状况', trigger: 'change' }],
        dressing: [{ required: true, message: '请选择穿衣能力状况', trigger: 'change' }],
        toileting: [{ required: true, message: '请选择如厕能力状况', trigger: 'change' }],
        washing: [{ required: true, message: '请选择洗漱能力状况', trigger: 'change' }],
        mobility: [{ required: true, message: '请选择活动能力状况', trigger: 'change' }]
      },
      mentalRules: {
        memory: [{ required: true, message: '请选择记忆力状况', trigger: 'change' }],
        emotion: [{ required: true, message: '请选择情绪状态', trigger: 'change' }],
        communication: [{ required: true, message: '请选择沟通能力状况', trigger: 'change' }],
        behavior: [{ required: true, message: '请选择行为状况', trigger: 'change' }],
        sleep: [{ required: true, message: '请选择睡眠状况', trigger: 'change' }]
      },
      safetyRules: {
        fallRisk: [{ required: true, message: '请评估跌倒风险', trigger: 'change' }],
        wanderingRisk: [{ required: true, message: '请评估走失风险', trigger: 'change' }],
        swallowRisk: [{ required: true, message: '请评估误食风险', trigger: 'change' }],
        medicationSafety: [{ required: true, message: '请评估用药安全', trigger: 'change' }],
        selfHarmRisk: [{ required: true, message: '请评估自伤风险', trigger: 'change' }]
      },
      environmentRules: {
        safeFacilities: [{ required: true, message: '请评估安全设施情况', trigger: 'change' }],
        cleanliness: [{ required: true, message: '请评估环境整洁度', trigger: 'change' }],
        accessibility: [{ required: true, message: '请评估无障碍设施情况', trigger: 'change' }],
        ventilation: [{ required: true, message: '请评估采光通风情况', trigger: 'change' }],
        livingSpace: [{ required: true, message: '请评估居住空间情况', trigger: 'change' }]
      }
    }
  },
  methods: {
    // 下一步
    nextStep () {
      const formNames = ['dailyLifeForm', 'mentalForm', 'safetyForm', 'environmentForm']
      this.$refs[formNames[this.activeStep]].validate((valid) => {
        if (valid) {
          this.activeStep++
        }
      })
    },
    // 上一步
    prevStep () {
      this.activeStep--
    },
    // 提交问卷
    submitSurvey () {
      this.$refs.environmentForm.validate((valid) => {
        if (valid) {
          // 整合所有表单数据
          const surveyData = {
            dailyLife: this.dailyLifeForm,
            mental: this.mentalForm,
            safety: this.safetyForm,
            environment: this.environmentForm
          }
          // 这里可以添加提交数据的逻辑
          console.log('提交的问卷数据：', surveyData)
          this.$message.success('问卷提交成功！')
          this.$router.push('/')
        }
      })
    }
  }
}
</script>

<style scoped>
.survey-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.survey-card {
  margin-bottom: 20px;
  border-radius: 8px;
}

.survey-steps {
  margin: 30px 0;
}

.survey-buttons {
  margin-top: 30px;
  text-align: center;
}

.survey-buttons .el-button {
  margin: 0 10px;
}

h3 {
  color: #409EFF;
  margin-bottom: 20px;
  font-weight: 600;
}

.el-form-item {
  margin-bottom: 25px;
}
</style>
