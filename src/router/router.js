import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import Login from '@/views/Login'
import SignUp from '@/views/SignUp'
import PageNotFound from '@/components/PageNotFound'
import Profile from '@/components/Profile'
import Setting from '@/components/Setting'
import StockTrack from '@/components/StockTrack'
import StockDetails from '@/components/StockDetails'
import AddStock from '@/components/AddStock'
Vue.use(Router)

let baseRoutes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
    children: [
      {
        path: 'stocktrack',
        name: 'StockTrack',
        component: StockTrack
      },
      {
        path: 'profile',
        name: 'Profile',
        component: Profile
      },
      {
        path: 'setting',
        name: 'Setting',
        component: Setting
      },
      {
        path: 'addstock',
        name: 'AddStock',
        component: AddStock
      },
      {
        path: 'stockdetails',
        name: 'StockDetails',
        component: StockDetails
      }
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '*',
    name: 'PageNotFound',
    component: PageNotFound
  }
]

const router = new Router({
  mode: 'history',
  linkExactActiveClass: 'active',
  base: process.env.BASE_URL,
  routes: baseRoutes
})

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/login', '/signup']
  const authRequired = !publicPages.includes(to.path)
  const loggedIn = localStorage.getItem('user')
  // const loggedIn = window.sessionStorage.getItem('token')
  if (!authRequired && loggedIn) {
    return next('/home')
  }
  else if (authRequired && !loggedIn) {
    return next('/login')
  }
  next()
})

export default router
