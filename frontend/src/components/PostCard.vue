<script lang="ts">
import {ref, reactive, onBeforeMount} from "vue";
import type {FormInstance, FormRules} from 'element-plus';
import {ElMessage, ElNotification as notify } from 'element-plus';

export default {
  props: {
    post_id: Number,
    question: String,
    answer: String,
    username: String,
    is_public: Boolean
  },
  setup(props) {
    console.log('PostCard:', props.post_id);
    const Visible = ref(false)
    const question = ref(props.question);
    const answer = ref(props.answer);
    let a0 = props.answer===undefined ? "" : props.answer.slice(0,5).concat("...")
    const answer0 = ref(a0);
    return {
      question, answer, answer0,
      Visible
    }
  }
}
</script>

<template>
  <div>

    <el-tooltip content="点击查看">
    <el-card shadow="hover" class="Card" @click="Visible=true;">
        <template #header>
          <p>{{ username }}</p>
          <p>问题：{{ question }}</p>
        </template>
        <div>
          <p>回答：{{ answer }}</p>
        </div>
    </el-card>
    </el-tooltip>

    <el-dialog v-model="Visible">
      <div>
        <el-card>
          <template #header>
            {{ question }}
          </template>
          <div>
            <p>{{ answer }}</p>
          </div>
        </el-card>
        <el-button @click="Visible = false;">
          关闭
        </el-button>
      </div>
    </el-dialog>
  </div>

</template>

<style scoped>

.Card {
  width: 300px;
  margin-left: 5em;
  margin-bottom: 2em;
}
.textCenter {
  text-align: center;
}
</style>