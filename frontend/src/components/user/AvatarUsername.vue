<script setup lang="ts">
import { UserFilled } from "@element-plus/icons-vue"
import HoverUserinfo from "@/components/user/HoverUserinfo.vue";
// props
const props = defineProps({
  hostName: String,
  hostSignature: String
})
</script>

<template>
  <div class="avatar-username-container">
<!--    <el-space alignment="center" spacer="|">-->
    <el-popover
        :width=300
        placement="top-start"
        class="popover-container"
    >
      <template #reference>
        <el-space alignment="center">
      <!--    <el-avatar :icon="UserFilled" />-->
          <el-avatar :icon="UserFilled" size="small" shape="circle"/>
          <p>
            {{ hostName }}
          </p>
        </el-space>
      </template>

      <hover-userinfo :host-name="props.hostName" :host-signature="hostSignature">
      </hover-userinfo>

    </el-popover>
  </div>

</template>

<style scoped>
.avatar-username-container {
  display: flex;
  justify-content: center;
  height: 5px;
}
</style>