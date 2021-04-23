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
            <el-avatar
              :size="60"
              :src="imageUrl"
              @click.native="Profile"
            ></el-avatar>
          </div>
        </el-row>
        <el-row>
          <div class="name">
            <span>{{ name }}</span>
          </div>
        </el-row>
        <el-row>
          <el-menu default-active="1" class="el-menu-vertical-demo" router>
            <el-menu-item index="1" route="/home/stocktrack">
              <i class="el-icon-menu"></i>
              <span slot="title">My Stocks</span>
            </el-menu-item>
            <el-menu-item index="2" route="/home/profile">
              <i class="el-icon-document"></i>
              <span slot="title">Profile</span>
            </el-menu-item>
            <el-menu-item index="3" route="/home/setting">
              <i class="el-icon-setting"></i>
              <span slot="title">Settings</span>
            </el-menu-item>
            <el-menu-item index="4" route="/home/addstock">
              <i class="el-icon-plus"></i>
              <span slot="title">Add stocks</span>
            </el-menu-item>
          </el-menu>
        </el-row>
      </el-aside>
      <el-main>
        <div><router-view></router-view></div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
// import HomeMenu from "@/components/Menu";
import { getStore, removeItem } from "@/config/utils";
import axios from "axios";
export default {
  name: "home",
  methods: {
    logout() {
      removeItem("user");
      this.$router.push("/login");
    },
    Profile() {
      this.$router.push("/profile");
    },
  },
  data() {
    return {
      name: getStore("user").name,
      imageUrl: getStore("user").imageUrl,
      email: getStore("user").email,
      investment_horizon: 0,
      long_tax_rate: 0,
      short_tax_rate: 0,
      stocks: [],
    };
  },
  created() {
    axios
      .get("/profile?id=" + 123)
      .then((res) => {
        console.log(res);
        this.investment_horizon = res.data.investment_horizon;
        this.long_tax_rate = res.data.long_tax_rate;
        this.short_tax_rate = res.data.short_tax_rate;
      })
      .catch((err) => {
        console.error(err);
      });
  },
};
</script>

<style lang="sass" scoped>
.home-container
  height: 100%
  width: 100%
  padding: 0px
  margin: 0px

.el-header
  background-color: #1A89FA
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
  > div
    padding: 15px
    background-color: #fff
    height: 100%

.avatar
  padding: 10px
  padding-top: 30px
  text-align: center
  > el-avatar :hover
    box-shadow: 10px 10px 5px #888888

.name
  padding-top: 10px
  padding-bottom: 10px
  text-align: center
  font-size: 20px
  font-weight: bold

.aside-text
  padding-top: 50px
  padding-left: 15px
  font-size: 18px
  // font-weight: bold

.aside-render-text
  padding-top: 10px
  padding-left: 15px
  font-size: 18px
  font-family: Arial
  font-weight: bold
  color: #01B0FF
</style>