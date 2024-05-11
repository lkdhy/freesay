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

        <el-main class="tmp">
          <h1>
            欢迎来到复旦大学 Tape 提问箱
          </h1>
          <h3>
            卿云烂兮，乣缦缦兮
          </h3>
          <h3>
            日月光华，旦复旦兮
          </h3>
          <p>
            请在右上角点击登录 / 注册
          </p>
        </el-main>
      </el-header>
    </el-container>
</template>

<style scoped>
.tmp {
  display: flex;
  flex-direction: column;
}
* {
  margin-bottom: 30px;
  margin-left: 10px;
}
</style>