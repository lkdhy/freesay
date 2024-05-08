<script setup lang="ts">
import {useRouter} from 'vue-router';
// import {useUserstore} from "@/store/user";

// const userStore=useUserstore();
const router = useRouter();

const jump2Login = () => {
  router.push('/login');
}
const jump2Register = () => {
  router.push('/register');
}
</script>

<template>
    <el-container>
      <el-header>
        <div style="
          display: flex;
          justify-content: space-between;
          align-items: center;"
        >
          <div>
            <img src="https://img2.imgtp.com/2024/04/05/DMHKG7pg.jpg"
                 alt="Logo" style="height: 50px;">
            <img src="@/assets/icons/chat-icon.svg"
                 alt="Logo" style="height: 40px;">
            <p>FDU Tape</p>
          </div>

          <div>
            <el-button type="success" @click="jump2Login">
              登录
            </el-button>
            <el-button type="danger" @click="jump2Register">
              注册
            </el-button>
          </div>
        </div>

        <el-main>
          <h1>
            欢迎！
          </h1>
          <h2>
            我是还没登陆的地方，我是 /index 哦~
          </h2>
          <p>
            请右上角点击登录 / 注册吧
          </p>
        </el-main>
      </el-header>
    </el-container>
</template>

<style scoped>

</style>