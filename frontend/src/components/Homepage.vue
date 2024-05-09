<script setup lang="ts">
import {onBeforeMount, reactive, ref} from "vue";
import {useRouter} from 'vue-router';
import {ElMessage} from 'element-plus';
import {RegisterApi} from "@/request/api";
import {useUserstore} from "@/store/user";
import PostDialog from "@/components/PostDialog.vue";

const router = useRouter();
const userStore = useUserstore();

console.log(`当前访问用户是${userStore.visitedUserName}`);
console.log(`你是${userStore.userName}`);

const curUser = ref<string>(userStore.userName);
// const visUser = ref<string>($route.params.id);
// console.log(visUser);

</script>

<template>

  <h2>我是个人主页</h2>

  <h3>
    你好 {{ curUser }}
  </h3>
  <h3>
    这里是 {{ $route.params.id }} 的个人主页
  </h3>

  <el-descriptions
      title="User Info"
      border
  >
    <el-descriptions-item label="Username">
      {{ $route.params.id }}
    </el-descriptions-item>
    <el-descriptions-item label="姓名"></el-descriptions-item>
    <el-descriptions-item label="Place">
      这些东西后面再仔细搞！！！
    </el-descriptions-item>
    <el-descriptions-item label="Remarks">
      <el-tag size="small">School</el-tag>
    </el-descriptions-item>
    <el-descriptions-item label="Address">
<!--      No.1188, Wuzhong Avenue, Wuzhong District, Suzhou, Jiangsu Province-->
    </el-descriptions-item>
  </el-descriptions>

<!--  <el-button type="primary">-->
<!--    向他提问-->
<!--  </el-button>-->

  <post-dialog>
    <template v-slot:hostName>
      {{ $route.params.id }}
    </template>
  </post-dialog>

<!--  TODO  -->
  <div>
    <h2>
      他的回答
    </h2>
    <p>
      ……………………………………
    </p>
  </div>

</template>

<style scoped>
/* TODO */
* {
  margin: 10px;
}
</style>