import api from '@/services/api'

export default {
  fetchMessages() {
    return api.get(`http://127.0.0.1:8000/admin/api/message/`)
              .then(response => response.data)
    },
  postMessage(payload) {
    return api.post(`http://127.0.0.1:8000/admin/api/message/`, payload)
              .then(response => response.data)
  },
  deleteMessage(msgId) {
    return api.delete(`http://127.0.0.1:8000/admin/api/message/${msgId}`)
              .then(response => response.data)
  }
}