import api from '@/services/api'

export default {
  fetchMessages() {
    return api.get(`/post/`)
              .then(response => response.data)
    },
  postMessage(payload) {
    console.log(payload)
    return api.post(`/post/`, payload)
              .then(response => response.data)
  },
  deleteMessage(msgId) {
    return api.delete(`/post/${msgId}`)
              .then(response => response.data)
  }
}