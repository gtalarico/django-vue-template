import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import My404 from './views/My404.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/messages',
      name: 'messages',
      // route level code-splitting
      // this generates a separate chunk (xxx.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "messages" */ './views/Messages.vue')
    },
    { path: '*', component: My404 }
  ]
})
