import Vue from 'vue'
import App from './App.vue'
import router from './router/router'
import store from './store/store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import './registerServiceWorker'
import '@/assets/css/style.css'
import GoogleAuth from '@/config/google_oAuth.js'
import axios from 'axios'
import locale from 'element-ui/lib/locale/lang/en'

const gauthOption = {
  clientId: '1052465622185-hl3qvsb6o5j432c95bb9fritksuuq4vh.apps.googleusercontent.com',
  scope: 'profile email',
  prompt: 'select_account'
}

Vue.use(ElementUI, { locale })
Vue.use(GoogleAuth, gauthOption)
Vue.prototype.$ajax = axios
Vue.config.productionTip = false
axios.defaults.baseURL = 'http://localhost:8000'
// axios.defaults.baseURL = 'https://portfoliotradingassistant.herokuapp.com'
// axios.defaults.baseURL = 'http://rap2api.taobao.org/app/mock/282070/'

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')