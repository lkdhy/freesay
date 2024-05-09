<script setup lang="ts">
import { ref, reactive } from "vue";
import type {FormInstance, FormRules} from 'element-plus';
import {ElMessage, ElNotification as notify } from 'element-plus';
import {LogoutApi, PostAPI} from "@/request/api";
import {useRouter} from 'vue-router';
import {useUserstore} from "@/store/user";

const router = useRouter()
const userStore = useUserstore();

const jump2MyHomepage = () => {
  router.push(`/user/${userStore.userName}`);
}

async function logout() {
  let res = await LogoutApi()
  console.log('登出res：', res);
  if (res.success) {
    // TODO: 清空路由，避免直接退回回到之前登录时看到的界面
    // reset userStore to an empty string
    userStore.userName = '';
    ElMessage.success("登出成功");
    await router.push('/index');
  } else {
    ElMessage.error("Oops，出错了");
  }
}

const createBoxVisible = ref(false);
const ruleFormRef = ref<FormInstance>();
const shareForm = reactive({
  username: userStore.userName,
  description: '来向我提问吧~'
});

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  console.log('准备 share 提问箱到广场');
  formEl.validate(async (valid) => {
    if (valid) {
      console.log('post表单验证通过，准备提交');
      console.log(shareForm);
      // let res = await PostAPI({
      //   username: shareForm.username,
      //   description: shareForm.description
      // });
      // console.log('post结果', res);
      // if (res.success) {
      //   console.log('post表单提交成功');
      // } else {
      //   console.log('WTF');
      //   ElMessage({
      //     message: 'post 成功',
      //     type: 'success'
      //   });
      // }
    } else {
      console.log('post表单验证不通过');
    }
  });
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
        我之后想靠右边放你的头像等等，右边只有“创建提问箱”按钮是没用的</p>
    </div>
    <div>

<!--      TODO  -->
      <el-button type="success" @click="createBoxVisible = true;">
        分享我的提问箱
      </el-button>

      <el-button type="warning" @click="jump2MyHomepage">
        我的主页
      </el-button>
    </div>
    <div>
<!--      <el-button type="info" @click="logout">-->

      <el-button type="primary" @click="logout">
        退出登录
      </el-button>
    </div>

    <el-dialog v-model="createBoxVisible">
      <template #header="{ titleClass }" >
        <h3>
          分享提问箱让大家来问你问题吧！
        </h3>
      </template>
      <el-form
          ref="ruleFormRef"
          :model="shareForm"
      >
        <el-form-item prop="message">
<!--          TODO: 调整 min/maxRows  -->
          <el-input
              v-model="shareForm.description"
              type="textarea"
              :autosize="{ minRows: 10, maxRows: 100 }"
          >
            <!--  placeholder="来问我问题吧~"-->
          </el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <div>
          <el-button
              type="primary"
              @click="submitForm(ruleFormRef);
                      createBoxVisible=false;">
            分享到广场
          </el-button>
          <el-button @click="createBoxVisible = false">
            取消
          </el-button>
        </div>
      </template>
    </el-dialog>

  </div>
</template>

<style scoped>

</style>