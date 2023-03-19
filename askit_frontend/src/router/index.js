import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import QuestionView from '@/views/QuestionView.vue'
import AskView from '@/views/AskView.vue'
import AboutView from "@/views/AboutView.vue";
import ModuleView from "@/views/ModuleView.vue";
import PrivacyView from "@/views/PrivacyView.vue";
import LoginView from "@/views/LoginView.vue";
import SignUpView from "@/views/SignUpView.vue";

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
        name: 'ask',
        component: AskView
    },
    {
        path: '/module/:mod',
        name: 'module',
        component: ModuleView
    },
    {
        path: '/log-in',
        name: 'LogIn',
        component: LoginView
    },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUpView
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
