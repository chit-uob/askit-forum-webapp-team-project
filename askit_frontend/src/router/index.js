import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import QuestionView from '@/views/QuestionView.vue'
import ask_questionsVue from '@/views/ask_questions.vue'
import AboutView from "@/views/AboutView.vue";
import ModuleView from "@/views/ModuleView.vue";
import PrivacyView from "@/views/PrivacyView.vue";

const routes = [
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/privacy',
    name: 'privacy',
    component: PrivacyView
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
    path: '/ask/:mod',
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
