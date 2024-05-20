<script setup lang="ts">
import {useRouter} from 'vue-router';
import {useUserstore} from "@/store/user";
// import { jump2Login } from "@/utils/common"

const userStore=useUserstore();
const router = useRouter();

console.log('欢迎页：', router.currentRoute.value);
// console.log('【学习用】router的值：', router);
console.log('currentRoute 的 name：', router.currentRoute.value.name)
console.log('fullPath:', router.currentRoute.value.fullPath)

// 现在下面可认为没用
if (userStore.userName.length) {
  console.log('用户登录了，故应跳转到广场')
}

const refresh = () => {
  let curPath = router.currentRoute.value.fullPath
  router.push('/empty').then(() => {
  router.replace(curPath)
  })
}
const jump2Login = () => { router.push('login') }
const jump2Register = () => { router.push('/register'); }
</script>

<template>
    <el-container>
      <el-header>
        <div style="
          display: flex;
          justify-content: space-between;
          align-items: center;"
        >
          <div class="Icons">
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

        <el-main class="desc">
          <h2 class="title">
            复旦大学 Tape 匿名提问箱
          </h2>
          <h3 class="poem">
            卿云烂兮，乣缦缦兮
          </h3>
          <h3 class="poem">
            日月光华，旦复旦兮
          </h3>
          <p class="loginTip">
            （右上角点击登录 / 注册）
          </p>
        </el-main>
      </el-header>
    </el-container>
</template>

<style scoped>
.desc {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.title {
  font-size: 60px;
  margin-bottom: 100px;
  font-family: 华文细黑;
}
.poem {
  font-size: 30px;
  font-family: 华文中宋;
  margin-bottom: 10px;
}
.loginTip {
  margin-top: 100px;
}
/*
.Icons {
  display: flex;
  flex-direction: row;
  align-items: center;
}
 */
.Icons > * {
  margin-right: 10px;
}

</style>