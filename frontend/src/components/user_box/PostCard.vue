<script setup lang="ts">
import AvatarUsername from "@/components/user/AvatarUsername.vue";
// props
const props = defineProps({
  hostName: String,
  askerName: String,
  anonymous: Boolean,
  question: String,
  answer: String,
})

</script>

<template>
  <div class="post-card-container">
    <el-card class="post-card">
<!--      <template #header>-->
<!--        <div class="flex gap-2">-->
<!--        </div>-->
<!--      </template>-->
      <div class="tags-container">
        <el-tag type="primary">恋爱</el-tag>
        <el-tag type="success">学习</el-tag>
      </div>
      <div class="post-card-content">
        <div class="question-container">
          <p style="word-break: break-all; text-align: center">
            {{ question }}
          </p>
        </div>
        <el-divider content-position="right">
          <avatar-username v-if="!anonymous"
                           :host-name="askerName">
          </avatar-username>
<!--          <p v-else>匿名</p>-->
<!--          <el-avatar size="small"></el-avatar>-->
        </el-divider>
        <div class="anwser-container">
          <el-space>
            <el-avatar size="default"></el-avatar>
            <p> {{ answer }}</p>
          </el-space>
        </div>
      </div>
    </el-card>
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
.post-card-content {
  height: 200px;
}
.question-container {
  height: 60%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.anwser-container {
  height: 20%;

}
</style>