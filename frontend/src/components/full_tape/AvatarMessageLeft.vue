<script setup lang="ts">
const props = defineProps({
  avatar: String,
  message: String,
})

</script>

<template>
  <div class="avatar-message-container">
    <el-space size="large">
      <el-avatar :src="avatar"></el-avatar>
      <p class="message-container">{{ message }}</p>
    </el-space>
  </div>

</template>

<style scoped>
.avatar-message-container {
  display: flex;
  justify-content: left;
  align-items: center;
  height: 50px;
  margin: 10px;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
}
.message-container {
  text-align: center;
  font-size: 15px;
}

</style>