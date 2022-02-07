<template>
    <div>   
        <hr/>
        <div>
            <h3>Messages on Database</h3>
            <div class="msg">
                <p v-if="messages.length === 0">No Messages</p>
                <div class="msg" v-for="(msg, index) in messages" :key="index">
                    <p class="msg-subject" v-html="msg.title"></p>
                    <p class="msg-body" v-html="msg.text"></p>
                    <input type="submit" @click="editMessage(msg.pk)" value="edit" />
                    <input type="submit" @click="deleteMessage(msg.pk)" value="Delete" />
                </div>
            </div>
        </div>
        <div class="msg">
            <h3>Add Post</h3>
            <p>Title</p>
            <input type="text" placeholder="Hello" v-model="title" class="msg-index">
            <p>Text</p>
            <input type="text" placeholder="This is ...." v-model="text" class="msg-index">
            <br><br>
            <input 
                type="submit" 
                value="Add" 
                class="addbtn"
                @click="addMessage({ title, text })" 
                :disabled="!title || !text"
            >    
        </div>       
    </div>
</template>

<script>
  import { mapState, mapActions } from 'vuex'
  export default {
    name: "VueMessages",
        data() {
            return {
            title: "",
            text: "",
            };
        },
    computed: mapState({
      messages: state => state.messages.messages
    }),
    methods: mapActions('messages', [
      'addMessage',
      'deleteMessage',
      'editMessage'
    ]),
    created() {
      this.$store.dispatch('messages/getMessages')
    }
  };
</script>

<style scoped>
hr {
  max-width: 65%;
}

.addbtn {
    font-size: 1rem;
    border-radius: 20%;
    color: pink;
}

.msg {
  margin: 0 auto;
  max-width: 40%;
  text-align: left;
  border-top: 1px solid #ccc;
  padding: 1rem;
  font-size: 1rem;
}

.msg-index {
  color: rgb(121, 99, 99);
  /* margin-bottom: 0; */
}

img {
  width: 250px;
  padding-top: 50px;
  padding-bottom: 50px;
}

</style>