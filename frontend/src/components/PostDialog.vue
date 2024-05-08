<template>
  <el-button @click="dialogVisible = true">点击我</el-button>
  <el-dialog
      v-model="dialogVisible"
  >
    <template #header="{ titleClass }">
      <h4>
        你正在向<slot name="hostName"></slot>提问
      </h4>
    </template>
    <p>
      你想对他说：
    </p>
    <el-input
        v-model="form.name"
        type="textarea"
        :autosize="{ minRows: 10, maxRows: 100 }"
        placeholder="你想对他说……"
    >
    </el-input>

        <el-button type="primary" @click="submitForm('form')">立即创建</el-button>
        <el-button @click="dialogVisible = false">取消</el-button>

  </el-dialog>
</template>

<script>
export default {
  data() {
    return {
      dialogVisible: false,
      form: {
        name: '',
        // 更多表单数据...
      }
    }
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!');
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    }
  }
}
</script>

<style>
.inputQuestion {
  height: 200px;
}
</style>