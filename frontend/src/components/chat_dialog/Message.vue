<script setup lang="ts">
const props = defineProps({
  avatar: String, message: String, fromSelf: Boolean,
})

</script>

<template>
  <div class="message-container">
    <el-space v-if="fromSelf" size="large">
      <div class="avatar-container">
        <el-avatar :src="avatar" shape="square"></el-avatar>
      </div>
      <p class="message-content">{{ message }}</p>
    </el-space>
    <el-space v-else>
      <p class="message-content">{{ message }}</p>
      <div class="avatar-container">
        <el-avatar :src="avatar" shape="square"></el-avatar>
      </div>
    </el-space>
  </div>
</template>

<style scoped>
.message-container {
  display: flex;
  justify-content: right;
  align-items: center;
  width: 90%;
  border: 1px solid #ebeef5;
  /*
  height: 50px;
  margin: 9px;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
   */
}
.message-content {
  font-size: 20px;
}
.avatar-container {
  margin-right: 10px;
}
</style>