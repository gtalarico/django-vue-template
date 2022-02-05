<template>
    <div>
        <h3>Sign Up</h3>
        <img src="@/assets/logo.png">
        <div class="msg">
            <p>User Name</p>
            <input type="text" placeholder="username" v-model="username" class="msg-index">
            <p>Password</p>
            <input type="password" placeholder="password" v-model="password" class="msg-index">
            <br><br>
            <input 
                type="submit" 
                value="Sign Up" 
                class="btn"
                @click="signup({ username: username, password: password })" 
                :disabled="!username || !password"
            >    
        </div>
        <br>
    </div>
</template>

<script>
  import { mapState, mapActions } from 'vuex'
  export default {
    name: "SignUp",
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
      'signup'
    ])
  };
</script>
