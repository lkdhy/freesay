<script setup lang="ts">
import {onBeforeMount, ref} from "vue";
import {GetUserInfoByPageNum} from "@/request/api";
import Profile from "@/components/Profile.vue";

interface User {
  userName: string,
  first_name: string, last_name: string
  email: string
}
const tableData = ref<User[]>([]);
let currentPage = ref(1);
let pageSize = ref(10);
let total = ref(100);

onBeforeMount(async () => {
  let res = await GetUserInfoByPageNum({
    pageNumber: 1, number: 15
  })
  res.users.forEach(item => {
    tableData.value.push({
      userName: item.username,
      first_name: item.first_name, last_name: item.last_name,
      email: item.email
    });
  });
  total.value = res.total_users;
  console.log('total_pages:', total.value);
})

const handleCurrentChange = (newPage: number) => {
  currentPage.value = newPage;
  fetchData();
};
const fetchData = async () => {
  // 在这里调用 API 获取数据，使用 currentPage 作为参数
  let res = await GetUserInfoByPageNum({
    pageNumber: currentPage.value, number: 15
  });
  tableData.value = [];
  res.users.forEach(item => {
    tableData.value.push({
      userName: item.username,
      first_name: item.first_name, last_name: item.last_name,
      email: item.email
    });
  });
  total.value = res.total_users;
};

</script>

<template>
<!--  <el-row>-->
<!--    <el-col :span="24">-->

<!--      不要 stripe（斑马纹）  -->
<!--   仅是排版，故不显示顶部的表头 -->
<!--  <el-scrollbar>-->
<!--  TODO: 优化高度计算的逻辑 -->
      <el-table
          :data="tableData"
          :show-header="false"
          style="width: 100%"
          max-height="575"
      >
        <el-table-column label="哈哈哈，我不会被显示出来">
          <template #default="scope">
            <profile></profile>
          </template>
        </el-table-column>
        <el-table-column>
          <template #default="scope">
            <profile></profile>
          </template>
        </el-table-column>
        <el-table-column>
          <template #default="scope">
            <profile></profile>
          </template>
        </el-table-column>

        <el-table-column>
          <template #default="scope">
            <profile></profile>
          </template>
        </el-table-column>
<!--        <el-table-column>-->
<!--          <template #default="scope">-->
<!--            <profile></profile>-->
<!--          </template>-->
<!--        </el-table-column>-->
<!--        <el-table-column>-->
<!--          <template #default="scope">-->
<!--            <profile></profile>-->
<!--          </template>-->
<!--        </el-table-column>-->
<!--        <el-table-column prop="userName" label="用户名" width="180"/>-->
<!--        <el-table-column prop="email" label="邮箱"/>-->
      </el-table>
<!--  </el-scrollbar>-->
<!--    </el-col>-->
<!--  </el-row>-->

  <el-pagination
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :page-size="pageSize"
      layout="prev, pager, next"
      :total="total"
  />

</template>

<style scoped>

</style>