<script setup lang="ts">
import {useRouter} from 'vue-router';
import {useUserstore} from "@/store/user";
import BackgroundSwiper from "@/components/BackgroundSwiper.vue";

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
          <img src="@/assets/icons/freesay-icon_FDU.svg"/>
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
        <h2 class="title two">
          复旦大学 <span class="freesay">freesay</span> 提问箱
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
    <background-swiper></background-swiper>
  </el-container>
</template>

<style scoped>
.desc {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.title {
  opacity: 95%;
  font-size: 90px;
  margin-top: 40px;
  margin-bottom: 175px;
  color: transparent;
  /* letter-spacing: 0.1rem; */
  background-position: 0 0;
  animation: animated-text 20s linear infinite;
}
@keyframes animated-text {
  100% {
    background-position: 200% 0;
  }
}
.one {
  -webkit-text-stroke: 1px rgba(16, 104, 31, 0.8);
  background: url(
  https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/e9d06cb6-2844-49ed-9bde-23d3364b9fa4);
  background-clip: text;
  -webkit-background-clip: text;
}
.two {
  -webkit-text-stroke: 1px yellow;
  -webkit-text-stroke: 1px #fff;
  background: url(
  https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/ba4edde6-822d-437a-88c2-f54392d7a56f);
  background-clip: text;
  -webkit-background-clip: text;
}
.poem {
  opacity: 90%;
  font-size: 30px;
  /* font-family: 华文中宋; */
  margin-top: 10px;
  color: yellow;
}
.loginTip {
  margin-top: 150px;
  color: white;
}
.Icons > * {
  /* margin-right: 10px; */
  margin-top: 5px;
  max-height: 45px;
}

</style>
