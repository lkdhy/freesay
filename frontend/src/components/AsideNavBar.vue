<script setup lang="ts">
import {
  Document, Menu as IconMenu, Setting,
} from '@element-plus/icons-vue';
import {useRouter} from 'vue-router';

const router = useRouter();

function change(key: string, keyPath: string[]) {
  console.log(key);
}

</script>

<template>
  <el-menu
      default-active="1"
      class="el-menu-vertical-demo"
      :router=true
  >

    <el-menu-item index="/plaza">

      <span>点我去往广场</span>
    </el-menu-item>

    <el-menu-item index="/user">
      <span>用户</span>
    </el-menu-item>

    <el-menu-item index="/userList">
      <el-icon><document/></el-icon>
      <span>查看所有用户</span>
    </el-menu-item>

    <el-menu-item index="profile">
      <span>（我认为不需要这条）你的 profile</span>
    </el-menu-item>

    <el-menu-item index="/test">

      <span>点我去往 Test</span>
    </el-menu-item>

<!--    <el-menu-item index="/index/">-->
<!--      <el-icon><icon-menu/></el-icon>-->
<!--      <span>我不知道这是什么</span>-->
<!--    </el-menu-item>-->

    <el-menu-item index="/addUser">
      <el-icon><setting/></el-icon>
      <span>（我暂时没用）添加用户</span>
    </el-menu-item>

  </el-menu>
</template>

<style scoped>

</style>