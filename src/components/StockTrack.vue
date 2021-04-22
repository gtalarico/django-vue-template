<template>
  <el-table
      :data="stock_data"
      style="font-size: 20px"
      width = "100%"
      height="300"
      :default-sort="{prop: 'stock_code', order: 'ascending'}"
      :header-cell-style="{fontSize: '24px'}" >
    <el-table-column
        fixed
        prop="stock_code"
        label="Code"
        width="250"
        >
    </el-table-column>
    <el-table-column
        prop="close_price"
        label="Close Price"
        width="250"
        >
    </el-table-column>
    <el-table-column
        prop="purchase_price"
        label="Purchase Price"
        width="200"
        style="font-size: 24px">
    </el-table-column>
    <el-table-column
        prop="target_price"
        label="Target Price"
        width="200"
       >
    </el-table-column>
    <el-table-column
        prop="horizon"
        label="Horizon"
        width="200"
        >
    </el-table-column>
    <el-table-column
        prop="left_horizon"
        label="Left Horizon"
        width="200"
      >
    </el-table-column>
    <el-table-column align="right">
      <template slot-scope="scope">
        <el-button
            size="medium"
            @click="handleEdit(scope.$index, scope.row)">Edit</el-button>
        <el-button
            size="medium"
            @click="handleDetails(scope.$index, scope.row)">Details</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>

export default {
  data() {
    return {
      stock_data: [{
        stock_code: "NIO",
        close_price: 31.3,
        purchase_price: 27.0,
        target_price: 40.0,
        horizon: 0,
        left_horizon: 2,
      },
        {
          stock_code: "APPL",
          close_price: 100.0,
          purchase_price: 98.0,
          target_price: 110.0,
          horizon: 0,
          left_horizon: 1,
        }]
    }
  },
  filters: {
    rounding (value) {
      return value.toFixed(2)
    }
  }
}

// Vue.component()
// const axios = require('axios');
// export default {
//   mounted(){
//     axios
//         .get(baseUrl+'profile/stock_detail/id=123')
//   }
</script>

<style lang="scss" scoped>
  .el-table {
    font-family: Helvetica;
  }
  .el-table__header-wrapper{
    font-size: 30px;
  }
</style>