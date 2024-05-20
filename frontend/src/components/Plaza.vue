<script lang="ts">
import {ref, reactive, onBeforeMount, onBeforeUpdate, onUpdated} from "vue";
import {ElMessage, ElNotification as notify } from 'element-plus';
import { GetBoxApi } from "@/request/api";
import BoxCard from "@/components/BoxCard.vue";

export default {
  components: { BoxCard },
  setup() {
    interface Box {
      username: string, description: string
    }
    const boxData = ref<Box[]>([]);
    const total = ref(100);
    const fetchBoxData = async () => {
      console.log('即将发送获取所有 boxes 的请求');
      let res = await GetBoxApi();
      console.log('boxes请求完毕，结果是：', res);
      if (res.success) {
        res.boxes.forEach(box => {
          boxData.value.push({
            username: box.username, description: box.description
          });
        })
        total.value = res.total_boxes;
      } else {
        ElMessage.error('WTF, Boxes 请求失败')
      }
    }

    onBeforeMount(fetchBoxData)

    return { boxData }
  },
}
</script>

<template>
  <h2 style="text-align: center;
margin-bottom: 1em">
    广场
  </h2>
  <el-scrollbar height="550px">
    <div class="canvas">
<!--      <div v-for="box of boxData">-->
        <box-card v-for="box of boxData"
            :host-name="box.username">
          <template #desc>
            {{ box.description }}
          </template>
          <template #hostInfo>
            {{ box.username }}
          </template>
        </box-card>
<!--      </div>-->
    </div>
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