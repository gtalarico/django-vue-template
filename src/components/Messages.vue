<template>
  <div class="hello">
    <img src='@/assets/logo-django.png' style="width: 250px" />
    <p>The data below is added/removed from the Postgres Database using Django's ORM and Restframork.</p>
    <br/>
    <p>Subject</p>
    <input type="text" placeholder="Hello" v-model="subject">
    <p>Message</p>
    <input type="text" placeholder="From the other side" v-model="msgBody">
    <br><br>
    <input type="submit" value="Add" @click="postMessage" :disabled="!subject || !msgBody">

    <hr/>
    <h3>Messages on Database</h3>
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
  name: "Messages",
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
        this.msgBody = ""
        this.subject = ""
        this.fetchMessages();
      });
    },
    deleteMsg(msgId) {
        this.$backend.$deleteMessage(msgId).then(() => {
            this.messages = this.messages.filter(m => m.pk !== msgId)
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

img {
  width: 250px;
  padding-top: 50px;
  padding-bottom: 50px;
}

</style>
