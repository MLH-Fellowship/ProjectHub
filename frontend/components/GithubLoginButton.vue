<template>
  <div>
    <el-button @click="authenticate">Login With GitHub</el-button>
  </div>
</template>

<script>
export default {
  name: 'GithubLoginButton',
  methods: {
    async authenticate() {
      const { code } = await this.$auth.authenticate('github');
      await this.$store.dispatch('user/login', code);
      this.$router.push('/');
    },
  },
};
</script>

<style></style>
