<template>
  <div>
    <UserDetails class="mt4 mh5" :disabled="!isUsersOwnPage" :user="user" />
    <hr />
    <ExploreLayout
      :projects="user.explorer.projects"
      :pod-options="user.explorer.pods"
      :language-options="user.explorer.languages"
      user-page
    />
  </div>
</template>

<script>
import pick from 'ramda/src/pick';
import ExploreLayout from '@/components/ExploreLayout.vue';

async function updateUser() {
  await this.$axios.$put(
    '/api/user',
    pick(['bio', 'pods', 'interests', 'skills'], this.user)
  );
}

export default {
  components: { ExploreLayout },
  async asyncData({ params, $axios, $github, error }) {
    try {
      const user = await $axios.$get(`/api/user/${params.username}`);
      const microUser = pick(
        ['login', 'name', 'bio', 'pods', 'avatar', 'github'],
        user
      );

      user.explorer.projects = user.explorer.projects.map((project) => ({
        ...project,
        user: microUser,
      }));

      return {
        user,
      };
    } catch (e) {
      return error({ statusCode: 404, message: 'User not found' });
    }
  },
  data() {
    return {
      options: {
        interests: ['Front-end', 'Back-end', 'Python'],
        skills: ['Android', 'ML/AI', 'Healthcare'],
      },
    };
  },
  computed: {
    isUsersOwnPage() {
      return this.$store.state.user.meta.login === this.$route.params.username;
    },
  },
  watch: {
    user() {
      console.log('user');
    },
    'user.bio'() {
      console.log('user.bio');
    },
    'user.pods': updateUser,
    'user.interests': updateUser,
    'user.skills': updateUser,
  },
  // methods: {
  //   updateUser() {
  //     console.log(omit(['projects'], this.user));
  //     // this.$axios.$put('/api/user', omit)
  //   },
  // },
};
</script>
