<template>
  <div>
    <HomeMenu />
    <div class="main-container">
      <div class="loginsuccess-container">
        <h2 class="heading">Login Success!</h2>
        <div>
          <div v-if="this.$store.state.loginUser.loginType == 'fb'">
            Facebook Access Token - {{this.$store.state.loginUser.fb.authResponse.accessToken}}
          </div>
          <div v-else-if="this.$store.state.loginUser.loginType == 'google'">
            Google Access Token - {{this.$store.state.loginUser.google.Zi.access_token}}
            <p>Welcome {{this.$store.state.loginUser.google.w3.ig}} !</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HomeMenu from '@/components/Menu'

export default {
  name: 'home',
  components: {
    HomeMenu
  }
}
</script>