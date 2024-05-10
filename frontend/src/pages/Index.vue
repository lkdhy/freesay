<script setup lang="ts">
import AsideNavBar from "@/components/AsideNavBar.vue";
import Header from "@/components/Header.vue";
import IndexMain from "@/components/IndexMain.vue";

</script>

<template>
  <div class="common-layout">
<!--    <el-container style="height: 100%">-->
    <el-container>
      <el-header>
        <Header></Header>
<!--        我是广场-->
      </el-header>
      <el-container>
        <el-aside>
          <AsideNavBar></AsideNavBar>
<!--          <p>我是侧边栏</p>-->
        </el-aside>

        <el-container>
          <el-main>
<!--            <p>这里一开始是广场！！！！</p>-->
            <router-view></router-view>
          </el-main>
        </el-container>

      </el-container>

    </el-container>
  </div>

</template>

<style scoped>

</style>