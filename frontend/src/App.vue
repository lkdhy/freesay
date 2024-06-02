<script setup lang="ts">
import SnowParticles from "@/components/Particles/SnowParticles.vue";
import ColorfulBubblesParticles from "@/components/Particles/ColorfulBubblesParticles.vue";
</script>

<template>
<!--  <snow-particles></snow-particles>-->
<!--  <colorful-bubbles-particles></colorful-bubbles-particles>-->
  <router-view></router-view>
</template>

<style>
*{
  margin:0;
  padding:0;
  border:0
}
.background-image {
  opacity: 98%;
  filter: brightness(0.9);
}
.freesay {
   font-style: italic;
   font-family: Consolas;
}
.tags-container {
  display: flex;
  gap: 8px;
}
</style>