<template>
  <el-table
    :data="stockData"
    stripe
    :cell-style="set_cell_style"
    style="width: 100%"
    :default-sort="{ prop: 'stock_code', order: 'ascending' }"
  >
    <el-table-column prop="name" label="Name"></el-table-column>
    <el-table-column prop="purchase_date" label="Purchase Date" sortable>
    </el-table-column>
    <el-table-column prop="close_price" label="Close Price ($)" sortable>
    </el-table-column>
    <el-table-column prop="purchase_price" label="Purchase Price ($)" sortable>
    </el-table-column>
    <el-table-column
      prop="target_price"
      label="Target Price ($)"
      class="target_price"
      sortable
    >
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
          type="primary"
          icon="el-icon-edit"
          circle
          @click="handleDetails(scope.$index, scope.row)"
        ></el-button>
        <el-button
          icon="el-icon-delete"
          type="danger"
          circle
          @click="handleDelete(scope.$index, scope.row)"
        ></el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import axios from "axios";
import { getStore } from "@/config/utils";
import router from "@/router/router";

export default {
  name: "stocktrack",
  data() {
    return {
      stockData: [],
    };
  },
  created() {
    axios
      .post("/profile/", {
        id: getStore("user").user_id,
      })
      .then((res) => {
        // console.log(res);
        let data = [];
        for (let key in res.data.stocks) {
          var stock = res.data.stocks[key];
          stock["name"] = key;
          stock["close_price"] = stock["close_price"].toFixed(2);
          stock["purchase_price"] = stock["purchase_price"].toFixed(2);
          stock["target_price"] = stock["target_price"].toFixed(2);
          data.push(stock);
        }
        this.stockData = data;
      })
      .catch((err) => {
        // console.error(err);
      });
  },
  methods: {
    handleDetails(index, row) {
      console.log(index, row);
      let stock_code, user_id;
      stock_code = this.stockData[index].code;
      user_id = getStore("user").user_id;
      router.push({
        name: "StockDetails",
        query: { stock_code: stock_code, user_id: user_id },
      });
    },
    handleDelete(index, row) {
      let stock_code, user_id;
      stock_code = this.stockData[index].code;
      user_id = getStore("user").user_id;
      axios
        .post("profile/delete_stock/", {
          id: user_id,
          deleted_stocks: [stock_code],
        })
        .then((res) => {
          if (res.data == "Deleting Succeeded!") {
            this.$message({
              message: "The stock has been deleted",
              type: "success",
            });
            this.$router.push("/home/stocktrack");
          } else {
            this.$message({
              message: "Something went wrong...",
              type: "error",
            });
            this.$router.push("/home/stocktrack");
          }
        })
        .catch((err) => {
          this.$message({
            message: "Something went wrong...",
            type: "error",
          });
          this.$router.push("/home/stocktrack");
        });
    },
    set_cell_style(row, column, rowIndex, columnIndex) {
      if (row.column.label === "Purchase Price ($)") {
        return "color: #389DFF; font-size: 16px; font-weight: bold";
      } else if (row.column.label === "Close Price ($)") {
        // console.log(row);
        if (
          this.stockData[row.rowIndex]["close_price"] >=
          this.stockData[row.rowIndex]["purchase_price"]
        ) {
          return "font-size:16px; color: green";
        } else {
          return "font-size:16px; color: red";
        }
      } else if (row.column.label === "Target Price ($)") {
        return "font-size:16px";
      } else if (row.column.label === "Name") {
        return "font-size:16px";
      } else return "font-size:16px";
    },
  },
  filters: {
    rounding(value) {
      return value.toFixed(2);
    },
  },
};
</script>

<style lang="sass" scoped>
.el-table .target_price
  background: oldlace
</style>