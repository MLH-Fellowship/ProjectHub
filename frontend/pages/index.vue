<template>
  <div class="container overflow-hidden pa3" style="justify-content: none">
    <el-row class="items-center w-100">
      <el-col :offset="2" :xs="22" :sm="14" :md="10">
        <div class="tl relative z-1">
          <p class="f1">Welcome to</p>
          <p class="b mv3" style="font-size: 5em">Project Hub</p>
          <p class="mt5">
            Introducing a new way to find and share your projects
          </p>
          <div class="mt4">
            <el-button round type="primary">Explore Projects</el-button>
            <GithubLoginButton v-if="user.anonymous" />
          </div>
        </div>
      </el-col>
      <el-col :xs="1" :sm="8" :md="12" class="hidden-xs-only">
        <el-image
          class="relative z-0"
          style="top: 50px; left: -100px; width: 120%"
          :src="require('~/assets/images/humans1.png')"
        ></el-image>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import GithubLoginButton from '@/components/GithubLoginButton';
import 'element-ui/lib/theme-chalk/display.css';

export default {
  name: 'LandingPage',
  components: { GithubLoginButton },
  computed: mapState(['user']),
};
</script>

<style></style>
