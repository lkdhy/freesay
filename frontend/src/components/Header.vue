<script setup lang="ts">
import {ElMessage, ElNotification as notify} from 'element-plus';
import {LogoutApi} from "@/request/api";
import {useRouter} from 'vue-router';
import {useUserstore} from "@/store/user";

const router = useRouter()
const userStore = useUserstore();
async function logout() {
  let res = await LogoutApi()
  console.log('登出res：', res);
  if (res.success) {
    // reset userStore to an empty string
    userStore.userName = '';
    ElMessage.success("登出成功");
    await router.push('/index');
  } else {
    ElMessage.error("Oops，出错了");
  }
}

</script>

<template>
<!--  此处设置了元素均匀分散（space-between） -->
  <div style="
    display: flex;
    /*justify-content: center;*/
    justify-content: space-between;
    align-items: center;">
    <div style="
      display: flex;
      flex-direction: row;
      align-items: center;
    ">
      <img src="https://img2.imgtp.com/2024/04/05/DMHKG7pg.jpg"
           alt="Logo" style="height: 50px;">
      <img src="@/assets/icons/chat-icon.svg"
           alt="Logo" style="height: 40px;">
      <p>FDU Tape</p>

    </div>

    <div>
      <p>你是 {{ userStore.userName }}，
        我之后想靠右边放你的头像等等，右边除了登出按钮，没用</p>
    </div>
    <div>
      <el-button type="success">
        创建提问箱
      </el-button>
      <el-button type="warning">
        我的主页
      </el-button>
    </div>
    <div>
<!--      <el-button type="info" @click="logout">-->
      <el-button type="primary" @click="logout">
        退出登录
      </el-button>
    </div>

  </div>
</template>

<style scoped>

</style>