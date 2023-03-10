import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import QuestionView from '../views/QuestionView.vue'
import ask_questionsVue from '@/views/ask_questions.vue'
import ModuleView from '../views/ModuleView.vue'

const routes = [
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/question/:id',
    name: 'question',
    component: QuestionView,
  },
      {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/ask',
    name:'ask',
    component: ask_questionsVue
  },
  {
    path: '/module/:mod',
    name:'module',
    component: ModuleView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
