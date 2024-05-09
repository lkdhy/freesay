<script setup lang="ts">
import {onBeforeMount, ref} from "vue";
import {GetUserInfoByPageNum} from "@/request/api";
import Profile from "@/components/Profile.vue";
import {useUserstore} from '@/store/user'
import {useRouter} from 'vue-router'

const userStore = useUserstore();
const router = useRouter();

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
    pageNumber: 1
  })
  res.users.forEach(item => {
    tableData.value.push({
      userName: item.username,
      first_name: item.first_name, last_name: item.last_name,
      email: item.email
    });
  });
  total.value = res.total_users;
  // console.log('total_pages:', total.value);
})

const handleCurrentChange = (newPage: number) => {
  currentPage.value = newPage;
  fetchData();
};
const fetchData = async () => {
  // 在这里调用 API 获取数据，使用 currentPage 作为参数
  let res = await GetUserInfoByPageNum({
    pageNumber: currentPage.value
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

// const record = (s: string) => {
//   console.log(s);
// }

const jump2Homepage = (userName: string) => {
  userStore.visitedUserName = userName;
  router.push(`/user/${userName}`);
}

</script>

<template>
  <el-row>
    <el-col :span="24">
      <el-table :data="tableData" stripe style="width: 100%">
        <el-table-column prop="userName" label="用户名" width="180"/>
        <el-table-column prop="first_name" label="姓" width="180"/>
        <el-table-column prop="last_name" label="名" width="180"/>
        <el-table-column prop="email" label="邮箱"/>
        <el-table-column label="去往他的个人主页">
          <template #default="scope">
            <el-button text @click="jump2Homepage(scope.row.userName)">
              试着点我 {{ scope.row.userName }}
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-col>
  </el-row>

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