import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
// import Messages from '@/components/Messages'
import VueDemo from '@/components/VueDemo'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/messages',
      name: 'messages',
      component: () => import('@/components/Messages')
    },
    {
      path: '/vue',
      name: 'vue',
      component: VueDemo
    }
  ]
})
