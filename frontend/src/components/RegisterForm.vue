<script setup lang="ts">
import {reactive, ref} from 'vue';
import type {FormInstance, FormRules} from 'element-plus';
import {useRouter} from 'vue-router';
import {ElMessage} from 'element-plus';
import {RegisterApi} from "@/request/api";
import {useUserstore} from "@/store/user";

const router = useRouter();
const userStore = useUserstore();

const ruleFormRef = ref<FormInstance>();
const registerForm = reactive({
  userName: '', password: '',
  first_name:'', last_name:'',
  email:'',
});
// TODO: 完善注册表单验证规则，比如二次验证密码，对密码提要求等
const rules = reactive<FormRules<typeof registerForm>>({
  userName: [{ required: true, message: '请输入用户名'}],
  password: [{ required: true, message: '请输入密码'}],
  first_name: [{ required: true, message: '请输入'}],
  last_name: [{ required: true, message: '请输入'}],
  email: [{required: true, message: '请输入邮箱'}]
})

const successMessage = (userName: string, num: number) =>  {
  ElMessage({
    message: `注册成功！欢迎${userName}加入FDU tape的世界！\n
      你是第${num}位用户`, type: 'success'
  });
};
const failMessage = () => {
  // TODO：可以考虑用户登录时跳出 alert 弹窗，而不是上面弹出的消磁
  ElMessage({
    message: 'Oops，该用户名已存在', type: 'warning'
  });
}
const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.validate(async (valid) => {
    if (valid) {
      console.log('注册表单验证通过，可以提交');
      let res = await RegisterApi({
        username: registerForm.userName,
        password: registerForm.password,
        first_name: registerForm.first_name,
        last_name: registerForm.last_name,
        email: registerForm.email
      });
      console.log('注册结果：', res);
      if (res.success) {
        successMessage(registerForm.userName, res.total_users);
        userStore.userName = registerForm.userName;
        jump2Login();
      } else {
        failMessage();
      }
    } else {
      console.log('注册表单不通过，请重新填写');
    }
  })
}

const jump2Login = () => {
  router.push('/login');
}

</script>

<template>
  <!--      :inline="true"-->
  <el-form
      ref="ruleFormRef"
      :model="registerForm" :rules="rules"
      style="max-width: 600px"
      label-position="top" label-width="auto"
      class="demo-ruleForm"
  >

    <el-form-item label="用户名" prop="userName">
      <el-input v-model="registerForm.userName" type="text"
                placeholder="用户名是你的昵称" autocomplete="off"/>
    </el-form-item>
    <!--      切换密码隐藏与显示（show-password） -->
    <el-form-item label="密码" prop="password">
      <el-input v-model="registerForm.password" type="password"
                show-password autocomplete="off"/>
    </el-form-item>
<!--    TODO: 把姓、名搞到一行（但有可能有点麻烦）  -->
    <el-form-item label="名" prop="first_name">
      <el-input v-model="registerForm.first_name" type="text" autocomplete="off"/>
    </el-form-item>
    <el-form-item label="姓" prop="last_name">
      <el-input v-model="registerForm.last_name" type="text" autocomplete="off"/>
    </el-form-item>
    <el-form-item label="邮箱" prop="email">
      <el-input v-model="registerForm.email" type="text" autocomplete="off"/>
    </el-form-item>

    <el-form-item>
      <el-button type="danger" @click="submitForm(ruleFormRef)">注册</el-button>
      <el-button type="success" @click="jump2Login">登录</el-button>
    </el-form-item>

  </el-form>
</template>

<style scoped>

</style>