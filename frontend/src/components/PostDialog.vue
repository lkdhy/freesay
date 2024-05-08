<template>
  <el-button @click="dialogVisible = true">点击我</el-button>
  <el-dialog v-model="dialogVisible" title="填写表单">
    <el-form ref="form" :model="form" label-width="80px">

<!--      <el-table>-->
<!--        <el-table-column label="hhh"></el-table-column>-->
<!--        <el-table-column label="fn2uon2o"></el-table-column>-->
<!--      </el-table>-->
      
      <p>你好</p>
      <a href="https://cs.fudan.edu.cn">复旦大学计算机科学技术学院</a>
      
      <el-form-item label="活动名称">
        <el-input
            v-model="form.name"
            type="textarea"
            maxlength="10"
        ></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm('form')">立即创建</el-button>
        <el-button @click="dialogVisible = false">取消</el-button>
      </el-form-item>
    </el-form>


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