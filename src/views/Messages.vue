<template>
  <div class="home">
    <img alt="Django logo"
        src="../assets/logo-django.png">
    <RestMessage />
  </div>
</template>

<script>
// @ is an alias to /src
import RestMessage from '@/components/RestMessage.vue'

export default {
  name: 'Messages',
  components: {
    RestMessage
  }
}
</script>
