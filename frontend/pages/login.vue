<template>
  <div class="container">
    <el-card class="login-box-card">
      <div slot="header" class="clearfix">
        <span>Login</span>
      </div>
      <GithubLoginButton />
    </el-card>
  </div>
</template>

<script>
import GithubLoginButton from '@/components/GithubLoginButton';

export default {
  components: {
    GithubLoginButton,
  },
};
</script>

<style>
.login-box-card {
  width: 80%;
  max-width: 400px;
  min-width: 200px;
}
</style>
