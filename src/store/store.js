import Vue from 'vue'
import Vuex from 'vuex'
import { setStore, getStore } from '@/config/utils'

Vue.use(Vuex)

const user = getStore('user')

export default new Vuex.Store({
  state: {
    loginUser: user
  },
  mutations: {
    setLoginUser(state, user) {
      state.loginUser = user
      setStore('user', user)
    }
  },
  actions: {

  },
  getters: {
    getLoginUserInfo(state) {
      return state.loginUser
    }
  }
})