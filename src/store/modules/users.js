import userService from '../../services/userService'

const state = {
  users: []
}

const getters = {
    users: state => {
      return state.users
    }
}

const actions = {
    loginuser({ commit }, user) {
        userService.postUser(user)
        .then(() => {
          commit('loginuser', user)
        })
    },
    signupuser({ commit }, user) {
        userService.postUser(user)
        .then(() => {
          commit('signupuser', user)
        })
    }
}

const mutations = {
    loginuser(state, user) {
        state.users.push(user)
    },
    signupuser(state, user) {
        state.users.push(user)
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
  }