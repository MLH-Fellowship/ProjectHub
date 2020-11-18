<template>
  <div>
    <el-menu
      :default-active="activeRoute"
      mode="horizontal"
      @select="handleSelect"
    >
      <el-menu-item index="/">
        <img src="/logo.png" alt="Logo" style="max-height: 61px" />
      </el-menu-item>
      <el-menu-item index="#search">
        <el-input v-model="search" placeholder="Search"></el-input>
      </el-menu-item>
      <el-menu-item index="/projects">Projects</el-menu-item>
      <el-submenu index="4" style="float: right">
        <template slot="title">
          <!-- load profile image from state -->
          <el-avatar
            size="large"
            src="https://avatars0.githubusercontent.com/u/10343470?v=4"
          />
        </template>
        <el-menu-item index="#" disabled>Noah Cardoza</el-menu-item>
        <el-menu-item index="/NoahCardoza">Profile</el-menu-item>
        <el-menu-item index="/settings">Settings</el-menu-item>
      </el-submenu>
    </el-menu>
    <Nuxt />
  </div>
</template>

<script>
export default {
  data() {
    return {
      search: '',
      activeRoute: '1',
    };
  },
  methods: {
    handleSelect(key) {
      if (key !== '#') {
        this.$router.push(key);
      }
    },
  },
};
</script>

<style></style>
