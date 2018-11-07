<template>
<div id="home">
    <v-navigation-drawer
      v-model="drawer"
      fixed
      app
    >
      <v-list dense>
        <v-list-tile>
          <v-list-tile-action href="/">
            <v-icon>home</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Home</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile>
          <v-list-tile-action href="/messages">
            <v-icon>contact_mail</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Messages</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar color="indigo" dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Home - {{username}}</v-toolbar-title>
      <v-btn @click="login">Login</v-btn>
    </v-toolbar>
    <v-content>
      <v-container fluid fill-height>
        <v-layout
          justify-center
          align-center
        >
          <v-flex text-xs-center>
          <router-link :to="{ name: 'messages' }">Django REST</router-link>
          </v-flex>
          <v-flex text-xs-center>
          <router-link :to="{ name: 'vue' }">Vue Demo</router-link>
          </v-flex>
          <v-flex text-xs-center>
            <v-tooltip left>
              <v-btn slot="activator" :href="source" icon large target="_blank">
                <v-icon large>code</v-icon>
              </v-btn>
              <span>Source</span>
            </v-tooltip>
            <v-tooltip right>
              <v-btn slot="activator" icon large href="https://codepen.io/johnjleider/pen/rJdVMq" target="_blank">
                <v-icon large>mdi-codepen</v-icon>
              </v-btn>
              <span>Codepen</span>
            </v-tooltip>
          </v-flex>
        </v-layout>
        <v-layout justify-center align-center>
          <v-flex text-xs-center>
          <v-btn @click="fetchMsgJWT">REST protected messages</v-btn>
          </v-flex>
          <v-flex text-xs-center>
          {{protectedMsg}}
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    </div>
</template>

<script>
  export default {
    name: "Home",
    data: () => ({
      drawer: null,
      username: 'Anonymous',
      token: '',
      protectedMsg: '',
    }),
    props: {
      source: String
    },
    methods: {
      login() {
        const payload = { username: 'test1', password: '12345678t' };
        this.$backend.$getJWTToken(payload).then(responseData => {
          // eslint-disable-next-line
          console.log(responseData)
          if (responseData.token) {
            this.username = 'Welcome'
            this.token = responseData.token
          } else alert('Invalid login!')
        }).catch(error => {
          // eslint-disable-next-line
          console.log(error)  // 400
          alert('Error!')
        });
      },
      fetchMsgJWT() {
        this.$backend.$fetchMsgJWT(this.token).then(responseData => {
          // eslint-disable-next-line
          console.log(responseData)
          if (responseData) {
            this.protectedMsg = responseData
          } else alert('Invalid login!')
        }).catch(error => {
          // eslint-disable-next-line
          console.log(error)  // 400
          alert('Error!')
        });
      },
    }
  }
</script>