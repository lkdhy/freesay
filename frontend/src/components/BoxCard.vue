<script lang="ts">
import { ElMessage } from "element-plus";
import { defineComponent } from "vue";
export default {
  props: {
    fatherData: String
  },
  setup(props) {
    console.log('请见下面！！！！')
    console.log(props.fatherData);
  }
}

</script>

<template>
  <el-card class="boxCard" @click="console.log(`按下了${fatherData}`);">
    <template #header>
        <p>
          <slot name="desc">

          </slot>
        </p>
    </template>
<!--    <img-->
<!--        src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"-->
<!--    />-->
    <div class="hostInfo">
<!--      我想在这里放用户名等用户相关的东西-->
      <slot name="hostInfo"></slot>
    </div>
  </el-card>
</template>

<style scoped>
/*  TODO
*/
.boxCard {
  width: 30%;
  margin-left: 0.5em;
  margin-bottom: 1em;
}
.hostInfo {
  text-align: center;
}
</style>