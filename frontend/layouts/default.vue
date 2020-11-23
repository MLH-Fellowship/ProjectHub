<template>
  <div class="layout-default">
    <!-- can't figure out how to make navbar stick to top -->
    <div class="flex flex-row items-center">
      <div class="logo-wrapper" @click="$router.push('/')">
        <img
          :src="require('~/assets/images/logo.png')"
          alt="Logo"
          width="120px"
        />
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
          <el-menu-item class="never-active" @click.native.stop="github"
            >Github</el-menu-item
          >
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
            <el-menu-item
              index="logout"
              :route="{ path: '/' }"
              @click.native.stop="logout"
              >Logout</el-menu-item
            >
          </el-submenu>
          <el-menu-item
            v-if="!user.anonymous"
            style="float: right"
            class="never-active"
          >
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
            class="never-active"
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
      route: this.$route.fullUrl,
    };
  },
  computed: {
    ...mapState(['user']),
    login() {
      if (this.$route.query.redirect) {
        return this.$route.fullUrl;
      }

      if (this.$route.path === '/') {
        console.log(this.$route.path);
        return `/?login=1`;
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
.logo-wrapper {
  border-bottom: solid 1px #e6e6e6;
  background-color: #fff;
  line-height: 75px;
  text-align: center;
  width: 150px;
  height: 61px;
}

ul:not(.el-menu--popup) > li.el-menu-item {
  font-weight: 300;
  font-size: 1.5rem;
}

.layout-default >>> .el-menu-item.is-active:not(.never-active),
.layout-default >>> .el-submenu.is-active .el-submenu__title {
  border-bottom-color: #fbc6fd !important;
}

.layout-default >>> .never-active {
  border-bottom: none !important;
  color: #909399 !important;
}

.el-menu-item.is-active {
  font-weight: bolder;
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
