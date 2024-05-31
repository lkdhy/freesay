<script setup lang="ts">
import {onBeforeMount, reactive, ref} from "vue";
import {useRouter} from 'vue-router';
import {GetHostPostApi, GetPostApi} from "@/request/api";
import {useUserstore} from "@/store/user";
import PostDialog from "@/components/PostDialog.vue";
import FullTape from "@/components/full_tape/FullTape.vue";
import AvatarUsername from "@/components/user/AvatarUsername.vue";
import {ElTable} from "element-plus";
// props
const props = defineProps({
})

const router = useRouter();
const userStore = useUserstore();
interface GotPost {
  id: number
  asker_name: string
  asker_avatar: string
  is_anonymous: boolean
  is_public: boolean
  username: string
  user_avatar: string
  question: string
  answer: string
  tags: string[]
  thread: string[]
}
const tapeData = ref<GotPost>({
  id: 0, asker_name: '', asker_avatar: '', is_anonymous: true,
  is_public: true, username: '', user_avatar: '', question: '',
  answer: '', tags: [], thread: [],
})
const curUser = ref<string>(userStore.userName);
const visitedUser = ref<string>(userStore.visitedUserName);
console.log(`cur: ${curUser.value}, vised: ${visitedUser.value}`)
// const isMine = curUser.value === visitedUser.value;
const p1 = ref<GotPost[]>([]);
const p2 = ref<GotPost[]>([]);
// ---- 获取别人问自己的帖子 ----
// TODO: 用两个 loading
const loading = ref(true)

onBeforeMount(async () => {
  // ---- 获取别人问自己的帖子 ----
  let res = await GetHostPostApi({
    username: visitedUser.value
  });
  console.log('这个用户的帖子请求结果：', res);
  if (res.success) {
    res.posts.forEach(post => {
      for (let tag of post.tags) {
        if (!relatedTags1.value.includes(tag)) {
          relatedTags1.value.push(tag)
        }
      }
      p1.value.push(post);
      console.log(post);
    })
  } else {
    console.log('WTF, host posts 请求失败')
  }
  // ---- 获取别人问自己的帖子 ----
  // ---- 获取自己问别人的帖子 ----
  let res2 = await GetPostApi({
    username: visitedUser.value
  });
  if (res2.success) {
    res2.posts.forEach(post => {
      for (let tag of post.tags) {
        if (!relatedTags2.value.includes(tag)) {
          relatedTags2.value.push(tag)
        }
      }
      p2.value.push(post)
    })
    // ---- 获取自己问别人的帖子 ----
    loading.value = false
  }
})

const singleTableRef = ref<InstanceType<typeof ElTable>>()
const handleCurrentChange1 = (post: GotPost) => {
  // console.log('选中了这一行，其信息如下')
  // console.log(post)
  tapeData.value = post
  tapeData.value.username = userStore.userName
  tapeData.value.user_avatar = userStore.avatar
  fullTapeVisible.value = true
}
const handleCurrentChange2 = (post: GotPost) => {
  tapeData.value = post
  tapeData.value.asker_name = userStore.userName
  tapeData.value.asker_avatar = userStore.avatar
  fullTapeVisible.value = true
}

const fullTapeVisible = ref(false)

// ------ filters ------
const filterTag = (value: string, row: GotPost) => {
  return row.tags.includes(value)
}
const filterSetting = (value: boolean, row: GotPost) => {
  return row.is_public === value
}
const filterStatus = (value: boolean, row: GotPost) => {
  return (row.answer.length > 0) === value
}
// ------ filters ------

const relatedTags1 = ref<string[]>([])
const relatedTags2 = ref<string[]>([])
</script>

<template>
  <h2>我的主页</h2>
  <h3>
    你好 {{ curUser }}
  </h3>

  <full-tape
      v-if="fullTapeVisible"
      @close="
        fullTapeVisible = false;
      "
      :id="tapeData.id"
      :anonymous="tapeData.is_anonymous"
      :public="tapeData.is_public"
      :question="tapeData.question"
      :answer="tapeData.answer"
      :tags="tapeData.tags"
      :host="visitedUser"
      :poster="tapeData.asker_name"
      :poster-avatar="tapeData.asker_avatar"
      :host-avatar="tapeData.user_avatar"
  >
  </full-tape>

  <el-descriptions
      title="" border
  >
    <el-descriptions-item label="Username">
      {{ $route.params.id }}
    </el-descriptions-item>
    <el-descriptions-item label="个性签名">
        这个人很懒，什么都没有写
    </el-descriptions-item>
  </el-descriptions>

  <post-dialog>
    <template v-slot:hostName>
      {{ $route.params.id }}
    </template>
  </post-dialog>

  <div>

    <el-tabs v-loading="loading">
      <el-tab-pane label="TA问我的">
        <!--            highlight-current-row-->
        <el-table
            ref="singleTableRef"
            :data="p1"
            highlight-current-row
            @current-change="handleCurrentChange1"
            height="400"
        >
          <el-table-column label="From" width="200">
            <template #default="scope">
              <avatar-username v-if="!scope.row.is_anonymous"
                  :host-name="scope.row.asker_name"
                  :host-avatar="scope.row.asker_avatar"
              >
              </avatar-username>
              <el-avatar v-else shape="square">
                ?
              </el-avatar>
            </template>
          </el-table-column>
          <el-table-column label="Question" prop="question">
          </el-table-column>
          <el-table-column
              label="Tag"
              :filters="relatedTags1.map(tag => Object({
                text: tag, value: tag,
              }))"
              :filter-method="filterTag"
              filter-placement="top-end"
          >
            <template #default="scope">
              <el-space>
                <el-tag v-for="tag in scope.row.tags" round>
                  {{ tag }}
                </el-tag>
              </el-space>
            </template>
          </el-table-column>
          <el-table-column
              label="Status"
              :filters="[
                  { text: '已回答', value: true },
                  { text: '未回答', value: false },
              ]"
              :filter-method="filterStatus"
          >
            <template #default="scope">
              <el-tag v-if="scope.row.answer.length > 0">
                已回答
              </el-tag>
              <el-tag v-else>
                未回答
              </el-tag>
            </template>
          </el-table-column>
          <el-table-column
              label="Setting"
              :filters="[
                  { text: '公开', value: true },
                  { text: '私密', value: false },
              ]"
              :filter-method="filterSetting"
          >
            <template #default="scope">
              <div>
<!--                <el-tag v-if="scope.row.is_anonymous">匿名</el-tag>-->
<!--                <el-tag v-else>实名</el-tag>-->
                <el-tag v-if="scope.row.is_public">公开</el-tag>
                <el-tag v-else>私密</el-tag>
              </div>
            </template>
          </el-table-column>
        </el-table>
      </el-tab-pane>

      <el-tab-pane label="我问TA的">
        <el-table
            :data="p2"
            highlight-current-row
            @current-change="handleCurrentChange2"
            height="400"
        >
          <el-table-column label="To" width="200">
            <template #default="scope">
              <avatar-username
                  :host-name="scope.row.username"
                  :host-avatar="scope.row.user_avatar"
              >
              </avatar-username>
            </template>
          </el-table-column>
          <el-table-column label="Question" prop="question">
          </el-table-column>
          <el-table-column
              label="Tag" width="200"
              :filters="relatedTags2.map(tag => Object({
                text: tag, value: tag,
              }))"
              :filter-method="filterTag"
              filter-placement="top-end"
          >
            <template #default="scope">
              <el-space>
                <el-tag v-for="tag in scope.row.tags" round>
                  {{ tag }}
                </el-tag>
              </el-space>
            </template>
          </el-table-column>
          <el-table-column
              label="Status" width="150"
              :filters="[
                  { text: '已回答', value: true },
                  { text: '未回答', value: false },
              ]"
              :filter-method="filterStatus"
          >
            <template #default="scope">
              <el-tag v-if="scope.row.answer.length > 0">
                已回答
              </el-tag>
              <el-tag v-else>
                未回答
              </el-tag>
            </template>
          </el-table-column>
          <el-table-column
              label="Setting"
              :filters="[
                  { text: '公开', value: true },
                  { text: '私密', value: false },
              ]"
              :filter-method="filterSetting"
          >
            <template #default="scope">
              <div>
                <el-tag v-if="scope.row.is_public">公开</el-tag>
                <el-tag v-else>私密</el-tag>
              </div>
            </template>
          </el-table-column>
        </el-table>
      </el-tab-pane>
    </el-tabs>
  </div>

</template>

<style scoped>
/* TODO */
.canvas {
  display: flex;
  flex-wrap: wrap;
}
</style>