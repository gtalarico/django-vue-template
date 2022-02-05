<template>
    <div>
        <img src="@/assets/logo.png">
        <h3>Welcome to my site!</h3>
        <br>
        <div id="nav">
            <router-link :to="{ name: 'login' }">Log In</router-link> | 
            <router-link :to="{ name: 'signup' }">Sign Up</router-link>
        </div>
        <router-view/>
    </div>
</template>

<script>
    export default {
        name: 'VueDemo',
        props: {

        }
    }
</script>