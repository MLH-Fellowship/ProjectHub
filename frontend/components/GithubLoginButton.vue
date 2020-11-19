<template>
  <el-button round @click="authenticate">Login With GitHub</el-button>
</template>

<script>
export default {
  name: 'GithubLoginButton',
  methods: {
    async authenticate() {
      const { code } = await this.$auth.authenticate('github');
      await this.$store.dispatch('user/login', code);

      this.$router.push(this.$route.query.redirect || '/');
    },
  },
};
</script>

<style></style>
