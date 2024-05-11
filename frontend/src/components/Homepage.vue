<script lang="ts">
import {onBeforeMount, reactive, ref} from "vue";
import {useRouter} from 'vue-router';
import {ElMessage} from 'element-plus';
import {GetHostPostApi, GetPostApi} from "@/request/api";
import {useUserstore} from "@/store/user";
import PostDialog from "@/components/PostDialog.vue";
import tmp from "@/components/tmp.vue";
import UnansweredCard from "@/components/UnansweredCard.vue";
import PostCard from "@/components/PostCard.vue";

export default {
  props: {
    signature: String
  },
  components: {
    PostCard,
    UnansweredCard,
  },
  setup() {
    const router = useRouter();
    const userStore = useUserstore();
    console.log(`当前访问用户是${userStore.visitedUserName}`);
    console.log(`你是${userStore.userName}`);
    interface GotPost {
      id: number
      username: string
      question: string
      answer: string
    }
    const curUser = ref<string>(userStore.userName);
    const visitedUser = ref<string>(userStore.visitedUserName);
    const isMine = ref<boolean>(curUser.value === visitedUser.value);
    const p1 = ref<GotPost[]>([]);
    const p2 = ref<GotPost[]>([]);
    const p3 = ref<GotPost[]>([]);
    const p4 = ref<GotPost[]>([]);
    console.log(isMine.value);

    onBeforeMount(async () => {
      console.log('即将请求这个用户相关的帖子!')
      let res = await GetHostPostApi({
        username: visitedUser.value
      });
      console.log(res);
      if (res.success) {
        console.log('cool!!')
        res.posts.forEach(post => {
          if (!isMine.value) {
            if (post.answer.length
                && (post.is_public || post.username===curUser.value)) {
              p2.value.push(post);
            }
            console.log('p2:', p2.value);
          } else {
            if (!post.answer.length) {
              p1.value.push(post);
            } else {
              p2.value.push(post);
              console.log(post);
            }
          }
        })
      } else {
        console.log('WTF, host posts 请求失败')
      }
      if (!isMine.value) return
      let res2 = await GetPostApi({
        username: visitedUser.value
      });
      if (res2.success) {
        res2.posts.forEach(post => {
          if (post.answer.length) {
            p3.value.push(post);
          } else {
            p4.value.push(post);
          }
        })
      }
    })
    return {
      isMine, visitedUser, curUser,
      p1, p2, p3, p4
    }
  }
}

</script>

<template>
  <h2 v-if="isMine">
    我的主页
  </h2>
  <h2 v-else>
    {{ visitedUser }} 的主页
  </h2>
  <h3>
    你好 {{ curUser }}
  </h3>
<!--  <h3>-->
<!--    这里是 {{ $route.params.id }} 的个人主页-->
<!--  </h3>-->

  <el-descriptions
      title=""
      border
  >
    <el-descriptions-item label="Username">
      {{ $route.params.id }}
    </el-descriptions-item>
<!--    <el-descriptions-item label="姓名"></el-descriptions-item>-->
<!--    TODO: 增加个性签名  -->
        这个人很懒，什么都没有写
    <el-descriptions-item label="个性签名">
      这里放个性签名？？？？？
    </el-descriptions-item>
<!--    <el-descriptions-item label="Remarks">-->
<!--      <el-tag size="small">School</el-tag>-->
<!--    </el-descriptions-item>-->
<!--    <el-descriptions-item label="Address">-->
<!--      这里放个性签名？？？？？-->
<!--    </el-descriptions-item>-->
  </el-descriptions>

<!--  <el-button type="primary">-->
<!--    向他提问-->
<!--  </el-button>-->

  <post-dialog v-if="!isMine">
    <template v-slot:hostName>
      {{ $route.params.id }}
    </template>
  </post-dialog>

<!--  TODO  -->
<!--  <h2>-->
<!--    他的回答-->
<!--  </h2>-->
  <div>

    <el-tabs>
      <el-tab-pane label="未答" v-if="isMine">
        <el-scrollbar height="400px">
          <div class="canvas">
            <div v-for="post of p1">
              <unanswered-card
                  :post_id="post.id"
                  :question="post.question">
              </unanswered-card>
            </div>
          </div>
        </el-scrollbar>
      </el-tab-pane>

      <el-tab-pane label="已答">
        <el-scrollbar height="400px">
          <div class="canvas">
            <div v-for="post of p2">
              <post-card
                  :post_id="post.id"
                  :question="post.question"
                  :answer="post.answer">
              </post-card>
            </div>
          </div>
        </el-scrollbar>
      </el-tab-pane>

      <el-tab-pane label="有回答" v-if="isMine">
        <el-scrollbar height="400px">
          <div class="canvas">
            <div v-for="post of p3">
              <post-card
                  :post_id="post.id"
                  :question="post.question"
                  :answer="post.answer"
                  :username="post.username">
              </post-card>
            </div>
          </div>
        </el-scrollbar>
      </el-tab-pane>

      <el-tab-pane label="未回答" v-if="isMine">
        <el-scrollbar height="400px">
          <div class="canvas">
            <div v-for="post of p4">
              <post-card
                  :post_id="post.id"
                  :question="post.question"
                  :answer="post.answer"
                  :username="post.username">
              </post-card>
            </div>
          </div>
        </el-scrollbar>
      </el-tab-pane>
    </el-tabs>
  </div>

</template>

<style scoped>
/* TODO */
* {
  margin: 10px;
}
</style>