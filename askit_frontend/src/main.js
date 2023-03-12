import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import './index.css'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';

const app = createApp()
app.component('QuillEditor', QuillEditor)

// axios.defaults.baseURL= 'http://127.0.0.1:8000'

createApp(App).use(store).use(router,axios).mount('#app')
