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
  hostAvatar: String,
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

</script>

<template>
    <div>
      <el-card shadow="hover" class="boxCard">
        <el-tooltip
            content="点击进入TA的提问箱"
            placement="top"
        >
          <div @click="jump2userBox(<string>hostName)"
               class="question-container"
          >
            <p><slot name="desc"></slot></p>
          </div>
        </el-tooltip>
        <template #footer>
          <div class="footer-container">
            <avatar-username
                :host-name="hostName"
                :host-avatar="hostAvatar"
                :host-signature="hostSignature"
            >
            </avatar-username>
          </div>
        </template>
      </el-card>
    </div>
<!--    <el-dialog v-model="PostVisible">-->
<!--      <template #header="{ titleClass }" >-->
<!--        <h3>-->
<!--          向 {{ hostName }} 提问-->
<!--        </h3>-->
<!--      </template>-->
<!--      <el-form-->
<!--          ref="ruleFormRef"-->
<!--          :model="postForm"-->
<!--      >-->
<!--        <el-form-item prop="message">-->
<!--          &lt;!&ndash;          TODO: 调整 min/maxRows  &ndash;&gt;-->
<!--          <el-input-->
<!--              v-model="postForm.question"-->
<!--              type="textarea"-->
<!--              :autosize="{ minRows: 10, maxRows: 100 }"-->
<!--          >-->
<!--            &lt;!&ndash;  placeholder="来问我问题吧~"&ndash;&gt;-->
<!--          </el-input>-->
<!--        </el-form-item>-->
<!--      </el-form>-->
<!--&lt;!&ndash;      <template #footer>&ndash;&gt;-->
<!--&lt;!&ndash;        <div>&ndash;&gt;-->
<!--&lt;!&ndash;          <el-button&ndash;&gt;-->
<!--&lt;!&ndash;              type="primary"&ndash;&gt;-->
<!--&lt;!&ndash;              @click="submitForm(ruleFormRef);&ndash;&gt;-->
<!--&lt;!&ndash;                        PostVisible=false;">&ndash;&gt;-->
<!--&lt;!&ndash;            发送提问&ndash;&gt;-->
<!--&lt;!&ndash;          </el-button>&ndash;&gt;-->
<!--&lt;!&ndash;          <el-button @click="PostVisible = false;">&ndash;&gt;-->
<!--&lt;!&ndash;            取消&ndash;&gt;-->
<!--&lt;!&ndash;          </el-button>&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->
<!--&lt;!&ndash;      </template>&ndash;&gt;-->
<!--    </el-dialog>-->
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
.question-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.footer-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: 10px;
}
</style>