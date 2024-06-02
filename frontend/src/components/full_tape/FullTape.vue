<script setup lang="ts">
import {ref, watch} from "vue"
import {AnswerApi, UpdateThread} from "@/request/api";
import AvatarUsername from "../user/AvatarUsername.vue";
import {useRouter} from "vue-router";
import {useUserstore} from "@/store/user";
import {ElMessage, ElNotification as notify } from 'element-plus';
import AvatarMessageLeft  from "@/components/full_tape/AvatarMessageLeft.vue";
import AvatarMessageRight from "@/components/full_tape/AvatarMessageRight.vue";

const userStore = useUserstore()
const props = defineProps({
  id: Number,
  anonymous: Boolean,
  question: String,
  answer: String,
  tags: Array,
  host: String, poster: String,
  hostAvatar: String, posterAvatar: String,
  thread: Array<String>
})

const router = useRouter();

// 监听visible并emit给父组件，关闭完整Tape的这个对话框
const emit = defineEmits(['close'])
const visible = ref(true)
watch(visible, () => {
  emit('close')
})

const response = ref('')
const refresh = () => {
  let curPath = router.currentRoute.value.fullPath
  router.push('/empty').then(() => {
    router.replace(curPath)
  })
}

const thread_got = ref<Array<string>>(props.thread);
// if (props.thread) thread_got.value = props.thread
// console.log(thread_got.value)
console.log('length', thread_got.value.length)
const thread = ref<Array<Array<string>>>([])
if (thread_got.value && thread_got.value.length>0 && thread_got.value[thread_got.value.length-1].length===0)
  thread_got.value.pop()
// console.log('length', thread_got.value.length)
const real_len = thread_got.value.length
if (thread_got.value && thread_got.value.length%2===1) {
  thread_got.value.push('')
}
// console.log('length', thread_got.value.length)
if (thread_got.value && props.thread) {
  for (let i = 0; i < thread_got.value.length; i += 2) {
    thread.value.push([<string>thread_got.value[i], <string>thread_got.value[i+1]])
  }
  // console.log(thread)
}
// console.log('answer:', props.answer)
const can_answer =
    (userStore.userName===props.host && props.answer!=undefined && props.answer.length===0)
// console.log('lll', props.answer.length)
// console.log('lppp', can_answer)
// TODO: check this
const can_update_thread =
    (userStore.userName===props.host && props.thread!=undefined && real_len%2===1)
    || (userStore.userName===props.poster && props.thread!=undefined && props.answer && real_len%2===0)
// console.log('ghifhuiiorwnuiorwn')
// console.log('jjj',  (props.thread.length), (0)
//     || (userStore.userName===props.poster && props.thread && props.answer
//         && props.answer.length>0 && props.thread.length%2===0))
// console.log(props.thread?.length)
// console.log(props.thread)
const can_respond = ref(can_answer || can_update_thread)
const submitResponse = async (response: string) => {
  if (response.length === 0)
  {
    ElMessage.error('请输入！')
    return
  }
  if (can_answer) {
    const res = await AnswerApi({
      id: <number>props.id, // 类型断言
      answer: response,
      is_public: true,
    })
    if (res.success) {
      ElMessage({
        message: '已回复',
        type: 'success'
      });
      // TODO:
      // refresh()
    } else {
      console.log('WTF, 回复提问失败');
    }
  } else if (can_update_thread) {
    const res = await UpdateThread({
      id: <number>props.id,
      content: response,
    })
    if (res.success) {
      ElMessage({
        message: '已回复',
        type: 'success'
      });
    } else {
      console.log('WTF, 回复提问失败');
    }
  }
}
</script>

<template>
  <el-dialog v-model="visible"
  >
    <div class="full-tape-container">
      <div>
        <div class="tags-container">
          <el-tag v-for="tag in tags" round>
            {{ tag }}
          </el-tag>
        </div>
        <div class="question-container">
          <p>
            {{ question }}
          </p>
        </div>
        <el-divider content-position="right">
          <avatar-username
              v-if="!anonymous"
              :host-name="poster"
              :host-avatar="posterAvatar"
          >
          </avatar-username>
        </el-divider>
      </div>
      <div class="thread-container">
        <el-scrollbar
            height="300px"
        >
        <div class="answer-container"
             v-if="props.answer && props.answer.length > 0"
        >
          <avatar-message-left
              :avatar="hostAvatar"
              :message="answer"
          ></avatar-message-left>
        </div>
        <div v-for="conversation in thread">
          <avatar-message-right
              :anonymous="anonymous"
              :message="conversation[0]"
              :avatar="posterAvatar"
          ></avatar-message-right>
          <avatar-message-left
              v-if="conversation[1].length"
              :message="conversation[1]"
              :avatar="hostAvatar"
          ></avatar-message-left>

        </div>
        </el-scrollbar>
      </div>
<!--        <el-divider></el-divider>-->

    <div class="respond-area" v-if="can_respond">
      <el-input
          type="textarea"
          v-model="response"
      >

      </el-input>

      <el-button @click="submitResponse(response)" >
        回复
      </el-button>
    </div>
    </div>
  </el-dialog>

</template>

<style scoped>

.full-tape-container {
  display: flex;
  flex-direction: column;
  gap: 5px;
  min-height: 400px;
}
.question-container {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
}

</style>