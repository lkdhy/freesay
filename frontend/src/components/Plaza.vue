<script setup lang="ts">
import {ref, reactive, onBeforeMount, onBeforeUpdate, onUpdated} from "vue";
import type {FormInstance, FormRules} from 'element-plus';
import {ElMessage, ElNotification as notify } from 'element-plus';
import { GetBoxApi } from "@/request/api";
import {useRouter} from 'vue-router';
import {useUserstore} from "@/store/user";
import BoxCard from "@/components/BoxCard.vue";

const userStore = useUserstore();
const router = useRouter();

interface Box {
  username: string,
  description: string
}
let boxData = ref<Box[]>([]);
const total = ref(100);

onBeforeMount(async () => {
  console.log('onBeforeMount: 即将发送获取所有 res 的请求');
  let res = await GetBoxApi();
  console.log(res);
  if (res.success) {
    res.boxes.forEach(box => {
      boxData.value.push({
        username: box.username,
        description: box.description
      });
    })
    total.value = res.total_boxes;
    // console.log(router.currentRoute.value);
  } else {
    ElMessage.error('WTF, Boxes 请求失败')
  }
});

</script>

<template>
  <h1>
    我是广场
  </h1>
  <p>
    这里之后全都是别人分享的提问箱哦~
  </p>
<!--  <ul>-->
<!--    <li v-for="box of boxData">-->
<!--      <h3> {{ box.username }} </h3>-->
<!--      <p> {{ box.description }}</p>-->
<!--    </li>-->
<!--  </ul>-->
  <div v-for="box of boxData">
    <div style="display: flex; width: 100%">
      <box-card></box-card>
      <box-card></box-card>
      <box-card></box-card>
    </div>
  </div>
</template>

<style scoped>

</style>