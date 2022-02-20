import Vue from 'vue'
import Vuex from 'vuex'
import messages from './modules/messages'
import users from './modules/users'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    messages,
    users
  }
})