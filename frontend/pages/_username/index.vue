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
                :src="user.avatar"
                :size="200"
              ></el-avatar>
            </div>
          </div>
        </el-col>
        <el-col class="z-999 relative" :span="14">
          <div class="grid-content">
            <el-link type="primary" :href="user.github">
              <h2>{{ user.name }}</h2>
            </el-link>

            <el-form class="mv4" label-width="100px">
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
};
</script>
