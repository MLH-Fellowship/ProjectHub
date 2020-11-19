<template>
  <div class="layout-default">
    <el-menu
      :default-active="activeRoute"
      mode="horizontal"
      @select="handleSelect"
    >
      <el-menu-item index="/">
        <img src="/logo.png" alt="Logo" style="max-height: 61px" />
      </el-menu-item>
      <el-menu-item index="/explore">Explore</el-menu-item>
      <el-menu-item index="/about">About</el-menu-item>
      <el-menu-item index="#github">
        <a
          href="https://github.com/MLH-Fellowship/ProjectHub"
          rel="noopener noreferrer"
          target="_blank"
          style="text-decoration: none"
        >
          Github
        </a>
      </el-menu-item>
      <el-menu-item index="/team">Team</el-menu-item>
      <el-submenu v-if="!user.anonymous" index="#" style="float: right">
        <template slot="title">
          <el-avatar size="large" :src="user.meta.avatar" />
        </template>
        <el-menu-item :index="`/${user.meta.login}`">
          {{ user.meta.name }}
        </el-menu-item>
        <el-menu-item index="logout" @click="logout">Logout</el-menu-item>
      </el-submenu>
      <el-menu-item
        v-if="!user.anonymous"
        index="#add-project"
        style="float: right"
      >
        <el-button type="primary" @click.native="showNewProjectDialog = true">
          + Add Project
        </el-button>
      </el-menu-item>
      <el-menu-item v-if="user.anonymous" index="/login" style="float: right">
        Login
      </el-menu-item>
    </el-menu>
    <Nuxt />
    <NewProjectDialog v-model="showNewProjectDialog" />
  </div>
</template>

<script>
import NewProjectDialog from '@/components/NewProjectDialog';
import { mapState, mapActions } from 'vuex';

export default {
  components: {
    NewProjectDialog,
  },
  data() {
    return {
      activeRoute: '#',
      showNewProjectDialog: false,
    };
  },
  computed: mapState(['user']),
  methods: {
    ...mapActions('user', ['logout']),
    handleSelect(key) {
      if (key.startsWith('/') || key.startsWith('#')) {
        if (key === '/login') {
          if (this.$route.query.redirect) {
            return;
          }
          return this.$router.push(`/?login=1&redirect=${this.$route.path}`);
        }
        this.$router.push(key);
      }
    },
  },
};
</script>

<style scoped>
.layout-default >>> .container {
  margin: 0 auto;
  min-height: calc(100vh - 61px);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
