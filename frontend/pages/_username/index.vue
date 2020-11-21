<template>
  <div>
    <div style="margin-left: 200px">
      <el-row>
        <el-col :span="6">
          <div class="grid-content">
            <div class="relative" style="height: 270px">
              <el-image
                class="absolute"
                style="top: 0; left: 0; width: 400px"
                :src="require('~/assets/images/blob1.png')"
              ></el-image>
              <el-avatar
                class="absolute ma4"
                style="top: 0; left: 0"
                icon="el-icon-user-solid"
                :src="ghUser.avatar_url"
                :size="200"
              ></el-avatar>
            </div>
          </div>
        </el-col>
        <el-col class="z-999 relative" :span="14">
          <div class="grid-content">
            <el-link type="primary" :href="ghUser.html_url">
              <h2>{{ ghUser.name }}</h2>
            </el-link>

            <el-form class="mv4" :model="form" label-width="100px">
              <el-form-item class="tl" label="Pods">
                {{ user.pods | joinWithComma }}
              </el-form-item>

              <el-form-item class="tl" label="Interests">
                <el-select
                  v-model="user.interests"
                  :disabled="!isUsersOwnPage"
                  multiple
                  placeholder="Select"
                  class="w-100"
                >
                  <el-option
                    v-for="interest in options.interests"
                    :key="interest"
                    :label="interest"
                    :value="interest"
                  ></el-option>
                </el-select>
              </el-form-item>

              <el-form-item class="tl" label="Skills">
                <el-select
                  v-model="user.skills"
                  :disabled="!isUsersOwnPage"
                  multiple
                  placeholder="Select"
                  class="w-100"
                >
                  <el-option
                    v-for="skill in options.skills"
                    :key="skill"
                    :label="skill"
                    :value="skill"
                  ></el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="About">
                <el-input
                  v-model="user.bio"
                  :disabled="!isUsersOwnPage"
                  type="textarea"
                  placeholer="Write a short bio..."
                ></el-input>
              </el-form-item>
            </el-form>
          </div>
        </el-col>
      </el-row>
    </div>
    <hr />
    <ExploreLayout :projects="user.projects" />
  </div>
</template>

<script>
import pick from 'ramda/src/pick';
import ExploreLayout from '@/components/ExploreLayout.vue';

export default {
  components: { ExploreLayout },
  async asyncData({ params, $axios, $github, error }) {
    let user;
    try {
      user = await $axios.$get(`/api/user/${params.username}`);
    } catch (e) {
      return error({ statusCode: 404, message: 'User not found' });
    }

    const ghUser = await $github
      .get('users', params.username)
      .then(pick(['html_url', 'avatar_url']));

    const userMini = {
      ...pick(['login', 'name', 'bio'], user),
      ...ghUser,
    };

    user.projects = user.projects.map((project) => ({
      ...project,
      user: userMini,
    }));

    console.log(user);

    return {
      user,
      ghUser,
    };
  },
  data() {
    return {
      step: 0,
      visible: true,
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
  methods: {
    next() {
      this.step++;
    },
    back() {
      this.step--;
    },

    // submit() {
    //   this.visible = false;
    //   this.$emit('complete');
    // },
  },
};
</script>
