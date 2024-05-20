<script setup lang="ts">
import AsideNavBar from "@/components/AsideNavBar.vue";
import Header from "@/components/Header.vue";
import {useUserstore} from "@/store/user";
import {useRouter} from "vue-router";

const router = useRouter();
const userStore = useUserstore();

// 如果直接访问 “http://localhost:5173/”，则会跳到欢迎页 “http://localhost:5173/index”
if (!userStore.userName.length) {
  router.replace('/index');
}

</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <Header></Header>
      </el-header>
      <el-container>
        <el-aside width="12%">
          <AsideNavBar></AsideNavBar>
        </el-aside>

        <el-container>
          <el-main>
            <router-view></router-view>
          </el-main>
        </el-container>

      </el-container>

    </el-container>
  </div>

</template>

<style scoped>

</style>