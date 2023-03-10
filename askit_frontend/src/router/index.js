import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import QuestionView from '@/views/QuestionView.vue'
import ask_questionsVue from '@/views/ask_questions.vue'
import AboutView from "@/views/AboutView.vue";

const routes = [
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: AboutView
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
    path: '/module',
    name:'module',
    component: ModuleView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
