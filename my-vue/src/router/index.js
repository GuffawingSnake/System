import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Records from '@/views/Records'
import Survey from '@/views/Survey.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/survey',
    name: 'Survey',
    component: Survey
  },
  {
    path: '/records',
    name: 'Records',
    component: Records
  },
  {
    path: '/expert-chat',
    name: 'ExpertInteraction',
    component: () => import('../views/ExpertInteraction.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
