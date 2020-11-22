<template>
  <div class="layout-default">
    <!-- can't figure out how to make navbar stick to top -->
    <div class="flex flex-row items-center">
      <div
        style="border-bottom: solid 1px #e6e6e6; background-color: #fff"
        @click="$router.push('/')"
      >
        <img class="di" src="/logo.png" alt="Logo" style="max-height: 57px" />
      </div>
      <div style="flex: 1" class="f5">
        <el-menu
          class="fixed"
          mode="horizontal"
          :router="true"
          :default-active="$route.path"
        >
          <el-menu-item index="/explore">Explore</el-menu-item>
          <el-menu-item index="/team">Team</el-menu-item>
          <el-menu-item :index="null" @click="github">Github</el-menu-item>
          <el-submenu v-if="!user.anonymous" index="#" style="float: right">
            <template slot="title">
              <el-avatar size="large" :src="user.meta.avatar" />
            </template>
            <el-menu-item :index="`/${user.meta.login}`">
              {{ user.meta.name }}
            </el-menu-item>
            <el-menu-item :index="`/${user.meta.login}/bookmarks`">
              Bookmarks
            </el-menu-item>
            <el-menu-item @click="logout">Logout</el-menu-item>
          </el-submenu>
          <el-menu-item v-if="!user.anonymous" style="float: right">
            <el-button
              type="primary"
              @click.native="showNewProjectDialog = true"
            >
              + Add Project
            </el-button>
          </el-menu-item>
          <el-menu-item
            v-if="user.anonymous"
            :index="login"
            style="float: right"
          >
            Login
          </el-menu-item>
        </el-menu>
      </div>
    </div>
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
      showNewProjectDialog: false,
      route: this.$route.path,
    };
  },
  computed: {
    ...mapState(['user']),
    login() {
      if (this.$route.query.redirect) {
        return '/';
      }
      return `/?login=1&redirect=${this.$route.path}`;
    },
  },
  methods: {
    ...mapActions('user', ['logout']),
    github() {
      window.open('https://github.com/MLH-Fellowship/ProjectHub', '_blank');
    },
  },
};
</script>

<style scoped>
.el-menu-item {
  font-weight: 300;
  font-size: 1.5rem;
}

.el-menu-item.is-active {
  font-weight: bolder;
  border-bottom: 2px solid #fbc6fd;
}

.layout-default >>> .container {
  margin: 0 auto;
  min-height: calc(100vh - 61px);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
