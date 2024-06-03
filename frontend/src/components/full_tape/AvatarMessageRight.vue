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
      <div class="avatar-container">
        <el-avatar v-if="anonymous"
                   src="https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png"
                   shape="square">
        </el-avatar>
        <el-avatar v-else :src="avatar" shape="square"></el-avatar>
      </div>
    </el-space>
  </div>

</template>

<style scoped>
.avatar-message-container {
  display: flex;
  justify-content: right;
  align-items: center;
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
  margin-right: 10px;
}

</style>