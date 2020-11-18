<template>
  <div class="container">
    <el-card class="login-box-card">
      <div slot="header" class="clearfix">
        <span>Login</span>
      </div>
      <LoginBox />
    </el-card>
  </div>
</template>

<script>
import LoginBox from '@/components/LoginBox';

export default {
  components: {
    LoginBox,
  },
};
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.login-box-card {
  width: 80%;
  max-width: 400px;
  min-width: 200px;
}
</style>
