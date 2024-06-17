<script setup lang="ts">
import PublicTape from "@/components/public_box/PublicTape.vue";
import AvatarUsername from "@/components/user/AvatarUsername.vue";
import {ref} from "vue";

interface public_thread {
  username: string
  avatar: string
  is_anonymous: boolean
  content: string
}
// interface GotPublic {
//   username: string
//   avatar: string
//   is_anonymous: boolean
//   content: string
//   thread: public_thread[]
// }
const props = defineProps({
  pid: Number,
  username: String,
  avatar: String,
  is_anonymous: Boolean,
  content: String,
  thread: Array<public_thread>,
})

console.log('pid=', props.pid)

const emit = defineEmits(['responded'])
const publicTapeVisible = ref(false)

</script>

<template>
  <div class="public-card-container">
    <el-tooltip content="点击查看">
      <el-card class="post-card"
               shadow="hover"
               @click="publicTapeVisible = true; console.log(publicTapeVisible)"
      >
        <div class="question-container">
          <p style="word-break: break-all; text-align: center">
            {{ content }}
          </p>
        </div>

        <template #footer style="max-height: 10px">
          <avatar-username v-if="!is_anonymous"
                           :host-name="username"
                           :host-avatar="avatar"
          >
          </avatar-username>
        </template>
<!--        <el-divider content-position="right">-->
<!--          <avatar-username v-if="is_anonymous"-->
<!--                           :host-name="username"-->
<!--                           :host-avatar="avatar"-->
<!--          >-->
<!--          </avatar-username>-->
<!--        </el-divider>-->
      </el-card>
    </el-tooltip>
  </div>

  <public-tape
      v-if="publicTapeVisible"
      @close="publicTapeVisible = false"
      @responded="emit('responded')"
      :pid="pid"
      :thread="thread"
  ></public-tape>
</template>

<style scoped>
.public-card-container {
  margin-left: 50px;
  margin-bottom: 5px;
  margin-top: 5px;
  width: 300px;
}
.question-container {

}
.post-card {
  border-radius: 15px;
}
</style>