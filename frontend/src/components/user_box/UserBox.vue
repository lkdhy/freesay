<script setup lang="ts">
import PostCard from "@/components/user_box/PostCard.vue";
import {ref} from "vue";
import {useRouter} from "vue-router";
import {useUserstore} from "@/store/user";
import {onBeforeMount} from "vue";
import {GetHostPostApi} from "@/request/api";

const router = useRouter()
const visitedUser = router.currentRoute.value.params.username

interface GotPost {
  id: number, username: string,
  is_anonymous: boolean
  is_public: boolean
  question: string, answer: string
}
const posts = ref<GotPost[]>([])

const fetchUserInfo = async () => {

}

onBeforeMount(async () => {
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

  const host_st_res = await GetHostPostApi({
    username: <string>visitedUser
  })
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
      <div class="post-card-container">
        <el-scrollbar height="500px">
            <el-space
                size="large"
                wrap
            >
<!--              <post-card v-for="i in [1,2,3,4,5,6,7,8,9,1,1,1,1,1,1,1,1,1,1,1,1]">-->

<!--              </post-card>-->
              <post-card v-for="post in posts"
                         :host-name="visitedUser"
                         asker-name="TODO"
                         :anonymous="'is_anonymous' in post ?  post.is_anonymous : true"
                         :question="post.question"
                         :answer="post.answer"
              >

              </post-card>
            </el-space>
        </el-scrollbar>
      </div>
      </div>
    <div class="right">
      <el-avatar size="large" shape="square">
      </el-avatar>
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
.post-card-container {
  margin-top: 1px;
}
</style>