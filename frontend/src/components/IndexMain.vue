<script setup lang="ts">
import {useUserstore} from "@/store/user";

const userStore = useUserstore();

</script>

<template>
  <h2>
    我是 main
  </h2>
  <p>
    你好！{{ userStore.userName }}
  </p>
  <p>
    TODO
  </p>

</template>

<style scoped>

</style>