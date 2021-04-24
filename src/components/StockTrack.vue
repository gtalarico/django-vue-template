<template>
  <el-table
    :data="stockData"
    style="width: 100%"
    :default-sort="{ prop: 'stock_code', order: 'ascending' }"
  >
    <el-table-column prop="name" label="Name"> </el-table-column>
    <el-table-column prop="purchase_date" label="Purchase Date" sortable>
    </el-table-column>
    <el-table-column prop="close_price" label="Close Price" sortable>
    </el-table-column>
    <el-table-column prop="purchase_price" label="Purchase Price" sortable>
    </el-table-column>
    <el-table-column prop="target_price" label="Target Price" sortable>
    </el-table-column>
    <el-table-column
      prop="expect_return_rate"
      label="Expect Return Rate"
      sortable
    >
    </el-table-column>
    <el-table-column label="Action">
      <template slot-scope="scope">
        <el-button
          size="medium"
          type="primary"
          @click="handleDetails(scope.$index, scope.row)"
          >Details</el-button
        >
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import axios from "axios";
import {getStore} from "@/config/utils";

export default {
  name: "stocktrack",
  data() {
    return {
      stockData: [],
    };
  },
  created() {
    axios
      .get("/profile?id=" + 123)
      .then((res) => {
        let data = [];
        for (let key in res.data.stocks) {
          var stock = res.data.stocks[key];
          stock["name"] = key;
          data.push(stock);
        }
        this.stockData = data;
      })
      .catch((err) => {
        console.error(err);
      });
  },
  methods:{
    handleDetails(index, row){
      console.log(index, row)
      let stock_code, user_id;
      stock_code = stockData[index].code
      user_id = getStore("user").user_id
      .get("/profile/stock_detail", {
          data: {s_code: stock_code, id: user_id },
        })

    }
  },
  filters: {
    rounding(value) {
      return value.toFixed(2);
    },
  },
};
</script>

<style lang="scss" scoped>
</style>