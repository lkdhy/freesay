<script setup lang="ts">

import {reactive, ref} from 'vue'
import type {FormInstance, FormRules} from 'element-plus'
import {useRouter} from 'vue-router'
import {useUserstore} from '@/store/user'

const userStore=useUserstore()
const router = useRouter()

const ruleFormRef = ref<FormInstance>()

const ruleForm = reactive({
  userName: '小明还是小红...',
  password: ''
})


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
      alert('登陆成功！console控制台也能看得到后端返回的数据')
    } else {
      console.log('表单验证未通过，请重新填写表单');
      let res = await TestHello();
      console.log(res);
      alert('res: ' + JSON.stringify(res));
    }
  })
}



</script>

<template>
  <el-form
      ref="ruleFormRef"
      :model="ruleForm"
      :rules="rules"
      style="max-width: 600px"
      label-width="auto"
      class="demo-ruleForm"
  >
    <el-form-item label="你的用户名" prop="userName">
      <el-input v-model="ruleForm.userName" type="text" autocomplete="off"/>
    </el-form-item>

<!--    <el-form-item label="密码" prop="password">-->
    <el-form-item label="你的密码" prop="password">
      <el-input v-model="ruleForm.password" type="password" autocomplete="off"/>
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="submitForm(ruleFormRef)">登录</el-button>
      <el-button type="warning">注册</el-button>
    </el-form-item>

  </el-form>
</template>

<style scoped>

</style>