<script setup lang="ts">
import { Swiper, SwiperSlide } from "swiper/vue";
import { Navigation, Pagination, Scrollbar, A11y, Mousewheel, Autoplay } from "swiper/modules";

const onSlideChange = () => {
  console.log('slide change!')
}
</script>

<template>
  <section>
  <swiper
      :modules="[Navigation, Pagination, Scrollbar, A11y, Mousewheel, Autoplay]"
      :slides-per-view="1"
      :loop="true"
      navigation
      :autoplay="{ delay: 5000 }"
      :mousewheel="{ enabled: true }"
      :scrollbar="{ draggable: true }"
      :pagination="{ clickable: true }"
      @slideChange="onSlideChange"
  >
    <swiper-slide>
      <img src="@/assets/FDU_images/bright/江湾湖岸.jpg" alt="江湾湖岸">
    </swiper-slide>
    <swiper-slide>
      <img src="@/assets/FDU_images/bright/菜地.jpg" alt="菜地"/>
    </swiper-slide>
    <swiper-slide>
      <img src="@/assets/FDU_images/dark/任重入口.jpg" alt="任重入口">
    </swiper-slide>
    <swiper-slide>
      <img src="@/assets/FDU_images/bright/三教自习.jpg" alt="三教"/>
    </swiper-slide>
    <swiper-slide>
      <img src="@/assets/FDU_images/dark/光草.jpg" alt="三教"/>
    </swiper-slide>
  </swiper>
  </section>
</template>

<style scoped>
section {
  position: absolute;
  display: flex;
  width: 100%;
  height: 100vh;
  z-index: -100;
}
.swiper-slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>