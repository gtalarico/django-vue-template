<template>
  <div class="home">
    <img src='@/assets/logo-django.png' style="width: 250px" />
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
