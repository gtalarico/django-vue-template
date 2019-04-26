<template>
  <div class="home">
    <img src='@/assets/logo-django.png' style="width: 250px" />
    <p><a href="https://github.com/kevinqqnj/django-vue-template"
        target="_blank"
        rel="noopener">Source</a>
    </p>
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
