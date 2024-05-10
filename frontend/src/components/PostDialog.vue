<script setup lang="ts">
import { ref, reactive } from 'vue';
import type {FormInstance, FormRules} from 'element-plus';
import { useRouter } from "vue-router";
import { useUserstore } from "@/store/user.js";
import { PostApi } from "@/request/api.js";
import { ElMessage } from "element-plus";

const router = useRouter();
const userStore = useUserstore();

// console.log(`你想要给${userStore.visitedUserName}发问题吗`);

const dialogVisible = ref(false);

const ruleFormRef = ref<FormInstance>();
const postForm = reactive({
  username: userStore.userName,
  hostUsername: userStore.visitedUserName,
  question: ''
});

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  console.log('准备 post 帖子');
  formEl.validate(async (valid) => {
    if (valid) {
      console.log('post表单验证通过，准备提交');
      console.log(postForm);
      let res = await PostApi({
        username: postForm.username,
        hostUsername: postForm.hostUsername,
        question: postForm.question
      });
      console.log('post结果', res);
      if (res.success) {
        console.log('post表单提交成功');
      } else {
        console.log('WTF');
        ElMessage({
          message: 'post 成功',
          type: 'success'
        });
      }
    } else {
      console.log('post表单验证不通过');
    }
  });
}

</script>

<template>
  <el-button @click="dialogVisible = true">在这里向我提问</el-button>
  <el-dialog
      v-model="dialogVisible"
  >
    <template #header="{ titleClass }">
      <h4>
        你正在向<slot name="hostName"></slot>提问
      </h4>
    </template>
    <p>
      你想对他说：
    </p>
    <el-form
      ref="ruleFormRef"
      :model="postForm"
    >
      <el-form-item prop="message">
        <el-input
            v-model="postForm.question"
            type="textarea"
            :autosize="{ minRows: 10, maxRows: 100 }"
            placeholder="你想对他说……"
        >
        </el-input>
      </el-form-item>
    </el-form>
    <template #footer>
      <div>
        <el-button type="primary" @click="submitForm(ruleFormRef); dialogVisible=false;">
          提交问题
        </el-button>
        <el-button @click="dialogVisible = false">
          取消
        </el-button>
      </div>
    </template>
  </el-dialog>
</template>

<!--<script>-->
<!--export default {-->
<!--  data() {-->
<!--    return {-->
<!--      dialogVisible: false,-->
<!--      form: {-->
<!--        name: '',-->
<!--        // 更多表单数据...-->
<!--      }-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--    submitForm(formName) {-->
<!--      this.$refs[formName].validate((valid) => {-->
<!--        if (valid) {-->
<!--          alert('submit!');-->
<!--        } else {-->
<!--          console.log('error submit!!');-->
<!--          return false;-->
<!--        }-->
<!--      });-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style>-->
<!--.inputQuestion {-->
<!--  height: 200px;-->
<!--}-->
<!--</style>-->