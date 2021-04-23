<template>
  <div>
  <el-table
      :data="data.slice((currentPage-1)*pagesize,currentPage*pagesize)"
      style="width: 100%"
      height="900"
      :row-style="{fontSize: '20px'}"
      :default-sort="{prop: 'stock_code', order: 'ascending'}"
      :header-cell-style="{fontSize: '24px', height:'100px'}" >
    <el-table-column
        fixed
        width="50"
    >
    </el-table-column>
    <el-table-column
        fixed
        prop="code"
        label="Code"
        width="200"
        sortable>
    </el-table-column>
    <el-table-column
        prop = "purchase_date"
        label="Purchase Date"
        width="250"
        sortable>
    </el-table-column>
    <el-table-column
        prop = "close_price"
        label="Close Price"
        width="250"
        sortable>
    </el-table-column>
    <el-table-column
        prop = "purchase_price"
        label= "Purchase Price"
        width="250"
        sortable>
    </el-table-column>
    <el-table-column
        prop = "target_price"
        label="Target Price"
        width="250"
        sortable>
    </el-table-column>
    <el-table-column
        prop = "expect_return_rate"
        label="Expect Return Rate"
        width="300"
        sortable>
    </el-table-column>
<!--    <el-table-column-->
<!--        prop="horizon"-->
<!--        label="Horizon"-->
<!--        width="200">-->
<!--    </el-table-column>-->
<!--    <el-table-column-->
<!--        prop="left_horizon"-->
<!--        label="Left Horizon"-->
<!--        width="200">-->
<!--    </el-table-column>-->
    <el-table-column label="Action">
      <template slot-scope="scope">
        <el-button
            size="medium"
            @click="handleDetails(scope.$index, scope.row)">Details</el-button>
      </template>
    </el-table-column>
  </el-table>
  </div>
</template>

<script>

import axios from "axios";

export default {
  data(){
    return{
      data: [],
      pagesize:10,
      currentPage:1
    }
  },
  created() {
    axios
        .get("/profile?id=" + 123)
        .then((res) => {
          let data = []
          for(let i in res.data.stocks){
            data.push(res.data.stocks[i])
          }
          this.data = data

        })
        .catch((err) => {
          console.error(err);
        });
  },
  current_change:function(currentPage){
    this.currentPage = currentPage;
  },
  filters: {
    rounding (value) {
      return value.toFixed(2)
    }
  }
}

</script>

<style lang="scss" scoped>
  .el-table {
    font-family: Helvetica;
  }
  .el-table__header-wrapper{
    font-size: 30px;
  }
</style>