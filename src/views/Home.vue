<template>
  <el-container class="home-container">
    <el-header
      ><span>Portfolio Assistant</span>
      <el-button @click="logout">log out</el-button>
    </el-header>
    <el-container>
      <el-aside width="200px">
        <el-row>
          <div class="avatar">
            <el-avatar :size="50" :src="imageUrl"></el-avatar>
          </div>
        </el-row>
        <el-row>
          <div class="name">
            <span fontsize="24px">{{ name }}</span>
          </div>
        </el-row>
        <el-row> </el-row>
      </el-aside>
      <el-main>Main</el-main>
    </el-container>
  </el-container>
</template>

<script>
// import HomeMenu from "@/components/Menu";
import { getStore, removeItem } from "@/config/utils";
export default {
  name: "home",
  components: {},
  methods: {
    logout() {
      removeItem("user");
      this.$router.push("/login");
    },
  },
  data() {
    return {
      userProfile: getStore("user").google.Rs,
      name: getStore("user").google.Rs.Se,
      imageUrl: getStore("user").google.Rs.WI,
      email: getStore("user").google.Rs.At,
    };
  },
  created() {},
};
</script>

<style lang="sass" scoped>
.home-container
  height: 100%
  width: 100%
  padding: 0px
  margin: 0px

.el-header
  background-color: #4d6d9a
  display: flex
  padding-left: 0
  align-items: center
  color: #fff
  font-size: 24px
  box-shadow: 10px 10px 5px gray
  justify-content: space-between

  > div
    display: flex
    align-items: center
  > span
    margin-left: 15px

.el-aside
  background-color: #d3e3fc
  box-shadow: 0px 0px 5px gray

.el-main
  background-color: #fff

.avatar
  padding: 10px
  text-align: center

.name
  text-align: center
  font-size: 16px
</style>