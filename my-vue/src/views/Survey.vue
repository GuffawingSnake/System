<template>
  <div class="survey">
      <el-card class="survey-card">
        <div slot="header">
        <h2>老年照护需求调查问卷</h2>
        </div>
        
        <el-steps :active="activeStep" finish-status="success" align-center class="survey-steps">
        <el-step title="日常生活照护"></el-step>
        <el-step title="精神行为问题"></el-step>
        <el-step title="安全风险问题"></el-step>
        <el-step title="居住环境评估"></el-step>
        </el-steps>

      <el-form :model="surveyForm" :rules="rules" ref="surveyForm" label-width="120px">
        <!-- 第一部分：日常生活照护问题 -->
        <div v-show="activeStep === 0">
          <h3>日常生活照护问题</h3>
          <el-form-item prop="daily.eating">
            <template slot="label">
              进食能力
            </template>
            <el-radio-group v-model="surveyForm.daily.eating">
              <el-radio id="daily-eating-2" :label="2">
                <label for="daily-eating-2">完全自理</label>
              </el-radio>
              <el-radio id="daily-eating-1" :label="1">
                <label for="daily-eating-1">部分需要帮助</label>
              </el-radio>
              <el-radio id="daily-eating-0" :label="0">
                <label for="daily-eating-0">完全依赖</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="daily.dressing">
            <template slot="label">
              穿衣能力
            </template>
            <el-radio-group v-model="surveyForm.daily.dressing">
              <el-radio id="daily-dressing-2" :label="2">
                <label for="daily-dressing-2">完全自理</label>
              </el-radio>
              <el-radio id="daily-dressing-1" :label="1">
                <label for="daily-dressing-1">部分需要帮助</label>
              </el-radio>
              <el-radio id="daily-dressing-0" :label="0">
                <label for="daily-dressing-0">完全依赖</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="daily.toileting">
            <template slot="label">
              如厕能力
            </template>
            <el-radio-group v-model="surveyForm.daily.toileting">
              <el-radio id="daily-toileting-2" :label="2">
                <label for="daily-toileting-2">完全自理</label>
              </el-radio>
              <el-radio id="daily-toileting-1" :label="1">
                <label for="daily-toileting-1">部分需要帮助</label>
              </el-radio>
              <el-radio id="daily-toileting-0" :label="0">
                <label for="daily-toileting-0">完全依赖</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="daily.bathing">
            <template slot="label">
              洗澡能力
            </template>
            <el-radio-group v-model="surveyForm.daily.bathing">
              <el-radio id="daily-bathing-2" :label="2">
                <label for="daily-bathing-2">完全自理</label>
              </el-radio>
              <el-radio id="daily-bathing-1" :label="1">
                <label for="daily-bathing-1">部分需要帮助</label>
              </el-radio>
              <el-radio id="daily-bathing-0" :label="0">
                <label for="daily-bathing-0">完全依赖</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="daily.indoor">
            <template slot="label">
              室内活动
            </template>
            <el-radio-group v-model="surveyForm.daily.indoor">
              <el-radio id="daily-indoor-2" :label="2">
                <label for="daily-indoor-2">自如行走</label>
              </el-radio>
              <el-radio id="daily-indoor-1" :label="1">
                <label for="daily-indoor-1">需要辅助</label>
              </el-radio>
              <el-radio id="daily-indoor-0" :label="0">
                <label for="daily-indoor-0">无法行走</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="daily.outdoor">
            <template slot="label">
              户外活动
            </template>
            <el-radio-group v-model="surveyForm.daily.outdoor">
              <el-radio id="daily-outdoor-2" :label="2">
                <label for="daily-outdoor-2">自如行走</label>
              </el-radio>
              <el-radio id="daily-outdoor-1" :label="1">
                <label for="daily-outdoor-1">需要辅助</label>
              </el-radio>
              <el-radio id="daily-outdoor-0" :label="0">
                <label for="daily-outdoor-0">无法行走</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
        </div>

        <!-- 第二部分：精神行为问题 -->
        <div v-show="activeStep === 1">
          <h3>精神行为问题</h3>
          <el-form-item prop="mental.memory">
            <template slot="label">
              <label>记忆力</label>
            </template>
            <el-radio-group v-model="surveyForm.mental.memory">
              <el-radio id="mental-memory-2" :label="2">
                <label for="mental-memory-2">正常</label>
              </el-radio>
              <el-radio id="mental-memory-1" :label="1">
                <label for="mental-memory-1">轻度障碍</label>
              </el-radio>
              <el-radio id="mental-memory-0" :label="0">
                <label for="mental-memory-0">严重障碍</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="mental.emotion">
            <template slot="label">
              <label>情绪状态</label>
            </template>
            <el-radio-group v-model="surveyForm.mental.emotion">
              <el-radio id="mental-emotion-2" :label="2">
                <label for="mental-emotion-2">稳定</label>
              </el-radio>
              <el-radio id="mental-emotion-1" :label="1">
                <label for="mental-emotion-1">偶尔波动</label>
              </el-radio>
              <el-radio id="mental-emotion-0" :label="0">
                <label for="mental-emotion-0">经常波动</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="mental.sleep">
            <template slot="label">
              <label>睡眠质量</label>
            </template>
            <el-radio-group v-model="surveyForm.mental.sleep">
              <el-radio id="mental-sleep-2" :label="2">
                <label for="mental-sleep-2">良好</label>
              </el-radio>
              <el-radio id="mental-sleep-1" :label="1">
                <label for="mental-sleep-1">一般</label>
              </el-radio>
              <el-radio id="mental-sleep-0" :label="0">
                <label for="mental-sleep-0">差</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="mental.communication">
            <template slot="label">
              <label>沟通能力</label>
            </template>
            <el-radio-group v-model="surveyForm.mental.communication">
              <el-radio id="mental-communication-2" :label="2">
                <label for="mental-communication-2">正常</label>
              </el-radio>
              <el-radio id="mental-communication-1" :label="1">
                <label for="mental-communication-1">部分障碍</label>
              </el-radio>
              <el-radio id="mental-communication-0" :label="0">
                <label for="mental-communication-0">严重障碍</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="mental.behavior">
            <template slot="label">
              <label>行为异常</label>
            </template>
            <el-radio-group v-model="surveyForm.mental.behavior">
              <el-radio id="mental-behavior-2" :label="2">
                <label for="mental-behavior-2">无</label>
              </el-radio>
              <el-radio id="mental-behavior-1" :label="1">
                <label for="mental-behavior-1">偶尔</label>
              </el-radio>
              <el-radio id="mental-behavior-0" :label="0">
                <label for="mental-behavior-0">频繁</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="mental.cognition">
            <template slot="label">
              <label>认知能力</label>
            </template>
            <el-radio-group v-model="surveyForm.mental.cognition">
              <el-radio id="mental-cognition-2" :label="2">
                <label for="mental-cognition-2">正常</label>
              </el-radio>
              <el-radio id="mental-cognition-1" :label="1">
                <label for="mental-cognition-1">轻度下降</label>
              </el-radio>
              <el-radio id="mental-cognition-0" :label="0">
                <label for="mental-cognition-0">严重下降</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
        </div>

        <!-- 第三部分：安全风险问题 -->
        <div v-show="activeStep === 2">
          <h3>安全风险问题</h3>
          <el-form-item prop="safety.falling">
            <template slot="label">
              <label>跌倒风险</label>
            </template>
            <el-radio-group v-model="surveyForm.safety.falling">
              <el-radio id="safety-falling-2" :label="2">
                <label for="safety-falling-2">低风险</label>
              </el-radio>
              <el-radio id="safety-falling-1" :label="1">
                <label for="safety-falling-1">中等风险</label>
              </el-radio>
              <el-radio id="safety-falling-0" :label="0">
                <label for="safety-falling-0">高风险</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="safety.wandering">
            <template slot="label">
              <label>走失风险</label>
            </template>
            <el-radio-group v-model="surveyForm.safety.wandering">
              <el-radio id="safety-wandering-2" :label="2">
                <label for="safety-wandering-2">无</label>
              </el-radio>
              <el-radio id="safety-wandering-1" :label="1">
                <label for="safety-wandering-1">偶尔</label>
              </el-radio>
              <el-radio id="safety-wandering-0" :label="0">
                <label for="safety-wandering-0">频繁</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="safety.medication">
            <template slot="label">
              <label>用药安全</label>
            </template>
            <el-radio-group v-model="surveyForm.safety.medication">
              <el-radio id="safety-medication-2" :label="2">
                <label for="safety-medication-2">能自行管理</label>
              </el-radio>
              <el-radio id="safety-medication-1" :label="1">
                <label for="safety-medication-1">需要提醒</label>
              </el-radio>
              <el-radio id="safety-medication-0" :label="0">
                <label for="safety-medication-0">需要他人管理</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="safety.selfHarm">
            <template slot="label">
              <label>自伤风险</label>
            </template>
            <el-radio-group v-model="surveyForm.safety.selfHarm">
              <el-radio id="safety-selfHarm-2" :label="2">
                <label for="safety-selfHarm-2">无</label>
              </el-radio>
              <el-radio id="safety-selfHarm-1" :label="1">
                <label for="safety-selfHarm-1">偶尔</label>
              </el-radio>
              <el-radio id="safety-selfHarm-0" :label="0">
                <label for="safety-selfHarm-0">频繁</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="safety.accident">
            <template slot="label">
              <label>意外风险</label>
            </template>
            <el-radio-group v-model="surveyForm.safety.accident">
              <el-radio id="safety-accident-2" :label="2">
                <label for="safety-accident-2">低风险</label>
              </el-radio>
              <el-radio id="safety-accident-1" :label="1">
                <label for="safety-accident-1">中等风险</label>
              </el-radio>
              <el-radio id="safety-accident-0" :label="0">
                <label for="safety-accident-0">高风险</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="safety.emergency">
            <template slot="label">
              <label>紧急求助</label>
            </template>
            <el-radio-group v-model="surveyForm.safety.emergency">
              <el-radio id="safety-emergency-2" :label="2">
                <label for="safety-emergency-2">能够求助</label>
              </el-radio>
              <el-radio id="safety-emergency-1" :label="1">
                <label for="safety-emergency-1">部分能力</label>
              </el-radio>
              <el-radio id="safety-emergency-0" :label="0">
                <label for="safety-emergency-0">无法求助</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
        </div>

        <!-- 第四部分：居住环境评估 -->
        <div v-show="activeStep === 3">
          <h3>居住环境评估</h3>
          <el-form-item prop="environment.layout">
            <template slot="label">
              <label>室内布局</label>
            </template>
            <el-radio-group v-model="surveyForm.environment.layout">
              <el-radio id="environment-layout-2" :label="2">
                <label for="environment-layout-2">合理</label>
              </el-radio>
              <el-radio id="environment-layout-1" :label="1">
                <label for="environment-layout-1">部分不合理</label>
              </el-radio>
              <el-radio id="environment-layout-0" :label="0">
                <label for="environment-layout-0">不合理</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="environment.lighting">
            <template slot="label">
              <label>照明条件</label>
            </template>
            <el-radio-group v-model="surveyForm.environment.lighting">
              <el-radio id="environment-lighting-2" :label="2">
                <label for="environment-lighting-2">充足</label>
              </el-radio>
              <el-radio id="environment-lighting-1" :label="1">
                <label for="environment-lighting-1">一般</label>
              </el-radio>
              <el-radio id="environment-lighting-0" :label="0">
                <label for="environment-lighting-0">不足</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="environment.ventilation">
            <template slot="label">
              <label>通风条件</label>
            </template>
            <el-radio-group v-model="surveyForm.environment.ventilation">
              <el-radio id="environment-ventilation-2" :label="2">
                <label for="environment-ventilation-2">良好</label>
              </el-radio>
              <el-radio id="environment-ventilation-1" :label="1">
                <label for="environment-ventilation-1">一般</label>
              </el-radio>
              <el-radio id="environment-ventilation-0" :label="0">
                <label for="environment-ventilation-0">差</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="environment.safety">
            <template slot="label">
              <label>安全设施</label>
            </template>
            <el-radio-group v-model="surveyForm.environment.safety">
              <el-radio id="environment-safety-2" :label="2">
                <label for="environment-safety-2">完善</label>
              </el-radio>
              <el-radio id="environment-safety-1" :label="1">
                <label for="environment-safety-1">部分具备</label>
              </el-radio>
              <el-radio id="environment-safety-0" :label="0">
                <label for="environment-safety-0">缺乏</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="environment.hygiene">
            <template slot="label">
              <label>卫生条件</label>
            </template>
            <el-radio-group v-model="surveyForm.environment.hygiene">
              <el-radio id="environment-hygiene-2" :label="2">
                <label for="environment-hygiene-2">良好</label>
              </el-radio>
              <el-radio id="environment-hygiene-1" :label="1">
                <label for="environment-hygiene-1">一般</label>
              </el-radio>
              <el-radio id="environment-hygiene-0" :label="0">
                <label for="environment-hygiene-0">差</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="environment.accessibility">
            <template slot="label">
              <label>无障碍设施</label>
            </template>
            <el-radio-group v-model="surveyForm.environment.accessibility">
              <el-radio id="environment-accessibility-2" :label="2">
                <label for="environment-accessibility-2">完善</label>
              </el-radio>
              <el-radio id="environment-accessibility-1" :label="1">
                <label for="environment-accessibility-1">部分具备</label>
              </el-radio>
              <el-radio id="environment-accessibility-0" :label="0">
                <label for="environment-accessibility-0">缺乏</label>
              </el-radio>
            </el-radio-group>
          </el-form-item>
        </div>

        <!-- 导航按钮 -->
        <div class="button-group">
          <el-button 
            v-if="activeStep > 0" 
            @click="prevStep">上一步</el-button>
          <el-button 
            type="primary" 
            @click="handleSubmit"
            :loading="loading">
            {{ activeStep < 3 ? '下一步' : '提交' }}
          </el-button>
        </div>
      </el-form>
      </el-card>
    </div>
</template>

<script>
import { submitSurvey, trackVisitor } from '@/api/survey'

export default {
  name: 'Survey',
  data() {
    return {
      activeStep: 0,
      loading: false,
      surveyForm: {
        // 日常生活照护问题
        daily: {
          eating: null,
          dressing: null,
          toileting: null,
          bathing: null,
          indoor: null,
          outdoor: null
        },
        
        // 精神行为问题
        mental: {
          memory: null,
          emotion: null,
          sleep: null,
          communication: null,
          behavior: null,
          cognition: null
        },
        
        // 安全风险问题
        safety: {
          falling: null,
          wandering: null,
          medication: null,
          selfHarm: null,
          accident: null,
          emergency: null
        },
        
        // 居住环境评估
        environment: {
          layout: null,
          lighting: null,
          ventilation: null,
          safety: null,
          hygiene: null,
          accessibility: null
        }
      },
      rules: {
        // 日常生活照护问题验证规则
        'daily.eating': [{ required: true, type: 'number', message: '请评估进食能力', trigger: 'change' }],
        'daily.dressing': [{ required: true, type: 'number', message: '请评估穿衣能力', trigger: 'change' }],
        'daily.toileting': [{ required: true, type: 'number', message: '请评估如厕能力', trigger: 'change' }],
        'daily.bathing': [{ required: true, type: 'number', message: '请评估洗澡能力', trigger: 'change' }],
        'daily.indoor': [{ required: true, type: 'number', message: '请评估室内活动能力', trigger: 'change' }],
        'daily.outdoor': [{ required: true, type: 'number', message: '请评估户外活动能力', trigger: 'change' }],
        
        // 精神行为问题验证规则
        'mental.memory': [{ required: true, type: 'number', message: '请评估记忆力', trigger: 'change' }],
        'mental.emotion': [{ required: true, type: 'number', message: '请评估情绪状态', trigger: 'change' }],
        'mental.sleep': [{ required: true, type: 'number', message: '请评估睡眠质量', trigger: 'change' }],
        'mental.communication': [{ required: true, type: 'number', message: '请评估沟通能力', trigger: 'change' }],
        'mental.behavior': [{ required: true, type: 'number', message: '请评估行为异常', trigger: 'change' }],
        'mental.cognition': [{ required: true, type: 'number', message: '请评估认知能力', trigger: 'change' }],
        
        // 安全风险问题验证规则
        'safety.falling': [{ required: true, type: 'number', message: '请评估跌倒风险', trigger: 'change' }],
        'safety.wandering': [{ required: true, type: 'number', message: '请评估走失风险', trigger: 'change' }],
        'safety.medication': [{ required: true, type: 'number', message: '请评估用药安全', trigger: 'change' }],
        'safety.selfHarm': [{ required: true, type: 'number', message: '请评估自伤风险', trigger: 'change' }],
        'safety.accident': [{ required: true, type: 'number', message: '请评估意外风险', trigger: 'change' }],
        'safety.emergency': [{ required: true, type: 'number', message: '请评估紧急求助能力', trigger: 'change' }],
        
        // 居住环境评估验证规则
        'environment.layout': [{ required: true, type: 'number', message: '请评估室内布局', trigger: 'change' }],
        'environment.lighting': [{ required: true, type: 'number', message: '请评估照明条件', trigger: 'change' }],
        'environment.ventilation': [{ required: true, type: 'number', message: '请评估通风条件', trigger: 'change' }],
        'environment.safety': [{ required: true, type: 'number', message: '请评估安全设施', trigger: 'change' }],
        'environment.hygiene': [{ required: true, type: 'number', message: '请评估卫生条件', trigger: 'change' }],
        'environment.accessibility': [{ required: true, type: 'number', message: '请评估无障碍设施', trigger: 'change' }]
      },
      fieldNames: {
        daily: {
          eating: '进食能力',
          dressing: '穿衣能力',
          toileting: '如厕能力',
          bathing: '洗澡能力',
          indoor: '室内活动',
          outdoor: '户外活动'
        },
        mental: {
          memory: '记忆力',
          emotion: '情绪状态',
          sleep: '睡眠情况',
          communication: '沟通能力',
          behavior: '行为状态',
          cognition: '认知能力'
        },
        safety: {
          falling: '跌倒风险',
          wandering: '走失风险',
          medication: '用药安全',
          selfHarm: '自伤风险',
          accident: '意外风险',
          emergency: '紧急求助'
        },
        environment: {
          layout: '室内布局',
          lighting: '照明条件',
          ventilation: '通风条件',
          safety: '安全设施',
          hygiene: '卫生条件',
          accessibility: '无障碍设施'
        }
      }
    }
  },
  methods: {
    async nextStep() {
      try {
        // 验证当前步骤的所有字段
        const currentSection = ['daily', 'mental', 'safety', 'environment'][this.activeStep]
        const fields = this.getFieldsByStep(this.activeStep)
        
        // 使用 Element UI 的表单验证
        const valid = await this.$refs.surveyForm.validateField(fields)
        
        // 如果验证通过，进入下一步
      if (this.activeStep < 3) {
        this.activeStep++
          console.log('当前步骤:', this.activeStep)
        } else {
          // 如果是最后一步，提交表单
          await this.submitForm('surveyForm')
        }
      } catch (error) {
        // 使用 Element UI 的表单验证错误提示
        this.$message({
          message: `请完成${this.getSectionTitle(this.activeStep)}的所有评估项`,
          type: 'warning',
          duration: 3000,
          showClose: true
        })
      }
    },

    prevStep() {
      if (this.activeStep > 0) {
        this.activeStep--
        console.log('当前步骤:', this.activeStep)
      }
    },

    // 修改提交按钮的处理方法
    handleSubmit() {
      if (this.activeStep < 3) {
        this.nextStep()
      } else {
        this.$refs.surveyForm.validate(async (valid) => {
          if (valid) {
            try {
              this.loading = true
              const formData = {
                visitor_id: parseInt(localStorage.getItem('visitor_id')),
                daily: this.getFormSection('daily'),
                mental: this.getFormSection('mental'),
                safety: this.getFormSection('safety'),
                environment: this.getFormSection('environment')
              }
              
              // 添加调试日志
              console.log('准备提交的表单数据:', {
                visitor_id: formData.visitor_id,
                daily: formData.daily,
                mental: formData.mental,
                safety: formData.safety,
                environment: formData.environment
              })
              
              const response = await submitSurvey(formData)
              console.log('服务器响应:', response)
              
              this.$message({
                message: '问卷提交成功！',
                type: 'success',
                duration: 2000,
                onClose: () => {
      this.$router.push('/')
                }
              })
            } catch (error) {
              console.error('提交失败:', error)
              const errorMessage = error.response?.data?.message || error.message || '提交失败，请重试'
              
              this.$message({
                message: errorMessage,
                type: 'error',
                duration: 5000,
                showClose: true,
                dangerouslyUseHTMLString: true
              })
            } finally {
              this.loading = false
            }
          }
        })
      }
    },

    getFieldsByStep(step) {
      const fieldMap = {
        0: ['daily.eating', 'daily.dressing', 'daily.toileting', 'daily.bathing', 'daily.indoor', 'daily.outdoor'],
        1: ['mental.memory', 'mental.emotion', 'mental.sleep', 'mental.communication', 'mental.behavior', 'mental.cognition'],
        2: ['safety.falling', 'safety.wandering', 'safety.medication', 'safety.selfHarm', 'safety.accident', 'safety.emergency'],
        3: ['environment.layout', 'environment.lighting', 'environment.ventilation', 'environment.safety', 'environment.hygiene', 'environment.accessibility']
      }
      console.log('验证字段:', fieldMap[step])
      return fieldMap[step]
    },

    // 获取表单某个部分的数据
    getFormSection(section) {
      const result = {}
      for (const key in this.surveyForm[section]) {
        const value = this.surveyForm[section][key]
        // 直接使用原始值，不做转换
        result[key] = parseInt(value)
      }
      return result
    },

    // 在提交方法中添加日志
    async submitForm(formName) {
      try {
        console.log('开始提交表单...')
        const valid = await this.$refs[formName].validate()
        if (!valid) {
          throw new Error('表单验证失败')
        }

        this.loading = true
        const visitor_id = localStorage.getItem('visitor_id')
        console.log('访客ID:', visitor_id)
        
        const formData = {
          visitor_id: parseInt(visitor_id),
          daily: this.getFormSection('daily'),
          mental: this.getFormSection('mental'),
          safety: this.getFormSection('safety'),
          environment: this.getFormSection('environment')
        }
        
        console.log('提交的表单数据:', formData)
        const response = await submitSurvey(formData)
        console.log('服务器响应:', response)
        
        // ... 其他代码 ...
      } catch (error) {
        console.error('提交失败:', error)
        // ... 错误处理 ...
      }
    }
  }
}
</script>

<style scoped>
.survey {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
}
.survey-card {
  margin-bottom: 20px;
}
.survey-steps {
  margin: 20px 0 40px;
}
h3 {
  margin: 20px 0;
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
  color: #409EFF;
}
.el-form-item {
  margin-bottom: 22px;
}
</style> 
