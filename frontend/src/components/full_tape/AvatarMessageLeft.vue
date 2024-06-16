<script setup lang="ts">
const props = defineProps({
  avatar: String,
  message: String,
})

</script>

<template>
  <div class="avatar-message-container">
    <el-space size="large">
      <div class="avatar-container">
        <el-avatar :src="avatar" shape="square"></el-avatar>
      </div>
      <p class="message-container">{{ message }}</p>
    </el-space>
  </div>

</template>

<style scoped>
.avatar-message-container {
  display: flex;
  justify-content: left;
  align-items: center;
  /*
  width: 70%;
  border: 1px solid #ebeef5;
  */
  height: 50px;
  margin: 9px;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
}
.message-container {
  text-align: center;
  font-size: 15px;
}
.avatar-container {
  margin-left: 10px;
}

</style>