<script setup lang="ts">
import {onBeforeMount, ref, watch} from "vue";
import {CircleCloseFilled} from "@element-plus/icons-vue";
import {ChatSendApi, ChatGetApi, AnswerApi, UpdateThread} from "@/request/api";
import {ElMessage, ElNotification} from "element-plus";
import {useUserstore} from "@/store/user";
import Message from "@/components/chat_dialog/Message.vue";

const useStore = useUserstore()
const self = useStore.userName
const selfAvatar = useStore.avatar

interface chatMessage {
  username: string, message: string,
}
const props = defineProps({
  user: String, userAvatar: String,
  // messages: Array<chatMessage>, // TODO: check this
})

const emit = defineEmits(['close', 'responded'])
const visible = ref(true)
watch(visible, () => {
  emit('close')
})
const loading = ref(false)

const message = ref<chatMessage[]>([]) // TODO: check this
const chatResponse = ref('')

const fetchChatData = async () => {
  loading.value = true
  const res = await ChatGetApi({
    user1: self,
    user2: <string>props.user,
  })
  if (res.success) {
    console.log(res)
    message.value = []
    message.value = res.chats
  } else {
    console.log('WTF，私聊消息获取失败')
  }
  loading.value = false
}
onBeforeMount(() => {
  fetchChatData()
})

const submitResponse = async (response: string) => {
  if (response.length === 0)
  {
    ElMessage.error('请输入~'); return
  }
  const res = await ChatSendApi({
    user1: self,
    user2: <string>props.user,
    sender: self,
    content: response
  })
  if (res.success) {
    ElNotification({
      title: '已回复',
      type: 'success',
      showClose: false,
    })
    console.log(res.message)
    chatResponse.value = ''
  } else {
    console.log('WTF，私信聊天消息发送失败')
  }
  // update chat messages instantaneously
  await fetchChatData()
}
</script>

<template>

  <el-dialog
      v-model="visible"
      :show-close="false"
      top="6vh"
      width="70%"
  >
    <template #header="{ close, titleId, titleClass }">
      <div class="my-header">
        <el-space size="large">
          <el-avatar :src="userAvatar" shape="square" size="large"></el-avatar>
          <h1 :id="titleId" class="title-username">
            {{ user }}
          </h1>
        </el-space>
        <el-button type="danger" @click="close">
          <el-icon class="el-icon--left"><circle-close-filled/></el-icon>
          Close
        </el-button>
      </div>

      <el-divider></el-divider>
    </template>
    <div v-loading="loading" class="message-container">
<!--      style="display: flex; flex-direction: column; align-items: center"-->
      <el-scrollbar
          height="95%"
      >
<!--        <p v-for="x in message">hhh</p>-->
        <div style="display: flex; flex-direction: column; align-items: center">
          <message v-for="msg in message"
                   :from-self="msg.username === self"
                   :username="msg.username"
                   :avatar="msg.username === self ? selfAvatar : userAvatar"
                   :message="msg.message"
                   :key="msg.message"
          >
          </message>
        </div>
      </el-scrollbar>
    </div>
    <div class="input-container">
      <el-input
          type="textarea"
          v-model="chatResponse"
          :rows="2"
          input-style="
            font-size: 20px;
            letter-spacing: 1.5px;
            line-height: 1.5;
          "
      >

      </el-input>

      <div class="respond-button-container">
        <el-button
            @click="submitResponse(chatResponse);"
            type="primary"
        >
          回复
        </el-button>
      </div>
    </div>
  </el-dialog>
</template>

<style scoped>

.my-header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
}
.title-username {
  font-size: 30px;
}
.message-container {
  height: 50vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.respond-button-container {
  display: flex;
  justify-content: right;
  margin-top: 5px;
  margin-bottom: 5px;
}
</style>