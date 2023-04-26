import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import './index.css'

const app = createApp()

createApp(App).use(store).use(router, axios).mount('#app')
