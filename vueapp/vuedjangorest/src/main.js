import Vue from 'vue'
import App from './App.vue'
import router from './routes.js'
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'


Vue.config.productionTip = false

axios.defaults.baseURL = 'http://127.0.0.1:8000'

new Vue({
  router,
  axios,
  render: h => h(App),
}).$mount('#app')