import Vue from 'vue';
import VueSocialauth from 'vue-social-auth';

import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(VueAxios, axios);

Vue.use(VueSocialauth, {
  providers: {
    github: {
      clientId: process.env.GITHUB_CLIENT_ID,
      redirectUri: `${process.env.FRONTEND_BASE_URL}/callback/github`,
      scope: ['read:user', 'read:org'],
    },
  },
});
