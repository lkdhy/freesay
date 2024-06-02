<script setup lang="ts">
import PostCard from "@/components/user_box/PostCard.vue";
import {ref, reactive} from "vue";
import {useRouter} from "vue-router";
import {useUserstore} from "@/store/user";
import {onBeforeMount} from "vue";
import { GetUserInfo, GetHostPostApi} from "@/request/api";
import UserInfo from "@/components/user_box/UserInfo.vue";
import PostDialog from "@/components/user_box/PostDialog.vue";

const router = useRouter()
const visitedUser = router.currentRoute.value.params.username

interface GotPost {
  id: number, username: string
  asker_name: string
  asker_avatar: string
  is_anonymous: boolean
  is_public: boolean
  question: string, answer: string
  tags: string[]
  thread: string[]
}
interface GotUserInfo {
  username: string,
  avatar: string,
  email: string,
  signature: string
}
const userInfo = ref<GotUserInfo>({
  username: '', email: '', signature: '', avatar: ''
})
const posts = ref<GotPost[]>([])

const fetchUserInfo = async () => {
  console.log(`即将请求${visitedUser}的个人信息`)
  const user_info_res = await GetUserInfo({
    username: <string>visitedUser
  })
  console.log(`${visitedUser}的个人信息请求结果：`, user_info_res)
  if (user_info_res.success) {
    userInfo.value = user_info_res.userinfo
  } else {
    console.log('WTF，用户个人信息请求失败')
  }
}

onBeforeMount(async () => {
  await fetchUserInfo()
  console.log(`即将请求${visitedUser}的所有公开已答帖子`)
  const host_post_res = await GetHostPostApi({
    username: <string>visitedUser
  })
  console.log('在这个用户的公开已答帖子请求结果：', host_post_res)
  if (host_post_res.success) {
    host_post_res.posts.forEach(post => {
      if (post.answer.length) {
        posts.value.push(post)
      }
    })
    console.log(posts.value)
  } else {
    console.log('WTF, host posts 请求失败')
  }
})
</script>

<template>
  <el-space
      size="large"
      alignment="start"
  >
    <div class="main">
      <div class="description-container">

      </div>

      <div class="operation-container">
        <post-dialog :host-name="visitedUser"></post-dialog>
      </div>

      <div class="post-card-container">
        <el-scrollbar height="500px">
            <el-space
                size="large"
                wrap
            >
              <post-card v-for="post in posts"
                         v-show="post.is_public"
                         :id="post.id"
                         :host-name="visitedUser"
                         :host-avatar="userInfo.avatar"
                         :asker-name="post.asker_name"
                         :asker-avatar="post.asker_avatar"
                         :anonymous="post.is_anonymous"
                         :question="post.question"
                         :answer="post.answer"
                         :tags="post.tags"
                         :thread="post.thread"
              >
              </post-card>
            </el-space>
        </el-scrollbar>
      </div>
      </div>
    <div class="right">
      <user-info
          :username="userInfo.username"
          :avatar="userInfo.avatar"
          :email="userInfo.email"
          :signature="userInfo.signature"
      >

      </user-info>
    </div>
  </el-space>
</template>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 1000px;
  border: blue 2px solid;
}
.right {
  width: 200px;
  border: orange 4px solid;
}
.description-container {
  height: 200px;
}
.operation-container {
  margin: 10px
}
.post-card-container {
  margin-top: 1px;
}
</style>