<script setup lang="ts">
import { ref, reactive } from "vue";
import type {FormInstance, FormRules} from 'element-plus';
import {ElMessage, ElNotification as notify } from 'element-plus';
import {PostApi} from "@/request/api";
import {useUserstore} from "@/store/user";
import {useRouter} from "vue-router";
import AvatarUsername from "@/components/user/AvatarUsername.vue";
// props
// const props = defineProps(['hostName'])
const props = defineProps({
  hostName: String,
  hostSignature: String
})

const userStore = useUserstore();
const router = useRouter()
const PostVisible = ref(false)
const ruleFormRef = ref<FormInstance>();
const postForm = reactive({
  username: userStore.userName,
  question: '你想问TA…'
});

const jump2userBox = (hostName: string) => {
  router.push(`/user2/${hostName}`)
}

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  console.log('准备post问题');
  formEl.validate(async (valid) => {
    if (valid) {
      console.log('post问题表单验证通过，准备提交');
      console.log(postForm);
      let tmp = props.hostName != undefined ? props.hostName : "WTF_why?";
      let res = await PostApi({
        username: postForm.username,
        hostUsername: tmp,
        question: postForm.question
      });
      // console.log('share结果', res);
      if (res.success) {
        console.log('share表单提交成功');
        ElMessage({
          message: '已向TA发送提问',
          type: 'success'
        });
      } else {
        console.log('WTF，post提问失败');
      }
    } else {
      console.log('post表单验证不通过');
    }
  });
}

</script>

<template>
  <div>
    <el-card shadow="hover" class="boxCard">
      <el-tooltip
        content="点击向TA提问"
      >
        <div @click="jump2userBox(<string>hostName)">
          <p><slot name="desc"></slot></p>
        </div>
      </el-tooltip>
      <template #footer>
<!--        <div class="hostInfo" style="-->
<!--            max-height: 5px; display: flex; flex-direction: column; justify-content: center;-->
<!--           ">-->
<!--          &lt;!&ndash;      我想在这里放用户名等用户相关的东西&ndash;&gt;-->
<!--          <span>{{ hostName }}</span>-->
<!--        </div>-->
        <avatar-username :host-name="hostName" :host-signature="hostSignature">
        </avatar-username>
      </template>
    </el-card>
    <el-dialog v-model="PostVisible">
      <template #header="{ titleClass }" >
        <h3>
          向 {{ hostName }} 提问
        </h3>
      </template>
      <el-form
          ref="ruleFormRef"
          :model="postForm"
      >
        <el-form-item prop="message">
          <!--          TODO: 调整 min/maxRows  -->
          <el-input
              v-model="postForm.question"
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
                        PostVisible=false;">
            发送提问
          </el-button>
          <el-button @click="PostVisible = false;">
            取消
          </el-button>
        </div>
      </template>
    </el-dialog>
  </div>
</template>

<style scoped>
/*  TODO */
.boxCard {
  width: 300px;
  margin-left: 5em;
  /* margin-bottom: 1.5em; */
  
  /*  added */
  border-radius: 10px;
}
.hostInfo {
  text-align: center;
}
</style>