<!-- eslint-disable no-trailing-spaces -->
<template>
  <page-background>
    <div class="records">
      <!-- 如果没有记录，显示问卷 -->
      <div v-if="!hasRecord">
        <el-steps :active="activeStep" finish-status="success" align-center>
          <el-step title="患者信息"></el-step>
          <el-step title="照护者信息"></el-step>
          <el-step title="完成"></el-step>
        </el-steps>

        <div class="form-container">
          <!-- 患者信息表单 -->
          <el-form
            v-if="activeStep === 0"
            :model="patientForm"
            :rules="patientRules"
            ref="patientForm"
            label-width="120px">
            <h2>患者基本信息</h2>
            
            <el-form-item label="性别" prop="gender">
              <el-radio-group v-model="patientForm.gender">
                <el-radio label="male">男</el-radio>
                <el-radio label="female">女</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item label="年龄" prop="age">
              <el-input-number v-model="patientForm.age" :min="1" :max="120"></el-input-number>
            </el-form-item>

            <el-form-item label="教育程度" prop="education">
              <el-select v-model="patientForm.education" placeholder="请选择教育程度">
                <el-option label="小学及以下" value="primary"></el-option>
                <el-option label="初中" value="junior"></el-option>
                <el-option label="高中/中专" value="high"></el-option>
                <el-option label="大专/本科" value="college"></el-option>
                <el-option label="研究生及以上" value="graduate"></el-option>
              </el-select>
            </el-form-item>

            <el-form-item label="疾病类型" prop="diseaseType">
              <el-select v-model="patientForm.diseaseType" placeholder="请选择疾病类型">
                <el-option label="阿尔茨海默病" value="alzheimer"></el-option>
                <el-option label="血管性痴呆" value="vascular"></el-option>
                <el-option label="路易体痴呆" value="lewy"></el-option>
                <el-option label="额颞叶痴呆" value="frontotemporal"></el-option>
                <el-option label="其他类型痴呆" value="other"></el-option>
              </el-select>
            </el-form-item>

            <el-form-item label="病情严重程度" prop="severity">
              <el-select v-model="patientForm.severity" placeholder="请选择严重程度">
                <el-option label="轻度" value="mild"></el-option>
                <el-option label="中度" value="moderate"></el-option>
                <el-option label="重度" value="severe"></el-option>
              </el-select>
            </el-form-item>

            <el-form-item label="确诊前兴趣爱好" prop="hobbies">
              <el-checkbox-group v-model="patientForm.hobbies">
                <el-checkbox label="reading">阅读</el-checkbox>
                <el-checkbox label="music">音乐</el-checkbox>
                <el-checkbox label="sports">运动</el-checkbox>
                <el-checkbox label="gardening">园艺</el-checkbox>
                <el-checkbox label="cooking">烹饪</el-checkbox>
                <el-checkbox label="art">绘画/手工</el-checkbox>
                <el-checkbox label="social">社交活动</el-checkbox>
                <el-checkbox label="travel">旅游</el-checkbox>
              </el-checkbox-group>
            </el-form-item>

            <el-form-item label="行走能力" prop="mobility">
              <el-select v-model="patientForm.mobility" placeholder="请选择行走能力">
                <el-option label="完全自主行走" value="independent"></el-option>
                <el-option label="需要辅助工具" value="assisted"></el-option>
                <el-option label="需要他人搀扶" value="dependent"></el-option>
                <el-option label="无法行走" value="unable"></el-option>
              </el-select>
            </el-form-item>

            <el-form-item>
              <el-button type="primary" @click="nextStep('patientForm')">下一步</el-button>
            </el-form-item>
          </el-form>

          <!-- 照护者信息表单 -->
          <el-form
            v-if="activeStep === 1"
            :model="caregiverForm"
            :rules="caregiverRules"
            ref="caregiverForm"
            label-width="120px">
            <h2>照护者基本信息</h2>

            <el-form-item label="性别" prop="gender">
              <el-radio-group v-model="caregiverForm.gender">
                <el-radio label="male">男</el-radio>
                <el-radio label="female">女</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item label="年龄" prop="age">
              <el-input-number v-model="caregiverForm.age" :min="16" :max="120"></el-input-number>
            </el-form-item>

            <el-form-item label="教育程度" prop="education">
              <el-select v-model="caregiverForm.education" placeholder="请选择教育程度">
                <el-option label="小学及以下" value="primary"></el-option>
                <el-option label="初中" value="junior"></el-option>
                <el-option label="高中/中专" value="high"></el-option>
                <el-option label="大专/本科" value="college"></el-option>
                <el-option label="研究生及以上" value="graduate"></el-option>
              </el-select>
            </el-form-item>

            <el-form-item label="照护年限" prop="careYears">
              <el-input-number v-model="caregiverForm.careYears" :min="0" :max="50" :step="0.5"></el-input-number>
            </el-form-item>

            <el-form-item label="与患者关系" prop="relationship">
              <el-select v-model="caregiverForm.relationship" placeholder="请选择与患者的关系">
                <el-option label="配偶" value="spouse"></el-option>
                <el-option label="子女" value="child"></el-option>
                <el-option label="父母" value="parent"></el-option>
                <el-option label="其他亲属" value="relative"></el-option>
                <el-option label="专业护工" value="professional"></el-option>
              </el-select>
            </el-form-item>

            <el-form-item label="是否同住" prop="livingTogether">
              <el-radio-group v-model="caregiverForm.livingTogether">
                <el-radio :label="true">是</el-radio>
                <el-radio :label="false">否</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item>
              <el-button @click="activeStep--">上一步</el-button>
              <el-button type="primary" @click="submitForm('caregiverForm')">提交</el-button>
            </el-form-item>
          </el-form>

          <!-- 完成页面 -->
          <div v-if="activeStep === 2" class="completion-message">
            <i class="el-icon-success"></i>
            <h2>信息提交成功！</h2>
            <p>感谢您填写相关信息，这将帮助我们为您提供更好的服务。</p>
            <el-button type="primary" @click="viewRecords">查看记录</el-button>
          </div>
        </div>
      </div>

      <!-- 如果有记录，显示记录列表 -->
      <div v-else class="records-view">
        <div class="info-section">
          <h2>基本信息记录</h2>
          
          <!-- 基本信息表格 -->
          <el-table :data="[patientForm]" style="margin-bottom: 20px">
            <el-table-column label="患者信息" align="center">
              <el-table-column prop="gender" label="性别" :formatter="formatGender"></el-table-column>
              <el-table-column prop="age" label="年龄"></el-table-column>
              <el-table-column prop="education" label="教育程度" :formatter="formatEducation"></el-table-column>
              <el-table-column prop="diseaseType" label="疾病类型" :formatter="formatDisease"></el-table-column>
              <el-table-column prop="severity" label="严重程度" :formatter="formatSeverity"></el-table-column>
              <el-table-column prop="mobility" label="行走能力" :formatter="formatMobility"></el-table-column>
              <el-table-column prop="hobbies" label="兴趣爱好" :formatter="formatHobbies"></el-table-column>
            </el-table-column>
          </el-table>

          <el-table :data="[caregiverForm]" style="margin-bottom: 20px">
            <el-table-column label="照护者信息" align="center">
              <el-table-column prop="gender" label="性别" :formatter="formatGender"></el-table-column>
              <el-table-column prop="age" label="年龄"></el-table-column>
              <el-table-column prop="education" label="教育程度" :formatter="formatEducation"></el-table-column>
              <el-table-column prop="careYears" label="照护年限"></el-table-column>
              <el-table-column prop="relationship" label="与患者关系" :formatter="formatRelationship"></el-table-column>
              <el-table-column prop="livingTogether" label="是否同住" :formatter="formatLivingTogether"></el-table-column>
            </el-table-column>
          </el-table>

          <!-- 编辑按钮移到这里 -->
          <div class="button-group">
            <el-button type="primary" @click="editInfo">编辑信息</el-button>
          </div>
        </div>

        <!-- 历史照护方案记录部分 -->
        <div class="care-plan-section">
          <h2>历史照护方案记录</h2>
          <el-table :data="carePlans" style="margin-bottom: 20px">
            <el-table-column prop="createTime" label="创建时间" :formatter="formatTime"></el-table-column>
            <el-table-column prop="status" label="状态" :formatter="formatStatus"></el-table-column>
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-button 
                  type="text" 
                  @click="viewPlanDetail(scope.row)"
                  :disabled="scope.row.status === 'pending'">
                  查看详情
                </el-button>
                <el-button 
                  v-if="scope.row.status === 'pending'" 
                  type="text" 
                  disabled>
                  专家评估中，预计明日上午8:30完成
                </el-button>
              </template>
            </el-table-column>
          </el-table>

          <!-- 添加新照护方案按钮 -->
          <div class="button-group">
            <el-button type="primary" @click="createNewPlan">新增照护方案</el-button>
          </div>
        </div>
      </div>

      <!-- 编辑对话框 -->
      <el-dialog :title="dialogTitle" :visible.sync="dialogVisible" width="50%">
        <el-form :model="editingForm" :rules="editingRules" ref="editForm" label-width="120px">
          <!-- 动态渲染表单项 -->
          <!-- eslint-disable-next-line vue/no-unused-vars -->
          <template v-for="(field, index) in editingFields">
            <el-form-item :key="field.prop" :label="field.label" :prop="field.prop">
              <!-- 根据字段类型渲染不同的表单控件 -->
              <el-radio-group v-if="field.type === 'radio'" v-model="editingForm[field.prop]">
                <el-radio v-for="opt in field.options" :key="opt.value" :label="opt.value">
                  {{ opt.label }}
                </el-radio>
              </el-radio-group>
              
              <el-input-number v-else-if="field.type === 'number'"
                v-model="editingForm[field.prop]"
                :min="field.min"
                :max="field.max"
                :step="field.step || 1">
              </el-input-number>
              
              <el-select v-else-if="field.type === 'select'"
                v-model="editingForm[field.prop]"
                :placeholder="field.placeholder">
                <el-option v-for="opt in field.options"
                  :key="opt.value"
                  :label="opt.label"
                  :value="opt.value">
                </el-option>
              </el-select>
              
              <el-checkbox-group v-else-if="field.type === 'checkbox'"
                v-model="editingForm[field.prop]">
                <el-checkbox v-for="opt in field.options"
                  :key="opt.value"
                  :label="opt.value">
                  {{ opt.label }}
                </el-checkbox>
              </el-checkbox-group>
            </el-form-item>
          </template>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="saveEdit">确定</el-button>
        </span>
      </el-dialog>
    </div>
  </page-background>
</template>

<script>
import PageBackground from '@/components/PageBackground.vue'

export default {
  name: 'Records',
  components: {
    PageBackground
  },
  data () {
    return {
      activeStep: 0,
      patientForm: {
        gender: '',
        age: null,
        education: '',
        diseaseType: '',
        severity: '',
        hobbies: [],
        mobility: ''
      },
      caregiverForm: {
        gender: '',
        age: null,
        education: '',
        careYears: null,
        relationship: '',
        livingTogether: null
      },
      patientRules: {
        gender: [{ required: true, message: '请选择性别', trigger: 'change' }],
        age: [{ required: true, message: '请输入年龄', trigger: 'change' }],
        education: [{ required: true, message: '请选择教育程度', trigger: 'change' }],
        diseaseType: [{ required: true, message: '请选择疾病类型', trigger: 'change' }],
        severity: [{ required: true, message: '请选择严重程度', trigger: 'change' }],
        hobbies: [{ type: 'array', required: true, message: '请至少选择一个兴趣爱好', trigger: 'change' }],
        mobility: [{ required: true, message: '请选择行走能力', trigger: 'change' }]
      },
      caregiverRules: {
        gender: [{ required: true, message: '请选择性别', trigger: 'change' }],
        age: [{ required: true, message: '请输入年龄', trigger: 'change' }],
        education: [{ required: true, message: '请选择教育程度', trigger: 'change' }],
        careYears: [{ required: true, message: '请输入照护年限', trigger: 'change' }],
        relationship: [{ required: true, message: '请选择与患者的关系', trigger: 'change' }],
        livingTogether: [{ required: true, message: '请选择是否同住', trigger: 'change' }]
      },
      hasRecord: false,
      dialogVisible: false,
      dialogTitle: '',
      editingForm: {},
      editingRules: {},
      editingFields: [],
      editingType: '', // 'patient' 或 'caregiver'
      showRecords: false,
      carePlans: [] // 存储历史照护方案
    }
  },
  created () {
    // 检查是否有记录
    this.checkExistingRecord()
  },
  methods: {
    nextStep (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.activeStep++
        } else {
          return false
        }
      })
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // 这里添加提交表单的逻辑
          console.log('Patient Form:', this.patientForm)
          console.log('Caregiver Form:', this.caregiverForm)
          this.activeStep++
        } else {
          return false
        }
      })
    },
    viewRecords () {
      this.showRecords = true
      this.hasRecord = true
      // 保存记录到本地存储
      this.saveToStorage()
      // 加载历史照护方案
      this.loadCarePlans()
    },
    checkExistingRecord () {
      // 这里检查本地存储或后端API是否有记录
      const savedRecord = localStorage.getItem('recordData')
      if (savedRecord) {
        const data = JSON.parse(savedRecord)
        this.patientForm = data.patient
        this.caregiverForm = data.caregiver
        this.hasRecord = true
      }
    },
    editPatientInfo () {
      this.editingType = 'patient'
      this.dialogTitle = '编辑患者信息'
      this.editingForm = { ...this.patientForm }
      this.editingRules = this.patientRules
      this.editingFields = [
        {
          type: 'radio',
          label: '性别',
          prop: 'gender',
          options: [
            { label: '男', value: 'male' },
            { label: '女', value: 'female' }
          ]
        },
        {
          type: 'number',
          label: '年龄',
          prop: 'age',
          min: 1,
          max: 120
        }
      ]
      this.dialogVisible = true
    },
    editCaregiverInfo () {
      this.editingType = 'caregiver'
      this.dialogTitle = '编辑照护者信息'
      this.editingForm = { ...this.caregiverForm }
      this.editingRules = this.caregiverRules
      this.editingFields = [
        // ... 照护者字段配置
      ]
      this.dialogVisible = true
    },
    saveEdit () {
      this.$refs.editForm.validate(valid => {
        if (valid) {
          // 更新患者信息
          this.patientForm = {
            gender: this.editingForm.gender,
            age: this.editingForm.age,
            education: this.editingForm.education,
            diseaseType: this.editingForm.diseaseType,
            severity: this.editingForm.severity,
            hobbies: this.editingForm.hobbies,
            mobility: this.editingForm.mobility
          }

          // 更新照护者信息
          this.caregiverForm = {
            gender: this.editingForm.caregiverGender,
            age: this.editingForm.caregiverAge,
            education: this.editingForm.caregiverEducation,
            careYears: this.editingForm.careYears,
            relationship: this.editingForm.relationship,
            livingTogether: this.editingForm.livingTogether
          }

          // 保存到本地存储
          this.saveToStorage()
          this.dialogVisible = false
          this.$message.success('保存成功')
        }
      })
    },
    editInfo () {
      this.dialogVisible = true
      this.dialogTitle = '编辑基本信息'
      // 设置编辑表单的初始值
      this.editingForm = {
        ...this.patientForm,
        caregiverGender: this.caregiverForm.gender,
        caregiverAge: this.caregiverForm.age,
        caregiverEducation: this.caregiverForm.education,
        careYears: this.caregiverForm.careYears,
        relationship: this.caregiverForm.relationship,
        livingTogether: this.caregiverForm.livingTogether
      }
      // 设置编辑字段配置
      this.editingFields = [
        // 患者信息字段
        {
          type: 'radio',
          label: '患者性别',
          prop: 'gender',
          options: [
            { label: '男', value: 'male' },
            { label: '女', value: 'female' }
          ]
        },
        {
          type: 'number',
          label: '患者年龄',
          prop: 'age',
          min: 1,
          max: 120
        },
        {
          type: 'select',
          label: '教育程度',
          prop: 'education',
          placeholder: '请选择教育程度',
          options: [
            { label: '小学及以下', value: 'primary' },
            { label: '初中', value: 'junior' },
            { label: '高中/中专', value: 'high' },
            { label: '大专/本科', value: 'college' },
            { label: '研究生及以上', value: 'graduate' }
          ]
        },
        {
          type: 'select',
          label: '疾病类型',
          prop: 'diseaseType',
          placeholder: '请选择疾病类型',
          options: [
            { label: '阿尔茨海默病', value: 'alzheimer' },
            { label: '血管性痴呆', value: 'vascular' },
            { label: '路易体痴呆', value: 'lewy' },
            { label: '额颞叶痴呆', value: 'frontotemporal' },
            { label: '其他类型痴呆', value: 'other' }
          ]
        },
        {
          type: 'select',
          label: '严重程度',
          prop: 'severity',
          placeholder: '请选择严重程度',
          options: [
            { label: '轻度', value: 'mild' },
            { label: '中度', value: 'moderate' },
            { label: '重度', value: 'severe' }
          ]
        },
        {
          type: 'checkbox',
          label: '兴趣爱好',
          prop: 'hobbies',
          options: [
            { label: '阅读', value: 'reading' },
            { label: '音乐', value: 'music' },
            { label: '运动', value: 'sports' },
            { label: '园艺', value: 'gardening' },
            { label: '烹饪', value: 'cooking' },
            { label: '绘画/手工', value: 'art' },
            { label: '社交活动', value: 'social' },
            { label: '旅游', value: 'travel' }
          ]
        },
        {
          type: 'select',
          label: '行走能力',
          prop: 'mobility',
          placeholder: '请选择行走能力',
          options: [
            { label: '完全自主行走', value: 'independent' },
            { label: '需要辅助工具', value: 'assisted' },
            { label: '需要他人搀扶', value: 'dependent' },
            { label: '无法行走', value: 'unable' }
          ]
        },
        // 照护者信息字段
        {
          type: 'radio',
          label: '照护者性别',
          prop: 'caregiverGender',
          options: [
            { label: '男', value: 'male' },
            { label: '女', value: 'female' }
          ]
        },
        {
          type: 'number',
          label: '照护者年龄',
          prop: 'caregiverAge',
          min: 16,
          max: 120
        },
        {
          type: 'select',
          label: '照护者教育程度',
          prop: 'caregiverEducation',
          placeholder: '请选择教育程度',
          options: [
            { label: '小学及以下', value: 'primary' },
            { label: '初中', value: 'junior' },
            { label: '高中/中专', value: 'high' },
            { label: '大专/本科', value: 'college' },
            { label: '研究生及以上', value: 'graduate' }
          ]
        },
        {
          type: 'number',
          label: '照护年限',
          prop: 'careYears',
          min: 0,
          max: 50,
          step: 0.5
        },
        {
          type: 'select',
          label: '与患者关系',
          prop: 'relationship',
          placeholder: '请选择与患者的关系',
          options: [
            { label: '配偶', value: 'spouse' },
            { label: '子女', value: 'child' },
            { label: '父母', value: 'parent' },
            { label: '其他亲属', value: 'relative' },
            { label: '专业护工', value: 'professional' }
          ]
        },
        {
          type: 'radio',
          label: '是否同住',
          prop: 'livingTogether',
          options: [
            { label: '是', value: true },
            { label: '否', value: false }
          ]
        }
      ]
    },
    saveToStorage () {
      const recordData = {
        patient: this.patientForm,
        caregiver: this.caregiverForm
      }
      localStorage.setItem('recordData', JSON.stringify(recordData))
    },
    getGenderText (value) {
      return value === 'male' ? '男' : '女'
    },
    getEducationText (value) {
      const map = {
        primary: '小学及以下',
        junior: '初中',
        high: '高中/中专',
        college: '大专/本科',
        graduate: '研究生及以上'
      }
      return map[value] || value
    },
    getDiseaseText (value) {
      const map = {
        alzheimer: '阿尔茨海默病',
        vascular: '血管性痴呆',
        lewy: '路易体痴呆',
        frontotemporal: '额颞叶痴呆',
        other: '其他类型痴呆'
      }
      return map[value] || value
    },
    getSeverityText (value) {
      const map = {
        mild: '轻度',
        moderate: '中度',
        severe: '重度'
      }
      return map[value] || value
    },
    getMobilityText (value) {
      const map = {
        independent: '完全自主行走',
        assisted: '需要辅助工具',
        dependent: '需要他人搀扶',
        unable: '无法行走'
      }
      return map[value] || value
    },
    getHobbiesText (value) {
      return value.join(', ')
    },
    getRelationshipText (value) {
      const map = {
        spouse: '配偶',
        child: '子女',
        parent: '父母',
        relative: '其他亲属',
        professional: '专业护工'
      }
      return map[value] || value
    },
    loadCarePlans () {
      // 从本地存储或后端加载历史照护方案
      const savedPlans = localStorage.getItem('carePlans')
      if (savedPlans) {
        this.carePlans = JSON.parse(savedPlans)
      }
    },
    viewPlanDetail (plan) {
      // 查看照护方案详情的逻辑
      this.$router.push({
        path: '/care-plan',
        query: { id: plan.id }
      })
    },
    // 表格格式化方法
    formatGender (row, column) {
      return this.getGenderText(row.gender)
    },
    formatEducation (row, column) {
      return this.getEducationText(row.education)
    },
    formatDisease (row, column) {
      return this.getDiseaseText(row.diseaseType)
    },
    formatSeverity (row, column) {
      return this.getSeverityText(row.severity)
    },
    formatMobility (row, column) {
      return this.getMobilityText(row.mobility)
    },
    formatHobbies (row, column) {
      return this.getHobbiesText(row.hobbies)
    },
    formatRelationship (row, column) {
      return this.getRelationshipText(row.relationship)
    },
    formatLivingTogether (row, column) {
      return row.livingTogether ? '是' : '否'
    },
    formatTime (row) {
      return new Date(row.createTime).toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
      })
    },
    formatStatus (row) {
      const statusMap = {
        pending: '评估中',
        completed: '已完成'
      }
      return statusMap[row.status] || row.status
    },
    createNewPlan () {
      // 创建新的照护方案记录
      const newPlan = {
        id: Date.now().toString(),
        createTime: new Date().toISOString(),
        status: 'pending'
      }

      // 添加到列表中
      this.carePlans.unshift(newPlan)

      // 保存到本地存储
      localStorage.setItem('carePlans', JSON.stringify(this.carePlans))

      // 显示提示信息
      this.$message({
        type: 'success',
        message: '已提交照护方案申请，专家正在评估中'
      })
    }
  }
}
</script>

<style scoped>
.records {
  min-height: 100vh;
}

.records-view {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0;
}

/* 卡片样式优化 */
.info-section,
.care-plan-section {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  padding: 28px;
  margin-bottom: 28px;
  transition: all 0.3s ease;
}

.info-section:hover,
.care-plan-section:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
}

/* 标题样式优化 */
h2 {
  font-size: 22px;
  color: #1a1a1a;
  margin: 0 0 24px 0;
  padding-bottom: 16px;
  border-bottom: 1px solid #ebeef5;
  font-weight: 600;
  position: relative;
  letter-spacing: 0.5px;
}

h2::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -1px;
  width: 80px;
  height: 3px;
  background: linear-gradient(90deg, #409EFF, #66b1ff);
  border-radius: 3px;
}

/* 表格样式优化 */
.el-table {
  margin-bottom: 28px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
}

.el-table th {
  background-color: #f5f7fa !important;
  color: #1a1a1a;
  font-weight: 600;
  padding: 16px 0;
}

.el-table td {
  padding: 16px 0;
  color: #2c3e50;
}

/* 按钮样式优化 */
.button-group {
  text-align: right;
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid #ebeef5;
}

.button-group .el-button {
  padding: 12px 28px;
  font-weight: 500;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.button-group .el-button--primary {
  background: linear-gradient(135deg, #409EFF, #66b1ff);
  border: none;
  box-shadow: 0 4px 12px rgba(64, 158, 255, 0.3);
}

.button-group .el-button--primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(64, 158, 255, 0.4);
}

/* 文本按钮样式优化 */
.el-button--text {
  padding: 0 16px;
  font-size: 14px;
  height: 32px;
  line-height: 32px;
  font-weight: 500;
  transition: all 0.3s ease;
}

.el-button--text:not([disabled]):hover {
  color: #409EFF;
  transform: translateY(-1px);
}

/* 步骤条样式优化 */
.el-steps {
  margin: 36px 0;
  padding: 28px;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.el-step__title {
  font-size: 16px;
  font-weight: 500;
}

.el-step__head.is-process {
  color: #409EFF;
  border-color: #409EFF;
}

/* 表单容器样式优化 */
.form-container {
  background: #fff;
  padding: 32px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

/* 表单项样式优化 */
.el-form-item__label {
  font-weight: 500;
  color: #1a1a1a;
}

.el-input__inner,
.el-select .el-input__inner {
  border-radius: 8px;
  padding: 0 16px;
  height: 40px;
  line-height: 40px;
  border-color: #dcdfe6;
  transition: all 0.3s ease;
}

.el-input__inner:hover,
.el-select .el-input__inner:hover {
  border-color: #409EFF;
}

.el-input__inner:focus,
.el-select .el-input__inner:focus {
  border-color: #409EFF;
  box-shadow: 0 0 0 2px rgba(64, 158, 255, 0.2);
}

/* 完成页面样式优化 */
.completion-message {
  text-align: center;
  padding: 48px 0;
}

.completion-message i {
  font-size: 80px;
  color: #67c23a;
  margin-bottom: 24px;
  text-shadow: 0 4px 12px rgba(103, 194, 58, 0.3);
}

.completion-message h2 {
  font-size: 24px;
  border: none;
  text-align: center;
  margin-bottom: 20px;
  color: #1a1a1a;
}

.completion-message p {
  font-size: 16px;
  color: #606266;
  margin-bottom: 32px;
  line-height: 1.6;
}

/* 编辑对话框样式优化 */
:deep(.el-dialog) {
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

:deep(.el-dialog__header) {
  padding: 24px 28px;
  border-bottom: 1px solid #ebeef5;
  background: #f5f7fa;
}

:deep(.el-dialog__title) {
  font-size: 18px;
  font-weight: 600;
  color: #1a1a1a;
}

:deep(.el-dialog__body) {
  padding: 28px;
}

:deep(.el-dialog__footer) {
  padding: 20px 28px;
  border-top: 1px solid #ebeef5;
  background: #f5f7fa;
}

/* 响应式布局优化 */
@media screen and (max-width: 768px) {
  .records {
    padding: 16px;
  }
  .info-section,
  .care-plan-section {
    padding: 20px;
    margin-bottom: 20px;
  }
  .form-container {
    padding: 20px;
  }
  .button-group {
    text-align: center;
  }
  .button-group .el-button {
    width: 100%;
    margin: 8px 0;
  }
  h2 {
    font-size: 20px;
    margin-bottom: 20px;
  }
  .completion-message {
    padding: 32px 0;
  }
  .completion-message i {
    font-size: 64px;
  }
  :deep(.el-dialog) {
    width: 90% !important;
    margin: 5vh auto !important;
  }
}
</style>
