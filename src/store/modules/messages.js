import messageService from '../../services/messageService'

const state = {
  messages: []
}

const getters = {
  messages: state => {
    return state.messages
  }
}

const mutations = {
  setMessages (state, messages) {
    state.messages = messages
  },
  addMessage (state, message) {
    state.messages.push(message)
  },
  deleteMessage (state, msgId) {
    state.messages = state.messages.filter(obj => obj.pk !== msgId)
  }
}

const actions = {
  getMessages ({ commit }) {
    messageService.fetchMessages()
      .then(messages => {
        commit('setMessages', messages)
      })
  },
  addMessage ({ commit }, message) {
    messageService.postMessage(message)
      .then(() => {
        commit('addMessage', message)
      })
  },
  deleteMessage ({ commit }, msgId) {
    messageService.deleteMessage(msgId)
    commit('deleteMessage', msgId)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
