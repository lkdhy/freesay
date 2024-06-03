<script setup lang="ts">
import { useUserstore } from "@/store/user";
import {onBeforeMount, onMounted, ref} from "vue"
import { PostApi, GetTags } from "@/request/api";
import {ElMessage} from "element-plus";

const userStore = useUserstore()
// props
const props = defineProps({
  hostName: String
})

const submitQuestion = async (question: string) => {
  if (question.length === 0) return
  // console.log('准备 post 帖子');
  const res = await PostApi({
    username: userStore.userName,
    hostUsername: <string>props.hostName,
    question: question,
    is_public: is_public.value,
    is_anonymous: is_anonymous.value,
    tags: selected_tags.value
  })
  // console.log('post结果', res);
  if (res.success) {
    console.log('post表单提交成功');
    ElMessage({
      message: '已向TA发送提问', type: 'success'
    });
  } else {
    console.log('WTF');
    ElMessage({
      message: '出错了！', type: 'success'
    });
  }
}

onBeforeMount(async () => {
  console.log('我是post-dialog')
})
const visible = ref(false)
const question = ref('')
const is_public = ref(true)
const is_anonymous = ref(true)
// as to tags
const selected_tags = ref<string[]>([])
const tag_options = ref([
  { tag: '恋爱', label: '恋爱' },
  { tag: '学习', label: '学习' },
  { tag: '动漫', label: '动漫' },
])

// 14 个推荐问题
let ref_questions = [
    '你现在是单身吗？',
    '你谈过几段恋爱？',
    '最喜欢玩什么游戏？',
    '最喜欢吃什么？',
    '新番里面有你喜欢的动漫吗？',
    '可以推荐一本你喜欢的书吗？',
    '对于不喜欢的人，你会如何对待？',
    '喜欢看什么类型的电影？',
    '感到压力大的时候，你一般怎么缓解？',
    '看不看足球？喜欢哪个球队？',
    '可以推荐一首你喜欢的歌吗？',
    '你觉得分手后还能做朋友吗？',
    '哪件事情让你觉得你是人间值得的？'
]
// 随机打乱
ref_questions.sort((a, b) => {
  return Math.random() < 0.5 ? 1 : -1
})

const getExistingTags = async () => {
  const res = await GetTags()
  if (res.success) {
    console.log(res.message)
    tag_options.value = res.tags.map(tag => ({ tag: tag, label: tag }))
    console.log(tag_options.value)
  } else {
    console.log('WTF, 现有标签请求失败')
  }
}
</script>

<template>
  <h4 @click="visible=true">
    点击此处向我提问
  </h4>

  <el-dialog
      v-model="visible"
      show-close
      draggable
      class="post-dialog"
  >
    <template #header>
      <div class="my-header">
        <h3>
          向 {{ hostName }} 提问
        </h3>
      </div>
    </template>

    <div class="question-editing-container">
<!--      <el-popover>-->
<!--      用 el-dropdown 而不是 el-popover-->
      <el-dropdown size="large">
<!--        <template #reference>-->
          <el-input
              v-model="question"
              type="textarea"
              :autosize="{ minRows: 5 }"
              placeholder="你想对TA说……"
              maxlength="150"
              show-word-limit
              size="large"
              class="input-question-area"
          >
          </el-input>
<!--        </template>-->

        <template #dropdown>
          <el-scrollbar height="300px">
            <el-dropdown-item
                v-for="ref_question of ref_questions"
                @click="question = ref_question"
            >
              <p class="reference-question">{{ ref_question }}</p>
            </el-dropdown-item>
          </el-scrollbar>
        </template>
      </el-dropdown>
<!--      </el-popover>-->

    </div>

    <div class="tag-select-container">
      <el-select
          @focus="getExistingTags"
          v-model="selected_tags"
          multiple
          filterable
          allow-create
          default-first-option
          :reserve-keyword="false"
          placeholder="选择标签，可以输入新增标签"
          style="width: 400px; margin-right: 30px"
      >
        <el-option
            v-for="tag in tag_options"
            :key="tag.tag"
            :label="tag.label"
            :value="tag.tag"
        />

        <template #tag>
          <el-tag v-for="tag in selected_tags"
                  :key="tag"
                  round
          >
            {{ tag }}
          </el-tag>
        </template>
      </el-select>
    </div>

    <div class="post-settings-container">
      <div class="single-setting-container">
        <p>是否匿名</p>
        <el-switch v-model="is_anonymous"
                   style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949"
        >
        </el-switch>
      </div>

      <div class="single-setting-container">
        <p>是否公开</p>
        <el-switch v-model="is_public">
        </el-switch>
      </div>
    </div>

    <template #footer>
      <div class="my-footer">
        <el-button
            type="primary"
            @click="submitQuestion(question); visible = false"
            style="margin-right: 10px; mar-bottom: 10px;"
        >
          发送提问
        </el-button>
      </div>
    </template>
  </el-dialog>

</template>

<style scoped>
.post-dialog {
  height: 600px;
}
.question-editing-container {
  display: flex;
  justify-content: center;
}
.tag-select-container {
  margin: 20px;
  display: flex;
  justify-content: right;
  gap: 50px;
}
.input-question-area {
  font-size: 20px;
  width: 400px;
  text-align: center;
}
.reference-question {
  margin-bottom: 1px;
  font-size: 16px;
}
.post-settings-container {
  font-size: 17px;
  margin-left: 40px;
}
.single-setting-container {
  margin-bottom: 8px;
}

</style>