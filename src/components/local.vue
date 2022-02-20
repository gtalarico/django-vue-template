 <template>
    <div>
        <div v-for="(user, n) in users">
            <p>
                <span class="user">{{ user }}</span>
                <button @click="removeuser(n)">Remove</button>
            </p>
        </div>
        <p>
            <input v-model="newuser">
            <button @click="adduser()">Sign Up</button>
        </p>  
    </div>
</template>

<script>
    import { defineComponent } from '@vue/composition-api'
    import Vue from 'vue'

    export default defineComponent({
        setup() {
            const app = new Vue({
                data : {
                users: [],
                newuser: null
                },
                mounted() {
                    if (localStorage.getItem('users')) {
                    try {
                        this.users = JSON.parse(localStorage.getItem('users'));
                    } catch(e) {
                        localStorage.removeItem('users');
                    }
                    console.log(this.users)
                    }
                },
                methods: {
                    adduser() {
                        if (!this.newuser) {
                            return;
                        }
                        this.users.push(this.newuser);
                        this.newuser = '';
                        this.saveusers();
                    },
                    removeuser(x) {
                        this.users.splice(x, 1);
                        this.saveusers();
                    },
                    saveusers() {
                        const parsed = JSON.stringify(this.users);
                        localStorage.setItem('users', parsed);
                    }
                },
            })
        },
    })
</script>

