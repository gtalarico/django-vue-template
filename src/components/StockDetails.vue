<template>

  <el-form :model="form" ref="form" label-position="left" >
    <el-form :inline="true">
      <el-form-item label="Stock Code" prop="stock_code" label-width="100px" class="item_name">
        <el-input  v-model="form.stock_code" :disabled="true" style="width: 50%"></el-input>
      </el-form-item>
      <el-form-item label="Stock Name" prop="stock_name" label-width="100px">
        <el-input v-model="form.stock_name" :disabled="true" style="width: 120%"></el-input>
      </el-form-item>
    </el-form>
    <el-form :inline="true">
      <el-form-item label="Purchase Price" prop="purchase_price" label-width="120px">
        <el-input  v-model="form.purchase_price" style="width: 80%"></el-input>
      </el-form-item>
      <el-form-item label="Target Price" prop="target_price" label-width="120px">
        <el-input  v-model="form.target_price" style="width: 80%"></el-input>
      </el-form-item>
    </el-form>

    <el-form :inline="true">
      <el-form-item label="Expect Return Rate" prop="expect_return_rate" label-width="150px">
        <el-input  v-model="form.expect_return_rate" style="width: 80%"></el-input>
      </el-form-item>
      <el-form-item label="Purchase Date" prop="purchase_date" label-width="120px">
          <el-date-picker  v-model="form.purchase_date" style="width: 90%;"></el-date-picker>
      </el-form-item>
    </el-form>

    <el-form :inline="true">
      <el-form-item label="Close Price" prop="close_price" label-width="150px">
        <el-input  v-model="form.close_price" :disabled="true" style="width: 80%"></el-input>
      </el-form-item>
      <el-form-item label="Close Date" prop="close_date" label-width="120px">
        <el-date-picker  v-model="form.close_date" :disabled="true" style="width: 90%;"></el-date-picker>
      </el-form-item>
    </el-form>

    <el-form :inline="true">
      <el-form-item label="Horizon" prop="horizon" label-width="150px">
        <el-input  v-model="form.horizon"></el-input>
      </el-form-item>
      <el-form-item label="Left Horizon" prop="left_horizon" label-width="120px">
        <el-input  v-model="form.left_horizon"></el-input>
      </el-form-item>
    </el-form>

    <el-form :inline="true">
      <el-form-item label="Opportunity Cost" prop="opportunity_cost" label-width="150px">
        <el-input  v-model="form.opportunity_cost" :disabled="true"></el-input>
      </el-form-item>
      <el-form-item label="Short Return" prop="short_return" label-width="120px">
        <el-input  v-model="form.short_return" :disabled="true"></el-input>
      </el-form-item>
      <el-form-item label="Long Return" prop="long_return" label-width="120px">
        <el-input  v-model="form.long_return" :disabled="true"></el-input>
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
      form:{
        stock_code: "NIO",
        stock_name: "NIO.Inc",
        purchase_price: 27.0,
        purchase_date: "2020-11-19",
        target_price: 40.0,
        expect_return_rate: 1.5, // means 150%
        close_price: 31.3,
        close_date: "2021-4-19",
        horizon: 0, // less than 1 year yet.
        opportunity_cost: 0.1,
        left_horizon: 2,
        short_return: 0.2,
        long_return: 0.1
      },
    };
  },
  // created() {
  //   axios
  //       .get("/profile?id=" + 123)
  //       .then((res) => {
  //         this.form = res.data;
  //       })
  //       .catch((err) => {
  //         console.error(err);
  //       });
  // },

  // methods: {
  //   Edit(formName) {
  //     this.$refs[formName].validate((valid) => {
  //       if (valid) {
  //         alert('submit!');
  //       } else {
  //         console.log('error submit!!');
  //         return false;
  //       }
  //     });
  //   },
  //   Back(formName) {
  //     this.$refs[formName].resetFields();
  //   }
  // }
}
</script>

