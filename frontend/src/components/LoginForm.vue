<script setup lang="ts">

import {reactive, ref} from 'vue'
import type {FormInstance, FormRules} from 'element-plus'
import {useRouter} from 'vue-router'
import {useUserstore} from '@/store/user'
import {LoginApi} from "@/request/api";
import {ElMessage} from 'element-plus'

const userStore=useUserstore();
const router = useRouter();

const ruleFormRef = ref<FormInstance>();
// const ruleForm = reactive<RuleForm>({
const ruleForm = reactive({
  // 刚刚注册完要登录，自动填上用户名
  userName: userStore.userName.length ? userStore.userName : '',
  password: ''
});

const checkUserName = (rule: any, value: any, callback: any) => {
  if (value === '') {
    return callback(new Error('请输入用户名'))
  } else { callback() }
}
const checkPassword = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('请输入密码'))
  } else { callback() }
}

const rules = reactive<FormRules<typeof ruleForm>>({
  userName: [{validator: checkUserName, trigger: 'blur'}],
  password: [{validator: checkPassword, trigger: 'blur'}],
  // [modified] 不用 validator 的写法（这样标签名前面会有红色的星号，太难看）
  // userName: [
  //   { required: false, message: '请输入用户名' }
  // ],
  // password: [
  //   { required: true, message: '请输入密码' }
  // ]
})
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
        username: ruleForm.userName, password: ruleForm.password
      });
      console.log('登录结果：', res);
      if (res.success) {
        successMessage(ruleForm.userName);
        userStore.userName = res.userinfo.username;
        userStore.avatar = res.userinfo.avatar;
        userStore.signature = res.userinfo.signature;
        userStore.email = res.userinfo.email;
        await router.push('/plaza');
      } else {
        failMessage();
        return false;
      }
    } else {
      console.log('登录表单验证未通过，请重新填写表单');
    }
  })
}

// 【更新】可以按"注册"按钮跳转到注册界面
const jump2Register = () => {
  router.push('/register');
}

</script>

<template>
<!--  https://element-plus.org/zh-CN/component/form.html#%E8%A1%A8%E5%8D%95%E6%A0%A1%E9%AA%8C-->
<!--  Form 组件提供了表单验证的功能，
  只需为 rules 属性传入约定的验证规则，并将 form-Item 的 prop 属性设置为需要验证的特殊键值即可。-->
  <el-form ref="ruleFormRef"
      :model="ruleForm" :rules="rules"
      style="max-width: 600px"
      label-position="top" label-width="auto"
  >
    <el-form-item label="你的用户名" prop="userName">
      <el-input v-model="ruleForm.userName" type="text" autocomplete="off"/>
    </el-form-item>

    <el-form-item label="你的密码" prop="password">
<!--      切换密码隐藏与显示（show-password） -->
      <el-input v-model="ruleForm.password" type="password"
                show-password autocomplete="off"/>
    </el-form-item>

<!--    <el-form-item>-->
    <div style="display: flex; justify-content: center;">
<!--      success：绿色；danger：红色  -->
<!--      https://element-plus.org/zh-CN/component/button.html  -->
      <el-button type="success" @click="submitForm(ruleFormRef)">登录</el-button>
      <el-button type="danger" @click="jump2Register">注册</el-button>
    </div>

<!--    <p style="text-align: center">[TODO]没有账号？注册</p>-->
<!--    </el-form-item>-->

  </el-form>
</template>

<style scoped>

</style>