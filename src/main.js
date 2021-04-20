import Vue from 'vue'
import App from './App.vue'
import router from './router/router'
import store from './store/store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import './registerServiceWorker'
import '@/assets/css/style.css'
import GoogleAuth from '@/config/google_oAuth.js'
const gauthOption = {
  clientId: '1052465622185-hl3qvsb6o5j432c95bb9fritksuuq4vh.apps.googleusercontent.com',
  scope: 'profile email',
  prompt: 'select_account'
}
Vue.use(ElementUI)
Vue.use(GoogleAuth, gauthOption)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')