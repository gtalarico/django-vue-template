<template>
    <div>
        <h3>Log In</h3>
        <img src="@/assets/logo.png">
        <div class="msg">
            <p>User Name</p>
            <input type="text" placeholder="username" v-model="username" class="msg-index">
            <p>Password</p>
            <input type="password" placeholder="password" v-model="password" class="msg-index">
            <br><br>
            <input 
                type="submit" 
                value="Log In" 
                class="btn"
                @click="login({ username: username, password: password })" 
                :disabled="!username || !password"
            >    
        </div>
        <br>
    </div>
</template>

<script>
  import { mapState, mapActions } from 'vuex'
  export default {
    name: "LogIn",
        data() {
            return {
            username: "",
            password: "",
            };
        },
    computed: mapState({
      users: state => state.users.users
    }),
    methods: mapActions('users', [
      'login'
    ])
  };
</script>
