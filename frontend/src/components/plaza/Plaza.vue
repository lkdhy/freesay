<script setup lang="ts">
import {ref, reactive, onBeforeMount, onBeforeUpdate, onUpdated} from "vue";
import {ElMessage, ElNotification as notify } from 'element-plus';
import { GetBoxApi } from "@/request/api";
import BoxCard from "@/components/BoxCard.vue";
interface Box {
  username: string,
  avatar: string,
  hostSignature: string,
  description: string
}
const boxData = ref<Box[]>([]);
const total = ref(100);
const loading = ref(true)
const fetchBoxData = async () => {
  // console.log('即将发送获取所有 boxes 的请求');
  loading.value = true
  let res = await GetBoxApi();
  // console.log('boxes请求完毕，结果是：', res);
  if (res.success) {
    // res.boxes.forEach(box => {
    //   boxData.value.push(box);
    // })
    boxData.value = res.boxes
    total.value = res.total_boxes
  } else {
    ElMessage.error('WTF, Boxes 请求失败')
  }
  loading.value = false
}

onBeforeMount(fetchBoxData)

</script>

<template>
  <h2 style="text-align: center; margin-bottom: 1em">
    广场
  </h2>
  <el-scrollbar
      v-loading="loading"
      height="550px"
  >
    <el-space wrap :size="20" alignment="center">
<!--      <div v-for="box of boxData">-->
        <box-card
            v-for="box of boxData"
            :host-name="box.username"
            :host-avatar="box.avatar"
            :host-signature="box.hostSignature"
        >
          <template #desc>
            {{ box.description }}
          </template>
        </box-card>
    </el-space>
<!--      </div>-->
  </el-scrollbar>
</template>

<style scoped>
.canvas {
  display: flex;
  /* flex-wrap: 自动换行往里面堆 */
  flex-wrap: wrap;
  /* align-items: center; */
  /* width: 100%; */
}
</style>