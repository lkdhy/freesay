<script setup lang="ts">
import AsideNavBar from "@/components/AsideNavBar.vue";
import Header from "@/components/Header.vue";
import IndexMain from "@/components/IndexMain.vue";

</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <Header></Header>
<!--        我是广场-->
      </el-header>
      <el-container>
        <el-aside width="200px">
          <AsideNavBar></AsideNavBar>
<!--          <p>我是侧边栏</p>-->
        </el-aside>

        <el-container>
          <el-main>

<!--            <index-main></index-main>-->
            <p>
              我们假设，用户登录后会跳转到满是提问箱的广场。
            </p>
            <router-view></router-view>
          </el-main>
        </el-container>

      </el-container>

    </el-container>
  </div>

</template>

<style scoped>

</style>