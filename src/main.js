import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from '@/store'
import './registerServiceWorker'

Vue.config.productionTip = false

if ('-ms-scroll-limit' in document.documentElement.style && '-ms-ime-align' in document.documentElement.style) {
  window.addEventListener('hashchange', (event) => {
    const currentPath = window.location.hash.slice(1)
    if (router.path !== currentPath) {
      router.push(currentPath)
    }
  }, false)
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
