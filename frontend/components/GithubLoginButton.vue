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

      if (this.$route.hash && this.$route.hash.startsWith('#redirect=')) {
        return this.$router.push(this.$route.hash.slice(10));
      }

      this.$router.push('/');
    },
  },
};
</script>

<style></style>
