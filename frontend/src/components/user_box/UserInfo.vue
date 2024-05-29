<script setup lang="ts">
import { ref } from 'vue'
import { useUserstore } from "@/store/user";
import { SetSignature } from "@/request/api";
// props
const props = defineProps({
  username: String,
  avatar: String,
  email: String,
  signature: String
})
console.log(props.username)

const userStore = useUserstore()
const isMine = userStore.userName == props.username
const input_signature = ref('')
console.log(userStore.userName, props.username)

console.log(isMine)
const modifySignature = async () => {
  console.log(input_signature.value)
  if (!input_signature.value.length) return

  // TODO
  const set_res = await SetSignature({
    username: props.username,
    signature: input_signature.value
  })
  if (set_res.success) {
    return
  } else  {
    console.log('WTF')
  }
}

</script>

<template>
<!--  <el-avatar size="large" shape="square">-->
<!--  </el-avatar>-->

  <el-avatar
      :src="avatar"
      :size="100"
      shape="circle"
  ></el-avatar>

  <div>
    <p>{{ username }}</p>
    <p> {{ email }}</p>
    <p> {{ signature }}</p>
  </div>

  <el-popover v-if="isMine">
    <el-input v-model="input_signature">
    </el-input>
    <el-button @click="modifySignature">提交</el-button>
    <template #reference>
      <el-button>修改个性签名</el-button>
    </template>
  </el-popover>

</template>

<style scoped>
* {
  margin-top: 15px;
}
</style>