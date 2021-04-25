<template>
  <div>
    <el-form ref="form" :model="form">
      <el-form-item label="Stock code">
        <el-input v-model="form.code"></el-input>
      </el-form-item>
      <el-form-item label="Purchase price ($)">
        <el-input v-model="form.purchase_price"></el-input>
      </el-form-item>
      <el-form-item label="Target price ($)">
        <el-input v-model="form.target_price"></el-input>
      </el-form-item>
      <el-form-item label="Purchase date (day)">
        <el-date-picker
          v-model="form.purchase_date"
          type="date"
          placeholder="选择日期"
        >
        </el-date-picker>
      </el-form-item>
      <el-form-item label="Expect return rate">
        <el-input v-model="form.expect_return_rate"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="Add">Add</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from "axios";
import { getStore } from "@/config/utils";
export default {
  name: "addstock",
  methods: {
    Add() {
      let added_stocks = {};
      added_stocks[this.form.code] = {
        purchase_price: this.form.purchase_price,
        purchase_date: this.form.purchase_date,
        target_price: this.form.target_price,
        expect_return_rate: this.form.expect_return_rate,
      };
      axios
        .post("/profile/add_stock/", {
          id: getStore("user").user_id,
          added_stocks,
        })
        .then((res) => {
          console.log(res);
          if (res.data == "Adding Succeeded!") {
            this.$message({
              message: "You have added the stock! Good luck!",
              type: "success",
            });
            this.$router.push("/home/stocktrack/");
          } else {
            this.$message({
              message: "something wrong when trying to add the stock...",
              type: "error",
            });
          }
        })
        .catch((err) => {
          console.error(err);
          this.$message({
            message: "something wrong when trying to add the stock...",
            type: "error",
          });
        });
    },
  },
  data() {
    return {
      form: {
        code: "",
        purchase_price: "",
        purchase_date: "",
        target_price: "",
        expect_return_rate: "",
      },
    };
  },
};
</script>
