<script setup lang="ts">
import {ref} from "vue";
import {CircleCloseFilled} from "@element-plus/icons-vue";
import {watch} from "vue";
import PublicMessage from "@/components/public_box/PublicMessage.vue";
import {
  Message,
} from '@element-plus/icons-vue'
import {useUserstore} from "@/store/user";
import {AddPublicApi, SendPublicApi} from "@/request/api";
import {ElMessage} from "element-plus";

const useRouter = useUserstore()

interface public_thread {
  username: string
  avatar: string
  is_anonymous: boolean
  content: string
}
const props = defineProps({
  pid: Number,
  thread: Array<public_thread>
})

const emit = defineEmits(['close', 'responded'])
const visible = ref(true)
watch(visible, () => {
  emit('close')
})

const chatResponse = ref('')
const is_anonymous = ref(false)

console.log('pid=fnavdioandnaiovnioenavinviks', props.pid)
const submitPost = async (response: string) => {
  if (response.length === 0)
  { ElMessage.error('请输入~'); return }
  console.log('hrer')
  console.log(props.pid)
  const res = await SendPublicApi({
    pid: props.pid,
    username: useRouter.userName,
    content: chatResponse.value,
    is_anonymous: is_anonymous.value,
  })
  if (res.success) {
    ElMessage.success('发送成功')
    console.log(res.message)
    chatResponse.value = ''
    emit('responded')
  } else {
    ElMessage.error('发送失败')
  }
}
</script>

<template>
  <el-dialog v-model="visible"
             :show-close="false"
             top="8vh"
             width="50%"
  >
    <template #header="{ close, titleClass }">
      <div class="my-header">
        <el-button type="danger" @click="close">
          <el-icon class="el-icon--left"><circle-close-filled/></el-icon>
          Close
        </el-button>
      </div>
    </template>

    <div class="message-container">
      <el-scrollbar height="95%">

        <public-message v-for="message in thread"
                        :username="message.username"
                        :avatar="message.avatar"
                        :content="message.content"
                        :is_anonymous="message.is_anonymous"
        >
        </public-message>
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

      <div class="single-setting-container">
        <p>是否匿名（默认不匿名）</p>
        <el-switch v-model="is_anonymous"
                   style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949"
        >
        </el-switch>
      </div>

      <div class="respond-button-container">
        <el-button
            @click="submitPost(chatResponse);"
            type="primary"
            circle :icon="Message"
        >
        </el-button>
      </div>
    </div>
  </el-dialog>

</template>

<style scoped>
.my-header {
  display: flex;
  flex-direction: row;
  justify-content: right;
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