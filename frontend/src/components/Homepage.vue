<script setup lang="ts">
import {onBeforeMount, reactive, ref} from "vue";
import {useRouter} from 'vue-router';
import {GetHostPostApi, GetPostApi} from "@/request/api";
import {useUserstore} from "@/store/user";
import PostDialog from "@/components/PostDialog.vue";
import UnansweredCard from "@/components/UnansweredCard.vue";
import PostCard from "@/components/user_box/PostCard.vue"
import FullTape from "@/components/full_tape/FullTape.vue";
import AvatarUsername from "@/components/user/AvatarUsername.vue";
// props
const props = defineProps({
})

const router = useRouter();
const userStore = useUserstore();
console.log(`当前访问用户是${userStore.visitedUserName}`);
console.log(`你是${userStore.userName}`);
interface GotPost {
  id: number
  asker_name: string
  asker_avatar: string
  is_anonymous: boolean
  is_public: boolean
  username: string
  question: string
  answer: string
  tags: string[]
  thread: string[]
}
const tapeData = ref<GotPost>({
  id: 0, asker_name: '', asker_avatar: '', is_anonymous: true,
  is_public: true, username: '', question: '',
  answer: '', tags: [], thread: []
})
const curUser = ref<string>(userStore.userName);
const visitedUser = ref<string>(userStore.visitedUserName);
console.log(`cur: ${curUser.value}, vised: ${visitedUser.value}`)
const isMine = curUser.value === visitedUser.value;
const p1 = ref<GotPost[]>([]);
const p2 = ref<GotPost[]>([]);
const p3 = ref<GotPost[]>([]);
const p4 = ref<GotPost[]>([]);
// console.log(isMine.value);

onBeforeMount(async () => {
  console.log('即将请求这个用户相关的帖子!')
  let res = await GetHostPostApi({
    username: visitedUser.value
  });
  console.log('这个用户的帖子请求结果：', res);
  if (res.success) {
    res.posts.forEach(post => {
      for (let tag of post.tags) {
        if (!relatedTags.value.includes(tag)) {
          console.log(tag)
          relatedTags.value.push(tag)
        }
      }
      if (!isMine) {
        if (post.answer.length
            && (post.is_public || post.username===curUser.value)) {
          p2.value.push(post);
        }
        console.log('p2:', p2.value);
      } else {
        if (!post.answer.length) {
          p1.value.push(post);
        } else {
          p2.value.push(post);
          console.log(post);
        }
      }
    })
  } else {
    console.log('WTF, host posts 请求失败')
  }
  if (!isMine) return
  let res2 = await GetPostApi({
    username: visitedUser.value
  });
  if (res2.success) {
    res2.posts.forEach(post => {
      if (post.answer.length) {
        p3.value.push(post);
      } else {
        p4.value.push(post);
      }
    })
  }
})

const handleCurrentChange = (post: GotPost) => {
  console.log('选中了这一行，其信息如下')
  console.log(post)
  tapeData.value = post
  fullTapeVisible.value = true
  console.log(tapeData.value)
}

const fullTapeVisible = ref(false)

const filterTag = (value: string, row: GotPost) => {
  return row.tags.includes(value)
}
const filterSetting = (value: boolean, row: GotPost) => {
  return row.is_public === value
}
const relatedTags = ref<string[]>([])
</script>

<template>
  <h2 v-if="isMine">我的主页</h2>
  <h2 v-else>{{ visitedUser }} 的主页</h2>
  <h3>
    你好 {{ curUser }}
  </h3>

  <full-tape
      v-if="fullTapeVisible"
      @close="fullTapeVisible = false"
      :id="tapeData.id"
      :anonymous="tapeData.is_anonymous"
      :public="tapeData.is_public"
      :question="tapeData.question"
      :answer="tapeData.answer"
      :tags="tapeData.tags"
      :host="visitedUser"
      :poster="tapeData.asker_name"
      :poster-avatar="tapeData.asker_avatar"
      host-avatar=''
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

  <post-dialog v-if="!isMine">
    <template v-slot:hostName>
      {{ $route.params.id }}
    </template>
  </post-dialog>

  <div>

    <el-tabs>
      <el-tab-pane label="未答" v-if="isMine">
        <!--            highlight-current-row-->
        <el-table
            :data="p1"
            @current-change="handleCurrentChange"
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
              :filters="relatedTags.map(tag => Object({
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
<!--        <el-scrollbar height="400px">-->
<!--          <div class="canvas">-->
<!--            <post-card v-for="post in p1"-->
<!--                       v-show="post.is_public"-->
<!--                       :host-name="visitedUser"-->
<!--                       :asker-name="post.asker_name"-->
<!--                       :anonymous="post.is_anonymous"-->
<!--                       :question="post.question"-->
<!--                       :answer="post.answer"-->
<!--                       :tags="post.tags"-->
<!--            >-->

<!--            </post-card>-->
<!--&lt;!&ndash;            <div v-for="post of p1">&ndash;&gt;-->
<!--&lt;!&ndash;              <unanswered-card&ndash;&gt;-->
<!--&lt;!&ndash;                  :post_id="post.id"&ndash;&gt;-->
<!--&lt;!&ndash;                  :question="post.question">&ndash;&gt;-->
<!--&lt;!&ndash;              </unanswered-card>&ndash;&gt;-->

<!--&lt;!&ndash;            </div>&ndash;&gt;-->

<!--          </div>-->
<!--        </el-scrollbar>-->
      </el-tab-pane>

      <el-tab-pane label="已答">
        <el-scrollbar height="400px">
          <div class="canvas">
            <div v-for="post of p2">
              <post-card
                  :post_id="post.id"
                  :question="post.question"
                  :answer="post.answer">
              </post-card>
            </div>
          </div>
        </el-scrollbar>
      </el-tab-pane>

      <el-tab-pane label="有回答" v-if="isMine">
        <el-scrollbar height="400px">
          <div class="canvas">
            <div v-for="post of p3">
              <post-card
                  :post_id="post.id"
                  :question="post.question"
                  :answer="post.answer"
                  :username="post.username">
              </post-card>
            </div>
          </div>
        </el-scrollbar>
      </el-tab-pane>

      <el-tab-pane label="未回答" v-if="isMine">
        <el-scrollbar height="400px">
          <div class="canvas">
            <div v-for="post of p4">
              <post-card
                  :post_id="post.id"
                  :question="post.question"
                  :answer="post.answer"
                  :username="post.username">
              </post-card>
            </div>
          </div>
        </el-scrollbar>
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