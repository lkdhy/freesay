<script setup lang="ts">
import { reactive, ref } from "vue";
import {useRouter} from 'vue-router';
import {ElMessage} from 'element-plus';
import {RegisterApi} from "@/request/api";
import {useUserstore} from "@/store/user";

const router = useRouter();
const userStore = useUserstore();

console.log(`当前登录用户${userStore.userName}`)
const curUser = ref<string>(userStore.userName);
// const visUser = ref<string>('tmp');

</script>

<template>

  <h1>我是个人主页</h1>

  <h3>
    你好 {{ curUser }}
  </h3>
  <h3>
    这里是 {{ $route.params.id }} 的个人主页
  </h3>

</template>

<style scoped>

</style>