<template>
  <el-form :model="form" ref="form" label-position="left">
    <el-form :inline="true">
      <el-form-item
        label="Stock Code"
        prop="stock_code"
        label-width="100px"
        class="item_name"
      >
        <el-input
          v-model="form.stock_code"
          :disabled="true"
          style="width: 50%"
        ></el-input>
      </el-form-item>
      <el-form-item label="Stock Name" prop="stock_name" label-width="100px">
        <el-input
          v-model="form.stock_name"
          :disabled="true"
          style="width: 120%"
        ></el-input>
      </el-form-item>
    </el-form>
    <el-form :inline="true">
      <el-form-item
        label="Purchase Price"
        prop="purchase_price"
        label-width="120px"
      >
        <el-input v-model="form.purchase_price" style="width: 80%"></el-input>
      </el-form-item>
      <el-form-item
        label="Target Price"
        prop="target_price"
        label-width="120px"
      >
        <el-input v-model="form.target_price" style="width: 80%"></el-input>
      </el-form-item>
    </el-form>

    <el-form :inline="true">
      <el-form-item
        label="Expect Return Rate"
        prop="expect_return_rate"
        label-width="150px"
      >
        <el-input
          v-model="form.expect_return_rate"
          style="width: 80%"
        ></el-input>
      </el-form-item>
      <el-form-item
        label="Purchase Date"
        prop="purchase_date"
        label-width="120px"
      >
        <el-date-picker
          v-model="form.purchase_date"
          style="width: 90%"
        ></el-date-picker>
      </el-form-item>
    </el-form>

    <el-form :inline="true">
      <el-form-item label="Close Price" prop="close_price" label-width="150px">
        <el-input
          v-model="form.close_price"
          :disabled="true"
          style="width: 80%"
        ></el-input>
      </el-form-item>
      <el-form-item label="Close Date" prop="close_date" label-width="120px">
        <el-date-picker
          v-model="form.close_date"
          :disabled="true"
          style="width: 90%"
        ></el-date-picker>
      </el-form-item>
    </el-form>

    <el-form :inline="true">
      <el-form-item label="Horizon" prop="horizon" label-width="150px">
        <el-input v-model="form.horizon" disabled></el-input>
      </el-form-item>
      <el-form-item
        label="Left Horizon"
        prop="left_horizon"
        label-width="120px"
      >
        <el-input v-model="form.left_horizon" disabled></el-input>
      </el-form-item>
    </el-form>

    <el-form :inline="true">
      <el-form-item
        label="Opportunity Cost"
        prop="opportunity_cost"
        label-width="150px"
      >
        <el-input v-model="form.opportunity_cost" :disabled="true"></el-input>
      </el-form-item>
      <el-form-item
        label="Short Return"
        prop="short_return"
        label-width="120px"
      >
        <el-input v-model="form.short_return" :disabled="true"></el-input>
      </el-form-item>
      <el-form-item label="Long Return" prop="long_return" label-width="120px">
        <el-input v-model="form.long_return" :disabled="true"></el-input>
      </el-form-item>
    </el-form>
    <el-form-item>
      <el-button type="primary" @click="Save">Save</el-button>
    </el-form-item>
  </el-form>
</template>


<script>
import axios from "axios";
// import {getStore} from "@/config/utils";
export default {
  data() {
    return {
      form: {},
    };
  },
  created() {
    let user_id = this.$route.query.user_id,
      stock_code = this.$route.query.stock_code;
    axios
      .post("/profile/stock_detail/", {
        s_code: stock_code,
        id: user_id,
      })
      .then((res) => {
        console.log(res);
        this.form = res.data;
        this.form.horizon = this.form.horizon.toFixed(2);
        this.form.left_horizon = this.form.left_horizon.toFixed(2);
        this.form.close_price = this.form.close_price.toFixed(3);
      });
  },

  methods: {
    Save() {
      axios
        .post("/profile/set_stock/", {
          id: this.$route.query.user_id,
          s_code: this.$route.query.stock_code,
          purchase_date: this.form.purchase_date,
          purchase_price: this.form.purchase_price,
          target_price: this.form.target_price,
          expect_return_rate: this.form.expect_return_rate,
        })
        .then((res) => {
          if (res.data == "Setting Stock Succeeded!") {
            this.$message({
              message: "The Stock has been reset!",
              type: "success",
            });
            this.$router.push("/home/stocktrack");
          } else {
            this.$message({
              message: "something went wrong...",
              type: "error",
            });
          }
        })
        .catch((err) => {
          // console.error(err);
          this.$message({
            message: "something went wrong...",
            type: "error",
          });
        });
    },
  },
};
</script>

