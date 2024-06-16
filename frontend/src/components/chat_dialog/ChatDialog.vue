<script setup lang="ts">
import {onBeforeMount, ref, watch} from "vue";
import {CircleCloseFilled} from "@element-plus/icons-vue";
import {ChatSendApi, ChatGetApi} from "@/request/api";

const props = defineProps({

})

const emit = defineEmits(['close', 'responded'])
const visible = ref(true)
watch(visible, () => {
  emit('close')
})
const loading = ref(false)

const fetchChatData = async () => {

}
onBeforeMount(() => {
  loading.value = true
})

</script>

<template>

  <el-dialog
      v-model="visible"
      :show-close="false"
      fullscreen
  >
    <template #header="{ close, titleClass }">
      <div class="my-header">
        <el-button type="danger" @click="close">
          <el-icon class="el-icon--left"><circle-close-filled/></el-icon>
          Close
        </el-button>
      </div>
    </template>
    <div v-loading="true">

    </div>
  </el-dialog>
</template>

<style scoped>

.my-header {
  display: flex;
  flex-direction: row;
  justify-content: right;
}
</style>