<template>
  <el-container class="home-container">
    <el-header><span>Portfolio Assistant</span></el-header>
    <el-container>
      <el-aside width="200px">Aside</el-aside>
      <el-main>Main</el-main>
    </el-container>
  </el-container>
</template>

<script>
// import HomeMenu from "@/components/Menu";
import { getStore } from "@/config/utils";
export default {
  name: "home",
  components: {},
  data() {
    return {
      userProfile: getStore("user").google.Rs,
      name: getStore("user").google.Rs.Se,
      imageUrl: getStore("user").google.Rs.WI,
      Email: getStore("user").google.Rs.At,
    };
  },
  created() {},
};
</script>

<style lang="sass" scoped>
.home-container
  height: 100%
  padding: 0px
  margin: 0px

.el-header
  background-color: #373d41
  display: flex
  padding-left: 0
  align-items: center
  color: #fff
  font-size: 24px

  > div
    display: flex
    align-items: center
  > span
    margin-left: 15px

.el-aside
  background-color: #333744

.el-main
  background-color: #eaedf1
</style>