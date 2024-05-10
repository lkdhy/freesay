<script lang="ts">
import {ref, reactive, onBeforeMount} from "vue";
import type {FormInstance, FormRules} from 'element-plus';
import {ElMessage, ElNotification as notify } from 'element-plus';
import { AnswerApi } from "@/request/api";
import {useRouter} from 'vue-router';
import {useUserstore} from "@/store/user";
import tmp from "@/components/tmp.vue";

const router = useRouter();

export default {
  props: {
    post_id: Number,
    question: String,
  },
  setup(props) {
    const userStore = useUserstore();
    const AnswerVisible = ref(false)

    console.log('post_id', props.post_id);
    const post_id = ref(props.post_id)
    const question = ref(props.question)
    const ruleFormRef = ref<FormInstance>();
    const answerForm = reactive({
      answer: '我是tmp用户回答！！'
    });
    const submitForm = (formEl: FormInstance | undefined) => {
      if (!formEl) return;
      console.log('准备answer问题');
      formEl.validate(async (valid) => {
        if (valid) {
          console.log('answer问题表单验证通过，准备提交');
          console.log(answerForm);
          let tmpid = props.post_id != undefined ? props.post_id : 0;
          console.log(tmpid);
          let res = await AnswerApi({
            id: tmpid,
            answer: answerForm.answer
          });
          console.log('answer结果', res);
          if (res.success) {
            console.log('answer表单提交成功');
            ElMessage({
              message: '已发送回答',
              type: 'success'
            });
          } else {
            console.log('WTF, answer提问失败');
          }
        } else {
          console.log('answer表单验证不通过');
        }
      });
    }
    return {
      question,
      AnswerVisible, answerForm,
      submitForm, ruleFormRef
    };
  }
}

</script>

<template>
  <div class="unansweredCard">
    <el-card>
        <el-tooltip
          content="点击回答TA的问题"
        >
          <div @click="
              AnswerVisible = true;">
            <p>
              {{ question }}
            </p>
          </div>
        </el-tooltip>

      <el-dialog v-model="AnswerVisible">
        <el-form
            ref="ruleFormRef"
            :model="answerForm"
        >
          <el-form-item prop="message">
            <!--          TODO: 调整 min/maxRows  -->
            <el-input
                v-model="answerForm.answer"
                type="textarea"
                :autosize="{ minRows: 8, maxRows: 12 }"
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
                        AnswerVisible=false;">
              发送回答
            </el-button>
            <el-button @click="AnswerVisible = false;">
              取消
            </el-button>
          </div>
        </template>
      </el-dialog>
    </el-card>
  </div>
</template>

<style scoped>
/*  TODO
*/
.unansweredCard {
  width: 300px;
  height: 40px;
  margin-left: 5em;
  margin-bottom: 10em;
}

</style>