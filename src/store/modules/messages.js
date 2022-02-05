import messageService from '../../services/messageService'

const state = {
  messages: []
}

const getters = {
  messages: state => {
    return state.messages
  }
}

const actions = {
  getMessages ({ commit }) {
    messageService.fetchMessages()
    .then(messages => {
      commit('setMessages', messages)
    })
  },
  addMessage({ commit }, message) {
    messageService.postMessage(message)
    .then(() => {
      commit('addMessage', message)
    })
  },
  deleteMessage( { commit }, msgId) {
    messageService.deleteMessage(msgId)
    commit('deleteMessage', msgId)
  },
  editMessage( { commit }, msgId){
    messageService.editMessage(msgId)
    commit('editMessage', msgId)
  }
}

const mutations = {
  setMessages (state, messages) {
    state.messages = messages
  },
  addMessage(state, message) {
    state.messages.push(message)
  },
  deleteMessage(state, msgId) {
    state.messages = state.messages.filter(obj => obj.pk !== msgId)
  },
  editMessage(state, msgId) {
      state.message.push(message)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}