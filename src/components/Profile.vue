<template>

  <el-form :model="form" ref="form" class="demo-form" label-position="left" >
    <el-form-item label="Name" prop="name" label-width="50px" class="item_name">
      <el-input  v-model="form.name" :disabled="true" style="width: 50%"></el-input>
    </el-form-item>

    <el-form-item label="Email" prop="email" label-width="50px">
      <el-input v-model="form.email" :disabled="true" style="width: 50%"></el-input>
    </el-form-item>

    <el-form :inline="true" ref="form" class="demo-form-inline">
      <el-form-item label="Short Tax Rate" prop="short_tax_rate" label-width="120px">
        <el-input  v-model="form.short_tax_rate"></el-input>
      </el-form-item>
      <el-form-item label="Long Tax Rate" prop="long_tax_rate" label-width="120px">
        <el-input  v-model="form.long_tax_rate"></el-input>
      </el-form-item>
    </el-form>

    <el-form-item label="Investment Horizon" prop="investment_horizon" label-width="140px" style="width: 50%">
      <el-input v-model="form.investment_horizon" ></el-input>
    </el-form-item>

  <el-form-item>
    <el-button type="primary" @click="Save">Save</el-button>
  </el-form-item>
  </el-form>
</template>


<script>
import axios from "axios";
import {getStore} from "@/config/utils";
export default {
  data() {
    return {
      form:{
        name: '',
        email: '',
        short_tax_rate: '',
        long_tax_rate: '',
        investment_horizon: ''
      },
    };
  },
  created() {
    axios
        .get("/profile?id=" + 123)
        .then((res) => {
          this.form = res.data;
          this.form.name = getStore("user").name;
          this.form.email = getStore("user").email;
        })
        .catch((err) => {
          console.error(err);
        });
  },

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

