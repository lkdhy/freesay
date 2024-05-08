<script setup lang="ts">

import {reactive, ref} from 'vue'
import type {FormInstance, FormRules} from 'element-plus'
import {useRouter} from 'vue-router'
import {useUserstore} from '@/store/user'

const userStore=useUserstore();
const router = useRouter();

const ruleFormRef = ref<FormInstance>();

const ruleForm = reactive({
  // 刚刚注册完要登录，自动填上用户名
  userName: userStore.userName.length ?
      userStore.userName : '',
  password: ''
});

const checkUserName = (rule: any, value: any, callback: any) => {
  if (value === '') {
    return callback(new Error('请输入用户名'))
  } else {
    callback()
  }
}

const checkPassword = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('请输入密码'))
  } else {
    callback()
  }
}

const rules = reactive<FormRules<typeof ruleForm>>({
  userName: [{validator: checkUserName, trigger: 'blur'}],
  password: [{validator: checkPassword, trigger: 'blur'}],
})
import { TestHello } from "@/request/api";
import {LoginApi} from "@/request/api";
import {ElMessage} from 'element-plus'
import Index from "@/pages/Index.vue";

const successMessage = (userName: string) =>  {
  ElMessage({
    message: `欢迎回来，${userName}~`,
    type: 'success'
  });
};
const failMessage = () => {
  // TODO：可以考虑用户登录时跳出 alert 弹窗（洛谷），而不是上面弹出的消息
  ElMessage({
    message: 'Oops，用户名或密码错误',
    type: 'warning'
  });
}
const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate(async (valid) => {
    if (valid) {
      console.log('表单验证通过，可以提交')
      let res = await LoginApi({
        username: ruleForm.userName,
        password: ruleForm.password
      });
      console.log(res);
      console.log('登陆结果：' + res.success);
      if (res.success) {
        successMessage(ruleForm.userName);
        // 存下状态
        userStore.userName = ruleForm.userName;
        await router.push('/index');
      } else {
        failMessage();
        return false;
      }
    } else {
      console.log('登录表单验证未通过，请重新填写表单');
      // let res = await TestHello();
      // console.log(res);
    }
  })
}

// 【更新】可以按"注册"按钮跳转到注册界面
const jump2Register = () => {
  router.push('/register');
}

</script>

<template>
<!--  【更新】表单：
      - 按钮颜色调整
      - 表单域标签放在上方（<label-position>）
  -->
  <el-form
      ref="ruleFormRef"
      :model="ruleForm"
      :rules="rules"
      style="max-width: 600px"
      label-position="top"
      label-width="auto"
      class="demo-ruleForm"
  >
    <el-form-item label="你的用户名" prop="userName">
      <el-input v-model="ruleForm.userName" type="text" autocomplete="off"/>
    </el-form-item>

<!--    <el-form-item label="密码" prop="password">-->
    <el-form-item label="你的密码" prop="password">
<!--      切换密码隐藏与显示（show-password） -->
      <el-input v-model="ruleForm.password" type="password"
                show-password autocomplete="off"/>
    </el-form-item>

    <el-form-item>
<!--      success：绿色；danger：红色  -->
<!--      https://element-plus.org/zh-CN/component/button.html  -->
      <el-button type="success" @click="submitForm(ruleFormRef)">登录</el-button>
      <el-button type="danger" @click="jump2Register">注册</el-button>
    </el-form-item>

  </el-form>
</template>

<style scoped>

</style>