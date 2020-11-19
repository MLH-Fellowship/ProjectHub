<template>
  <div class="container overflow-hidden">
    <el-row class="items-center mw8">
      <el-col :span="16">
        <div class="tl">
          <p class="f1">Welcome to</p>
          <p class="b mv3" style="font-size: 5em">Project Hub</p>
          <p class="mt5">
            Introducing a new way to find and share your projects
          </p>
          <div class="mt4">
            <el-button round type="primary">Explore Projects</el-button>
            <GithubLoginButton v-if="!user.token" />
          </div>
        </div>
      </el-col>
      <el-col :span="8">
        <el-image
          class="relative"
          style="top: 50px; left: -300px; width: 700px"
          src="/humans1.png"
        ></el-image>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import GithubLoginButton from '@/components/GithubLoginButton';

export default {
  name: 'LandingPage',
  components: { GithubLoginButton },
  computed: mapState(['user']),
};
</script>

<style></style>
