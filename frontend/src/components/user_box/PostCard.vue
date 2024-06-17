<script setup lang="ts">
import { ref } from "vue"
import AvatarUsername from "@/components/user/AvatarUsername.vue";
import FullTape from "@/components/full_tape/FullTape.vue";

// props
const props = defineProps({
  id: Number,
  hostName: String,
  hostAvatar: String,
  askerName: String,
  askerAvatar: String,
  anonymous: Boolean,
  question: String,
  answer: String,
  tags: Array<String>,
  thread: Array<String>,
})
const emit = defineEmits(['responded'])

const fullTapeVisible = ref(false)

</script>

<template>
  <div class="post-card-container">
    <el-tooltip content="点击查看">
      <el-card class="post-card"
               shadow="hover"
               @click="fullTapeVisible = true;"
      >
        <div class="tags-container">
          <el-tag v-for="tag in tags" round>
            {{ tag }}
          </el-tag>
        </div>
        <div class="post-card-content">
          <div class="question-container">
            <p style="word-break: break-all; text-align: center">
              {{ question }}
            </p>
          </div>
          <el-divider content-position="right">
            <avatar-username v-if="!anonymous"
                             :host-name="askerName"
                             :host-avatar="askerAvatar"
            >
            </avatar-username>
            <!--          <p v-else>匿名</p>-->
            <!--          <el-avatar size="small"></el-avatar>-->
          </el-divider>
          <div class="answer-container">
            <el-space>
              <el-avatar
                  :src="hostAvatar"
                  size="default"
              ></el-avatar>
              <p> {{ answer }}</p>
            </el-space>
          </div>
        </div>
      </el-card>

    </el-tooltip>

    <full-tape
        v-if="fullTapeVisible"
        @close="fullTapeVisible = false"
        @responded="console.log('userbox中有回复了'); emit('responded'); "
        :id="id"
        :anonymous = anonymous
        :question = question
        :answer = answer
        :tags="tags"
        :host = hostName
        :poster = askerName
        :poster-avatar="askerAvatar"
        :host-avatar="hostAvatar"
        :thread="thread"
    >

    </full-tape>
  </div>

</template>

<style scoped>
.post-card-container {
  margin-left: 50px;
  margin-bottom: 5px;
  margin-top: 5px;
  width: 350px;
}
.post-card {
  border-radius: 20px;
}
.post-card-content{
  height: 200px;
}
.question-container {
  height: 55%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.answer-container {
  height: 20%;
}
</style>