import Vue from 'vue';
import VueSocialauth from 'vue-social-auth';

import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(VueAxios, axios);

Vue.use(VueSocialauth, {
  providers: {
    github: {
      clientId: process.env.GITHUB_CLIENT_ID,
      redirectUri: 'http://localhost:3000/callback/github',
      scope: [
        'user',
        'admin:org',
        'repo',
        'admin:repo_hook',
        'admin:enterprise',
      ],
    },
  },
});
