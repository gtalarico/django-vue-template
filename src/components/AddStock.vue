<template>
  <div>
    <el-table :data="tableData" style="width: 100%" v-loading="loading">
      <el-table-column prop="code" label="Stock Code"> </el-table-column>
      <el-table-column prop="purchase_price" label="Purchase Price">
      </el-table-column>
      <el-table-column prop="target_price" label="Target Price">
      </el-table-column>
      <el-table-column
        prop="displayed_purchase_date"
        label="Purchase Date"
      ></el-table-column>
      <el-table-column
        prop="expect_return_rate"
        label="Expect Return Rate"
      ></el-table-column>
      <el-table-column label="Action">
        <template slot-scope="scope">
          <el-button
            icon="el-icon-delete"
            type="danger"
            circle
            @click="Delete(scope.$index, scope.row)"
          ></el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-button
      type="primary"
      icon="el-icon-plus"
      circle
      @click="dialogAddVisible = true"
      style="margin-top: 30px; margin-left: 10px"
    ></el-button>
    <el-button
      type="primary"
      icon="el-icon-upload"
      circle
      @click="dialogUploadVisible = true"
      style="margin-top: 30px; margin-left: 10px"
    ></el-button>
    <el-button
      type="primary"
      style="margin-top: 30px; margin-right: 10px; float: right"
      @click="Submit()"
      >Submit</el-button
    >
    <el-dialog title="Upload" :visible.sync="dialogUploadVisible">
      <el-upload
        class="upload-demo"
        drag
        action=""
        ref="upload"
        :on-change="handleUploadChange"
        :auto-upload="false"
        :limit="1"
      >
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">
          Drag the file here, or <em>click to upload</em>
        </div>
        <div class="el-upload__tip" slot="tip">Only .CSV is allowed</div>
      </el-upload>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="Template()" style="float: left"
          >Template</el-button
        >
        <el-button @click="dialogUploadVisible = false">Cancle</el-button>
        <el-button type="primary" @click="Upload()">Confirm</el-button>
      </div>
    </el-dialog>
    <el-dialog title="New Stock" :visible.sync="dialogAddVisible">
      <el-form ref="form" :model="form" label-position="left">
        <el-form :inline="true"
          ><el-row>
            <el-col :span="12"
              ><el-form-item label="Stock code" inline>
                <el-input v-model="form.code"></el-input> </el-form-item
            ></el-col>
            <el-col :span="12"
              ><el-form-item label="Purchase price ($)">
                <el-input
                  v-model="form.purchase_price"
                ></el-input> </el-form-item
            ></el-col> </el-row
        ></el-form>
        <el-form :inline="true"
          ><el-row>
            <el-col :span="12"
              ><el-form-item label="Target price ($)">
                <el-input v-model="form.target_price"></el-input> </el-form-item
            ></el-col>
            <el-col :span="12"
              ><el-form-item label="Expect return rate">
                <el-input
                  v-model="form.expect_return_rate"
                ></el-input> </el-form-item></el-col></el-row
        ></el-form>
        <el-form :inline="true">
          <el-form-item label="Purchase date (day)">
            <el-date-picker
              v-model="form.purchase_date"
              type="date"
              placeholder="Purchase date"
            >
            </el-date-picker>
          </el-form-item>
        </el-form>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogAddVisible = false">Cancle</el-button>
        <el-button type="primary" @click="Add()">Confirm</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import axios from "axios";
import { getStore } from "@/config/utils";
import moment from "moment";
import Papa from "papaparse";
import XLSX from "xlsx";
export default {
  name: "addstock",
  methods: {
    Submit() {
      let added_stocks = {};
      this.tableData.forEach(function (stock) {
        added_stocks[stock.code] = {
          purchase_price: stock.purchase_price,
          purchase_date: stock.purchase_date,
          target_price: stock.target_price,
          expect_return_rate: stock.expect_return_rate,
        };
      });
      this.loading = true;
      axios
        .post("/profile/add_stock/", {
          id: getStore("user").user_id,
          added_stocks,
        })
        .then((res) => {
          console.log(res);
          this.loading = false;
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
          this.loading = false;
          // console.error(err);
          this.$message({
            message: "something went wrong when trying to add the stock...",
            type: "error",
          });
        });
    },
    handleUploadChange(e) {
      const that = this;
      const fileToLoad = event.target.files[0];
      const reader = new FileReader();
      reader.onload = (fileLoadedEvent) => {
        Papa.parse(fileLoadedEvent.target.result, {
          header: true,
          complete(results) {
            // that.doc = JSON.stringify(results.data, null, 2);
            // console.log(that.doc);
            that.doc = results.data;
            console.log(that.doc);
          },
          error(errors) {
            this.$message({
              message: errors,
              type: "error",
            });
          },
        });
      };
      reader.readAsText(fileToLoad);
    },
    Upload() {
      const that = this;
      this.doc.forEach(function (stock) {
        var form = stock;
        form.purchase_date = new Date(form.purchase_date);
        form.displayed_purchase_date = moment(
          String(form.purchase_date)
        ).format("YYYY-MM-DD");
        that.tableData.push(form);
        that.dialogUploadVisible = false;
      });
    },
    Add() {
      var form = {
        code: this.form.code,
        purchase_price: this.form.purchase_price,
        purchase_date: this.form.purchase_date,
        target_price: this.form.target_price,
        expect_return_rate: this.form.expect_return_rate,
      };
      form.displayed_purchase_date = moment(
        String(this.form.purchase_date)
      ).format("YYYY-MM-DD");
      this.tableData.push(form);
      this.form = {};
      this.dialogAddVisible = false;
    },
    Delete(index, row) {
      this.tableData.splice(index, 1);
    },
    Template() {
      const worksheet = XLSX.utils.json_to_sheet([this.form]);
      const csvOutput = XLSX.utils.sheet_to_csv(worksheet);
      function s2ab(s) {
        var buf = new ArrayBuffer(s.length);
        var view = new Uint8Array(buf);
        for (var i = 0; i != s.length; ++i) view[i] = s.charCodeAt(i) & 0xff;
        return buf;
      }
      saveAs(
        new Blob([s2ab(csvOutput)], { type: "application/octet-stream" }),
        "Stock_template.csv"
      );
    },
  },
  data() {
    return {
      doc: null,
      form: {
        code: "",
        purchase_price: "",
        purchase_date: "",
        target_price: "",
        expect_return_rate: "",
      },
      tableData: [],
      dialogAddVisible: false,
      dialogUploadVisible: false,
      loading: false,
    };
  },
};
</script>
<style lang="sass" scoped>
</style>