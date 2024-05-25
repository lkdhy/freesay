<script setup lang="ts">
import PostCard from "@/components/user_box/PostCard.vue";

</script>

<template>
  <el-space
      size="large"
      alignment="start"
  >
    <div class="main">
      <p>llllllllllllllll</p>
      <div class="post-card-container">
        <el-scrollbar height="500px">
          <el-space
              size="large"
              wrap
          >
            <post-card v-for="i in [1,2,3,4,5,6,7,8,9,1,1,1,1,1,1,1,1,1,1,1,1]">

            </post-card>
          </el-space>
        </el-scrollbar>
      </div>
    </div>
    <div class="right">
      <el-avatar size="large" shape="square">
      </el-avatar>
    </div>
  </el-space>
</template>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 1000px;
  border: blue 2px solid;
}
.right {
  width: 200px;
  border: orange 4px solid;
}
.post-card-container {
  margin-top: 50px;
}
</style>