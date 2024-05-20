<script setup lang="ts">
import {useRouter} from "vue-router";
// import Swiper core and required modules
import { Navigation, Pagination, Scrollbar, A11y } from "swiper/modules";
import { Mousewheel } from "swiper/modules"
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue';
// Import Swiper styles
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
// Import Swiper styles
const onSlideChange = () => {
  console.log('slide change');
};
const router = useRouter()
const jump2Login = () => { router.push('/login'); }
const jump2Register = () => { router.push('/register'); }
</script>

<template>
  <el-container style="position: absolute;">
    <el-header style="z-index: 100;">
      <div style="
          margin-top: 10px;
          display: flex;
          justify-content: right;
          align-items: center;"
      >
        <div>
          <el-button type="success" @click="jump2Login">
            登录
          </el-button>
          <el-button type="danger" @click="jump2Register">
            注册
          </el-button>
        </div>
      </div>
    </el-header>
    <el-main></el-main>
  </el-container>
    <section>
      <img class="hero"
           src="https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/c62efd51-f844-4335-ba29-70ea35521dd8"
           alt="我是英雄"
      />
      <swiper
          :modules="[Navigation, Pagination, Scrollbar, A11y, Mousewheel]"
          :slides-per-view="1"
          :loop="true"
          navigation
          :mousewheel="{ enabled: true }"
          :scrollbar="{ draggable: true }"
          :pagination="{ clickable: true }"
          @slideChange="onSlideChange"
          style="height: 100vh; display: flex; justify-content: center; align-items: center"
      >
        <swiper-slide>
          <h1 class="title one">Edinburgh</h1>
          <img class="img" src="https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/1bdebd02-d675-4469-be36-dc248448980d" alt="" />
        </swiper-slide>
        <swiper-slide>
          <h1 class="title two">复旦大学</h1>
          <img class="img" src="https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/c9a61071-c74d-4e8b-966a-6948cdbd9665" alt="" />
        </swiper-slide>
        <swiper-slide>
          <h1 class="title three">复旦大学江湾校区</h1>
        </swiper-slide>
        <swiper-slide v-slot="{ isActive }">
          <div>current slide is {{ isActive ? 'active' : 'inactive '}}</div>
          <div> {{ isActive }}</div>
        </swiper-slide>
      </swiper>
    </section>
</template>

<style scoped>
/* * {
  box-sizing: border-box;
  margin: 0; padding: 0;
} */
el-header {
  position: relative;
  z-index: 100;
}
section {
  position: relative;
  display: flex;
  justify-content: center;
  width: 100%;
  height: 100vh;
}
.hero {
  position: absolute;
  bottom: 0;
  max-width: 550px;
  z-index: 100;
}
.title {
  position: absolute;
  left: 50%; top: 18%;
  transform: translate(-50%, -50%);
  font-size: 5rem;
  letter-spacing: 0.3rem;
}
.swiper-slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
h1 {
  font-size: 100px;
}
</style>