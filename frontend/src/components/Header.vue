<script setup lang="ts">
import { ref, reactive } from "vue";
import type {FormInstance, FormRules} from 'element-plus';
import {ElMessage, ElNotification as notify } from 'element-plus';
import {AddPublicApi, LogoutApi, ShareApi} from "@/request/api";
import {useRouter} from 'vue-router';
import {useUserstore} from "@/store/user";

const router = useRouter()
const userStore = useUserstore();

const jump2MyHomepage = () => {
  userStore.visitedUserName = userStore.userName;
  console.log('on header: ', userStore.visitedUserName)
  router.push(`/user/${userStore.userName}`);
}

const refresh = () => {
  let curPath = router.currentRoute.value.fullPath
  router.push('/empty').then(() => {
    router.replace(curPath)
  })
}

async function logout() {
  let res = await LogoutApi()
  console.log('登出res：', res);
  if (res.success) {
    // TODO: 清空路由，避免直接退回回到之前登录时看到的界面
    // reset userStore to an empty string
    userStore.userName = '';
    userStore.isAdmin = false;
    ElMessage.success("登出成功");
    await router.push('/index');
  } else {
    ElMessage.error("Oops，出错了");
  }
}

const createBoxVisible = ref(false);
const createPublicVisible = ref(false)
const is_anonymous = ref(false)

const ruleFormRef = ref<FormInstance>();
const shareForm = reactive({
  username: userStore.userName,
  description: '来向我提问吧~'
});

const submitPublic = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate(async (valid) => {
    if (valid) {
      let res = await AddPublicApi({
        username: shareForm.username,
        content: shareForm.description,
        is_anonymous: is_anonymous.value,
      });
      if (res.success) {
        ElMessage({
          message: '已分享到公开表白墙',
          type: 'success'
        });
        console.log(res.success)
      } else {
        console.log('WTF，公有墙分享失败')
      }
    } else {
      console.log('share表单验证不通过')
    }
  })
}
const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  // console.log('准备 share 提问箱到广场');
  formEl.validate(async (valid) => {
    if (valid) {
      let res = await ShareApi({
        username: shareForm.username,
        description: shareForm.description
      });
      // console.log('share结果', res);
      if (res.success) {
        console.log('share表单提交成功');
        ElMessage({
          message: '提问箱已分享到广场',
          type: 'success'
        });
        // console.log('提问箱分享成功，我要刷新界面喽！')
        refresh();
        // console.log('刷新完毕！应该能看到刚刚分享的提问箱')
      } else {
        console.log('WTF，提问箱分享失败');
      }
    } else {
      console.log('share表单验证不通过');
    }
  });
}

// const updatePage = () => {
//   if (router.currentRoute.value.path === '/plaza') {
//     router.replace('/plaza');
//     // router.push('/plaza');
//   }
//   router.currentRoute.value.fullPath
// }

</script>

<template>
<!--  此处设置了元素均匀分散（space-between） -->
  <div style="
    display: flex;
    justify-content: space-between;
    align-items: center;">
    <div>
      <el-space size="large">
<!--        <img src="https://img2.imgtp.com/2024/04/05/DMHKG7pg.jpg"-->
<!--             alt="FDU" style="height: 50px;">-->
        <div class="Icons">
          <img src="@/assets/icons/freesay-icon_FDU.svg"/>
        </div>
        <p style="font-size: 28px;text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
">
          FDU <span class="freesay">freesay</span>
        </p>
<!--        <img src="@/assets/icons/chat-icon.svg"-->
<!--             alt="Logo" style="height: 40px;">-->
      </el-space>
    </div>

    <div>
      <p style="font-size: 20px">你好！{{ userStore.userName }}</p>
    </div>
    <div>
      <el-button type="success" @click="createBoxVisible = true;">
        分享提问箱
      </el-button>
      <el-button type="warning" @click="createPublicVisible = true;">
        我要表白
      </el-button>
    </div>

    <div>
      <el-button type="info" @click="jump2MyHomepage">
        我的主页
      </el-button>
      <el-button type="danger" @click="logout">
        退出登录
      </el-button>
    </div>

    <el-dialog v-model="createPublicVisible">
      <template #header="{ titleClass }" >
        <h2>
          分享到公开表白墙！
        </h2>
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
              :autosize="{ minRows: 8, maxRows: 100 }"
              input-style="font-size:18px; padding: 10px;"
          >
            <!--  placeholder="来问我问题吧~"-->
          </el-input>
        </el-form-item>
        <div class="single-setting-container">
          <p>是否匿名</p>
          <el-switch v-model="is_anonymous"
                     style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949"
          >
          </el-switch>
        </div>
      </el-form>
      <template #footer>
        <div>
          <el-button
              type="primary"
              @click="submitPublic(ruleFormRef);
                      createPublicVisible=false;">
            分享
          </el-button>
          <el-button @click="createPublicVisible = false;">
            取消
          </el-button>
        </div>
      </template>
    </el-dialog>

    <el-dialog v-model="createBoxVisible">
      <template #header="{ titleClass }" >
        <h2>
          分享提问箱让大家来问你问题吧！
        </h2>
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
              input-style="font-size:18px; padding: 10px;"
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
.Icons {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.Icons > * {
  /* margin-right: 10px; */
  margin-top: 5px;
  max-height: 45px;
}
</style>