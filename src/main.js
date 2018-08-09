import Vue from 'vue'
import App from '@/App.vue'

import $backend from '@/backend'
Vue.config.productionTip = false
Vue.prototype.$backend = $backend

const vue = new Vue({
  render: h => h(App)
})

vue.$mount('#app')
