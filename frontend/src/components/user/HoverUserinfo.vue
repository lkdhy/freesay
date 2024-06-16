<script setup lang="ts">
import { UserFilled } from "@element-plus/icons-vue"
import {ref} from "vue";
import {useRouter} from "vue-router";
import ChatDialog from "@/components/chat_dialog/ChatDialog.vue";

const router = useRouter()
// props
const props = defineProps({
  hostName: String,
  hostAvatar: String,
  hostSignature: String
})

const showRecentAnswer = ref(false)
const showChatDialog = ref(false)

const jump2userBox = (hostName: string) => {
  router.push(`/user2/${hostName}`)
}

</script>

<template>

<!--  你好啊，我是{{ hostName }}，下面是我的个性签名-->

  <el-space>
<!--    <el-avatar :icon="UserFilled" size="large" shape="square"></el-avatar>-->

    <el-avatar
        :src="hostAvatar"
        :size="60"
    ></el-avatar>
    <p> {{ hostName }}</p>
  </el-space>

  <div class="signature-container">
    <p> {{ hostSignature }} </p>
  </div>

  <el-button
      type="primary"
      @click="jump2userBox(<string>hostName)"
  >
<!--    TA 最近的回答-->
    向 TA 提问
  </el-button>

  <el-button
      type="success"
      @click="showChatDialog = true"
  >
    私信 TA
  </el-button>

  <div
      v-if="showChatDialog"
  >
    <chat-dialog @close="showChatDialog = false">
    </chat-dialog>
  </div>
<!--  <div v-if="showRecentAnswer">-->
<!--    <p>-->
<!--      这里会显示 TA 最近的问答帖-->
<!--    </p>-->
<!--  </div>-->
</template>

<style scoped>
.signature-container {
  margin-top: 10px;
  margin-bottom: 15px;
}

</style>