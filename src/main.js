import Vue from 'vue'
import App from '@/App.vue'
// import Vuetify from 'vuetify'
import Vuetify from 'vuetify/lib'
// import 'vuetify/src/stylus/app.styl'
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader

Vue.use(Vuetify)

import router from '@/router'
import $backend from '@/backend'
Vue.prototype.$backend = $backend
Vue.config.productionTip = false

// Vue.use(VueRouter)

const vue = new Vue({
  router,
  render: h => h(App)
})

vue.$mount('#app')
