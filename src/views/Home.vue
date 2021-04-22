<template>
  <el-container class="home-container">
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
    </el-aside>
    <el-container>
      <el-header
        ><span>Portfolio Assistant</span>
        <el-button type="primary" @click="logout">log out</el-button>
      </el-header>
      <el-main>
        <StockTrack/>
      </el-main>
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
      name: getStore("user").name,
      imageUrl: getStore("user").imageUrl,
      email: getStore("user").email,
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
  background-color: #fff
  display: flex
  padding-left: 0
  align-items: center
  // color: #fff
  font-size: 24px
  font-weight: bold
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
  justify-content: space-between
  // border-radius: 4px

  > div
    display: flex
    align-items: center
  > span
    margin-left: 15px

.el-aside
  background-color: #409EFF
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)
  color: #fff
  // border-radius: 4px

.el-main
  background-color: #ECEEF1

.avatar
  padding: 10px
  text-align: center

.name
  text-align: center
  font-size: 16px
</style>