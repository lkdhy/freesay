<script setup lang="ts">
import AvatarUsername from "@/components/user/AvatarUsername.vue";

const props = defineProps({
  is_anonymous: Boolean,
  username: String, avatar: String, content: String,
})

</script>

<template>
  <div class="chat-message-container">
    <el-space size="small">
      <avatar-username
          v-if="!is_anonymous"
          :host-avatar="avatar" :host-name="username">
      </avatar-username>
      <el-avatar v-else
                 src="https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png"
      >
      </el-avatar>
      <el-divider
          direction="horizontal" border-style="solid"
      ></el-divider>
      <p class="message-content">{{ content }}</p>
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