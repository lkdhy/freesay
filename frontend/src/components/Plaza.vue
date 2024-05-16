<script lang="ts">
import {ref, reactive, onBeforeMount, onBeforeUpdate, onUpdated} from "vue";
import type {FormInstance, FormRules} from 'element-plus';
import {ElMessage, ElNotification as notify } from 'element-plus';
import { GetBoxApi } from "@/request/api";
import {useRouter} from 'vue-router';
import {useUserstore} from "@/store/user";
import BoxCard from "@/components/BoxCard.vue";

export default {
  components: {
    BoxCard
  },
  setup() {
    const userStore = useUserstore();
    const router = useRouter();

    interface Box {
      username: string, description: string
    }

    const boxData = ref<Box[]>([]);
    const total = ref(100);

    onBeforeMount(async () => {
      console.log('onBeforeMount: 即将发送获取所有 res 的请求');
      let res = await GetBoxApi();
      console.log(res);
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
    });
    return {
      boxData
    }
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
      <div v-for="box of boxData">
        <box-card :host-name="box.username">
          <template #desc>
            {{ box.description }}
          </template>
          <template #hostInfo>
            {{ box.username }}
          </template>
        </box-card>
      </div>
    </div>
  </el-scrollbar>

</template>

<style scoped>
.canvas {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  width: 100%;
}
.boxRow {
  display: flex;
  justify-content: space-between;
  width: 95%
}
</style>