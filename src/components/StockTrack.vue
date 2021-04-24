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
import { getStore, removeItem } from "@/config/utils";
export default {
  name: "stocktrack",
  data() {
    return {
      stockData: [],
    };
  },
  created() {
    axios
      .get("/profile", {
        data: { id: getStore("user").id },
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      })
      .then((res) => {
        console.log(res);
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
  filters: {
    rounding(value) {
      return value.toFixed(2);
    },
  },
};
</script>

<style lang="scss" scoped>
</style>