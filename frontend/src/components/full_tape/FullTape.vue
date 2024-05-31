<script setup lang="ts">
import {ref, watch} from "vue"
import {AnswerApi, UpdateThread} from "@/request/api";
import AvatarUsername from "../user/AvatarUsername.vue";
import {useRouter} from "vue-router";
import {ElMessage, ElNotification as notify } from 'element-plus';

const props = defineProps({
  id: Number,
  anonymous: Boolean,
  public: Boolean,
  question: String,
  answer: String,
  tags: [String],
  host: String, poster: String,
  hostAvatar: String, posterAvatar: String,
  thread: [String]
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

const submitResponse = async (response: string) => {
  if (response.length === 0)
  {
    ElMessage.error('请输入！')
    return
  }
  if (1 > 0) {
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
  } else {
    const res = await UpdateThread({
      id: <number>props.id,
      tid: 0, // TODO
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
    <div class="full-tape-container"
    >
    <el-card>
      <div class="tags-container">
        <el-tag v-for="tag in tags">
          {{ tag }}
        </el-tag>
      </div>

      <div>
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
        <div class="anwser-container">
          <el-space>
            <el-avatar :src="hostAvatar">
            </el-avatar>
            <p> {{ answer }} </p>
          </el-space>
        </div>
        <el-divider></el-divider>
        <div>
          [TODO] 这里是 thread（若有）
        </div>
      </div>
    </el-card>

    <div class="respond-area">
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
  gap: 10px;
  min-height: 400px;
}
.question-container {
  display: flex;
  align-items: center;
  justify-content: center;
}


</style>