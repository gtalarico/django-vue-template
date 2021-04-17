import Vue from 'vue'
import App from '@/App.vue'

import store from '@/store'
import router from '@/router'
import ElementUI from "element-ui";
import './plugins/element.js'
Vue.use(ElementUI);
Vue.config.productionTip = false

// Vue.use(VueRouter)

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')
