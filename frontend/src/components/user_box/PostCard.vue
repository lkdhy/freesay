<script setup lang="ts">
import AvatarUsername from "@/components/user/AvatarUsername.vue";
// props
const props = defineProps({
  hostName: String
})

</script>

<template>
  <div class="post-card-container">
    <el-card class="post-card">
      <div class="post-card-content">
        <div class="question-container">
          <p style="word-break: break-all; text-align: center">
            感到压力大的时候，你一般怎么缓解？
          </p>
        </div>
        <el-divider content-position="right">
          <avatar-username host-name="username"></avatar-username>
<!--          <el-avatar size="small"></el-avatar>-->
        </el-divider>
        <div class="anwser-container">
          <el-space>
            <el-avatar size="default"></el-avatar>
            <p>我是回答</p>
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
  height: 300px;
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