<script setup lang="ts">
const props = defineProps({
  avatar: String, message: String, fromSelf: Boolean,
})

</script>

<template>
  <div v-if="fromSelf" class="chat-message-container"
       style="justify-content: right"
  >
    <el-space size="small">
      <p class="message-content">{{ message }}</p>
      <div class="avatar-container">
        <el-avatar :src="avatar" shape="square"></el-avatar>
      </div>
    </el-space>
  </div>
  <div v-else class="chat-message-container"
  >
    <el-space size="small">
      <div class="avatar-container">
        <el-avatar :src="avatar" shape="square"></el-avatar>
      </div>
      <p class="message-content">{{ message }}</p>
    </el-space>
  </div>
</template>

<style scoped>
.chat-message-container {
  display: flex;
  flex-direction: row;
  justify-content: left;
  align-items: center;
  width: 97%;
  /* border: 1px solid #ebeef5; */
  margin-top: 5px;
  /*background: var(--el-color-primary-light-9); color: var(--el-color-primary);
  height: 50px;
  margin: 9px;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
   */
}
.message-content {
  text-align: center;
  font-size: 20px;
}
.avatar-container {
  /* margin-right: 10px; */
}
</style>