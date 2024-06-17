<script setup lang="ts">
import {
  User, Compass, View, ChatLineRound
} from '@element-plus/icons-vue';
import {useRouter} from 'vue-router';

const router = useRouter();

</script>

<template>
<!--  background-color="orchid"-->
<!--  设置活动菜单项同其它颜色-->
  <el-menu
      default-active="1"
      class="el-menu-vertical-demo"
      active-text-color="#303133"
      :router=true
  >

    <el-menu-item index="/plaza">
      <el-icon><Compass /></el-icon>
      <span style="text-align: center;">去往广场</span>
    </el-menu-item>

<!--    <el-menu-item index="/user">-->
<!--      <span>用户</span>-->
<!--    </el-menu-item>-->

<!--    <el-menu-item index="/userList">-->
<!--      <el-icon><User /></el-icon>-->
<!--      <span>看看有谁！</span>-->
<!--    </el-menu-item>-->

    <el-menu-item index="/publicBox">
      <el-icon><View /></el-icon>
      <span>表白墙</span>
    </el-menu-item>

<!--    <el-menu-item index="/">-->
<!--      <el-icon><ChatLineRound /></el-icon>-->
<!--      <span>我的聊天</span>-->
<!--    </el-menu-item>-->
<!--    <el-menu-item index="profile">-->
<!--      <span>（我认为不需要这条）你的 profile</span>-->
<!--    </el-menu-item>-->

<!--    <el-menu-item index="/test">-->

<!--      <span>点我去往 Test</span>-->
<!--    </el-menu-item>-->

<!--    <el-menu-item index="/index/">-->
<!--      <el-icon><icon-menu/></el-icon>-->
<!--      <span>我不知道这是什么</span>-->
<!--    </el-menu-item>-->

<!--    <el-menu-item index="/addUser">-->
<!--      <el-icon><setting/></el-icon>-->
<!--      <span>（我暂时没用）添加用户</span>-->
<!--    </el-menu-item>-->

  </el-menu>
</template>

<style scoped>

</style>