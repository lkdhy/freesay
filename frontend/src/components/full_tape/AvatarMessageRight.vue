<script setup lang="ts">
const props = defineProps({
  anonymous: Boolean,
  avatar: String,
  message: String,
})

</script>

<template>
  <div class="avatar-message-container">
    <el-space size="large">
      <p class="message-container">{{ message }}</p>
      <el-avatar v-if="anonymous">
        ?
      </el-avatar>
      <el-avatar v-else :src="avatar"></el-avatar>
    </el-space>
  </div>

</template>

<style scoped>
.avatar-message-container {
  display: flex;
  justify-content: right;
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