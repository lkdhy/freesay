<script setup lang="ts">
import {ref, watch} from "vue"
import AvatarUsername from "../user/AvatarUsername.vue";

const props = defineProps({
  anonymous: Boolean,
  public: Boolean,
  question: String,
  answer: String,
  tags: [String],
  host: String, poster: String,
  thread: [String]
})

// 监听visible并emit给父组件，关闭完整Tape的这个对话框
const emit = defineEmits(['close'])
const visible = ref(true)
watch(visible, () => {
  emit('close')
})

</script>

<template>
  <el-dialog v-model="visible">
    <el-card>
      <div class="tags-container">
        <el-tag v-for="tag in tags">
          {{ tag }}
        </el-tag>
      </div>

      <div>
        <div class="question-container">
          <p>
            {{ question }}
          </p>
        </div>
        <el-divider content-position="right">
          <avatar-username v-if="!anonymous" :host-name="host">
          </avatar-username>
        </el-divider>
        <div class="anwser-container">
          <el-space>
            <el-avatar></el-avatar>
            <p> {{ answer }} </p>
          </el-space>
        </div>
      </div>
    </el-card>
  </el-dialog>

</template>

<style scoped>

.question-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>