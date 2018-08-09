<template>
  <div class="hello">

    <p>Subject</p>
    <input type="text" placeholder="Hello" v-model="subject">
    <p>Message</p>
    <input type="text" placeholder="From the other side" v-model="msgBody">
    <br><br>
    <input type="submit" value="Add" @click="postMessage" :disabled="!subject || !msgBody">

    <hr/>
    <h3>Messages</h3>
    <p v-if="messages.length ===0">No Messages</p>
    <div class="msg" v-for="(msg, index) in messages" :key="index">
        <p class="msg-index">[{{index}}]</p>
        <p class="msg-subject" v-html="msg.subject"></p>
        <p class="msg-body" v-html="msg.body"></p>
        <input type="submit" @click="deleteMsg(msg.pk)" value="Delete" />
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      subject: "",
      msgBody: "",
      messages: []
    };
  },
  mounted() {
    this.fetchMessages();
  },
  methods: {
    fetchMessages() {
      this.$backend.$fetchMessages().then(responseData => {
        this.messages = responseData;
      });
    },
    postMessage() {
      const payload = { subject: this.subject, body: this.msgBody };
      this.$backend.$postMessage(payload).then(() => {
        this.fetchMessages();
      });
    },
    deleteMsg(msgID) {
        this.$backend.$deleteMessage(msgID).then(() => {
            this.fetchMessages();
        });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
hr {
  max-width: 65%;
}

.msg {
  margin: 0 auto;
  max-width: 30%;
  text-align: left;
  border-bottom: 1px solid #ccc;
  padding: 1rem;
}

.msg-index {
  color: #ccc;
  font-size: 0.8rem;
  /* margin-bottom: 0; */
}

.msg-subject {
  /* margin-top: 0px; */
  /* margin-bottom: 5px; */
}
.msg-body {
  /* margin-top: 0px; */
  /* margin-bottom: 1rem; */
}

</style>
