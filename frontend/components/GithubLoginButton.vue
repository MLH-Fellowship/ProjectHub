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
      // const { token } = this.$axios.$post('/api/auth/github', { code });
      // { token: jwt => store in local storage, email => display it in the client }
      console.log(code);
    },
  },
};
</script>

<style></style>
