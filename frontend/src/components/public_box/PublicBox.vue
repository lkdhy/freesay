<script setup lang="ts">
import PublicCard from "@/components/public_box/PublicCard.vue";
import {useRouter} from "vue-router";
import {ref, reactive, watch, onBeforeMount} from "vue";
import {GetPublicApi} from "@/request/api";
import {ElMessage} from "element-plus";

const loading = ref(false)
interface public_thread {
  username: string
  avatar: string
  is_anonymous: boolean
  content: string
}
interface GotPublic {
  pid: number
  username: string
  avatar: string
  is_anonymous: boolean
  content: string
  thread: public_thread[]
}
const public_posts = ref<GotPublic[]>([])
const fetchPublicPosts = async () => {
  loading.value = true
  const res = await GetPublicApi()
  if (res.success) {
    public_posts.value = res.posts
    loading.value = false
    // ElMessage( {
    //     message: '公开贴请求成功',
    //     type: 'success'
    //   }
    // )
    // console.log(res.message)
    // console.log(res.posts)
    console.log(public_posts.value)
  } else {
    console.log('公开贴请求失败')
  }
}

onBeforeMount(fetchPublicPosts)

</script>

<template>
  <h2 style="text-align: center; margin-bottom: 1em">
    广场
  </h2>
  <div class="public-card-container"
       v-loading="loading"
  >
    <el-scrollbar height="500px">
      <el-space size="large" wrap>
        <public-card v-for="post in public_posts"
                     @responded="fetchPublicPosts"
                     :pid="post.pid"
                      :username="post.username"
                      :avatar="post.avatar"
                      :is_anonymous="post.is_anonymous"
                      :content="post.content"
                      :thread="post.thread"
        >
        </public-card>
      </el-space>
    </el-scrollbar>
  </div>
</template>

<style scoped>

</style>