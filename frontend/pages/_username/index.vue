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
  async asyncData({ params, $axios, $github }) {
    // API request to fill out page
    const details = {
      success: true,
      pods: ['1.0.1', '1.2.2'],
      projects: ['NoahCardoza/CaptchaHarvester'],
    };

    const [user, projects] = await Promise.all([
      $github
        .get('users', params.username)
        .then(
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
          $github
            .get('repos', repository)
            .then(
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

<style></style>
