<script setup lang="ts">
import { UserFilled } from "@element-plus/icons-vue"
import {ref} from "vue";
// props
const props = defineProps({
  hostName: String
})

const showRecentAnswer = ref(false)

</script>

<template>

<!--  你好啊，我是{{ hostName }}，下面是我的个性签名-->

  <el-space>
    <el-avatar :icon="UserFilled" size="large" shape="square"></el-avatar>

    <p> {{ hostName }}</p>
  </el-space>

  <div class="signature-container">
    <p>内心的强大、永远胜过外表的浮华。</p>
  </div>

  <el-button
      type="primary"
      @click="showRecentAnswer=true"
  >
    TA 最近的回答
  </el-button>

  <div v-if="showRecentAnswer">
    <p>
      这里会显示 TA 最近的问答帖
    </p>
  </div>
</template>

<style scoped>
.signature-container {
  margin-top: 10px;
  margin-bottom: 15px;
}

</style>