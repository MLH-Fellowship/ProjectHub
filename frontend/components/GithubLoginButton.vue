<template>
  <div class="dib">
    <el-button ref="button" round @click="authenticate">
      Login With GitHub
    </el-button>
    <OnboardingDialog v-model="onBoarding" on-boarding @complete="finish" />
  </div>
</template>

<script>
import { mapState } from 'vuex';
import OnboardingDialog from '@/components/OnboardingDialog';

export default {
  name: 'GithubLoginButton',
  components: { OnboardingDialog },
  data() {
    return {
      loginFlow: null,
      onBoarding: false,
      interval: null,
    };
  },
  computed: {
    ...mapState(['user']),
    bounce() {
      return this.$route.query.login === '1';
    },
  },
  mounted() {
    if (this.bounce) {
      const { classList } = this.$refs.button.$el;
      let flag = true;
      classList.add('bounce');
      this.interval = setInterval(() => {
        if (flag) {
          classList.remove('bounce');
        } else {
          classList.add('bounce');
        }
        flag = !flag;
      }, 1500);
    }
  },
  destroyed() {
    clearInterval(this.interval);
  },
  methods: {
    async authenticate() {
      const { code } = await this.$auth.authenticate('github');

      this.loginFlow = await this.$store.dispatch('user/login', code);
      this.onBoarding = this.loginFlow.onBoarding;

      if (this.onBoarding) {
        return;
      }

      this.finish();
    },
    finish() {
      this.loginFlow.finish();
      this.$router.push(this.$route.query.redirect || '/explore');
    },
  },
};
</script>

<style>
@keyframes bounce {
  0%,
  100% {
    transform: scale(1) translateY(0px);
  }
  50% {
    transform: scale(1.05) translateY(-5px);
  }
}
.bounce {
  animation-duration: 0.5s;
  animation-fill-mode: both;
  animation-timing-function: cubic-bezier(0.25, 0.1, 0, 2.05);
  animation-iteration-count: 1;
  animation-name: bounce;
}
</style>
