import api from '@/services/api'

export default {
  postUsers(payload) {
    return api.post(`users/`, payload)
              .then(response => response.data)
  }
}