import './assets/main.css'
import axios from 'axios'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
const app = createApp(App)
axios.defaults.baseURL = 'http//127.0.0.1.5000'

const axiosInstance = axios.create({
    baseURL: 'https://milestone-ai.onrender.com/v1', 
  });

axiosInstance.interceptors.request.use(
    (config) => {
      const accessToken = localStorage.getItem('access_token');
      if (accessToken) {
        config.headers['Authorization'] = `Bearer ${accessToken}`;
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );
  
app.config.globalProperties.$axios = axiosInstance;
app.config.globalProperties.$user = null;

app.use(router)
app.mount('#app')
