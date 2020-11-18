<template>
  <div class="container">
    <div>
      <el-avatar :size="120" :src="user.avatar_url"></el-avatar>
    </div>
    <div>
      <a :href="user_github_url">
        <h1>{{ user.name }}</h1>
      </a>
    </div>
  </div>
</template>

<script>
import pick from 'ramda/src/pick';

export default {
  async asyncData({ params, $axios }) {
    const query = (...params) => {
      return $axios.$get(`https://api.github.com/${params.join('/')}`);
    };

    // API request to fill out page
    const details = {
      success: true,
      pods: ['1.0.1', '1.2.2'],
      projects: ['CaptchaHarvester'],
    };

    const [user, projects] = await Promise.all([
      query('users', params.username).then(
        pick([
          'login',
          'avatar_url',
          'name',
          'location',
          'email',
          'public_repos',
          'public_gists',
          'followers',
        ])
      ),
      Promise.all(
        details.projects.map((repository) =>
          query('repos', params.username, repository).then(
            pick([
              'name',
              'full_name',
              'private',
              'description',
              'fork',
              'html_url',
              'stargazers',
              'watchers',
              'language',
              'open_issues',
              'license',
              'forks',
            ])
          )
        )
      ),
    ]);

    return {
      user,
      projects,
    };
  },
  computed: {
    user_github_url() {
      return `https://github.com/${this.user.login}`;
    },
  },
};
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
