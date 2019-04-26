<template>
  <div id="app">
    <div id="nav">
      <span id="logo">Django VueJs Template</span>
      <router-link :to="{ name: 'home' }">Vue</router-link> |
      <router-link :to="{ name: 'messages' }">Django Rest</router-link> |
      <a href="/my404">Test 404</a> |
      <a href="/admin/">Admin</a>
    </div>
    <router-view />
  </div>
</template>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#logo {
  position: absolute;
  left: 2rem;
  font-weight: bold;
}
#nav {
  padding: 30px;
  a {
    font-weight: normal;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
