<script setup lang="ts">
import LoginForm from "@/components/LoginForm.vue";
import Pacts2 from "@/pages/Pacts2.vue";
import ColorfulBubblesParticles from "@/components/Particles/ColorfulBubblesParticles.vue";
</script>

<template>

  <div class="container">
    <header id="welcomeTitle">
      <h1>欢迎来到复旦大学提问箱</h1>
    </header>

    <div class="background">
      <LoginForm class="form-container"></LoginForm>
    </div>

<!--    <pacts2></pacts2>-->
    <colorful-bubbles-particles></colorful-bubbles-particles>

<!--    <div class="background">-->
<!--      <LoginForm class="form-container"></LoginForm>-->
<!--    </div>-->

  </div>
</template>

<style scoped>
* {
  box-sizing: border-box;
}

.container {
  /* background-image: url('@/assets/images/background.jpeg'); */
  background-size: cover;
  background-position: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.background {
  /* 设置背景颜色为白色，透明度为0.5 */
  background-color: rgba(103, 186, 239, 1);
  /* 其他样式，例如内边距、边框圆角等 */
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* 添加光影效果 */
}
.form-container {
  width: 400px;
}

#welcomeTitle {
  margin-bottom: 30px;
  color: deeppink;
  /* padding-bottom: 70px; */
}
</style>