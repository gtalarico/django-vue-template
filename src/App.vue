<template>
  <div id="app">
    <h1>Vue & Django</h1>
    <div id="nav">
      <router-link :to="{ name: 'home' }">Home</router-link> | 
      <router-link :to="{ name: 'messages' }">Messages</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  #nav {
    font-size: 20px;
    color: pink;
  }
</style>
