<template>
  <el-container class="home-container">
    <el-header>
      <span>Portfolio Assistant</span>
      <el-button @click="logout">log out</el-button>
    </el-header>
    <el-container>
      <el-aside width="200px">
        <el-row>
          <div class="avatar">
            <el-avatar :size="60" :src="imageUrl"></el-avatar>
          </div>
        </el-row>
        <el-row>
          <div class="name">
            <span fontsize="24px">{{ name }}</span>
          </div>
        </el-row>
      </el-aside>

      <el-main> <StockTrack/> </el-main>
    </el-container>
  </el-container>
</template>

<script>
// import HomeMenu from "@/components/Menu";
import { getStore, removeItem } from "@/config/utils";
import StockTrack from "@/components/StockTrack";
import axios from "axios";
export default {
  name: "home",
  components: {
    StockTrack
  },
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
  // created() {
  //   axios
  //     .get("/profile?id=" + 123)
  //     .then((res) => {
  //       console.log(res);
  //     })
  //     .catch((err) => {
  //       console.error(err);
  //     });
  // },
};
</script>

<style lang="sass" scoped>
.home-container
  height: 100%
  width: 100%
  padding: 0px
  margin: 0px

.el-header
  background-color: #252A2D
  display: flex
  padding-left: 0
  align-items: center
  color: #fff
  font-size: 24px
  font-weight: bold
  box-shadow: 10px 10px 5px #888888
  justify-content: space-between
  // border-radius: 4px

  > div
    display: flex
    align-items: center
  > span
    margin-left: 15px

.el-aside
  background-color: #fff
  // background-color: #409EFF

  // color: #fff
  // border-radius: 4px

.el-main
  background-color: #ECEEF1

.avatar
  padding: 10px
  padding-top: 30px
  text-align: center

.name
  padding-top: 10px
  text-align: center
  font-size: 18px
</style>