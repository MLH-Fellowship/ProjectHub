<template>
  <div>
    <br />
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
                :src="user.avatar_url"
                :size="200"
              ></el-avatar>
            </div>
          </div>
        </el-col>
        <el-col class="z-999 relative" :span="14">
          <div class="grid-content">
            <el-link type="primary" :href="user.html_url">
              <h2>{{ user.name }}</h2>
            </el-link>

            <el-form class="mv4" :model="form" label-width="100px">
              <el-form-item class="tl" label="Pods">1.0.1</el-form-item>

              <el-form-item class="tl" label="Interests">
                <el-select
                  v-model="form.interests"
                  multiple
                  placeholder="Select"
                  class="w-100"
                >
                  <el-option
                    v-for="interest in options.interests"
                    :key="interest.value"
                    :label="interest.label"
                    :value="interest.value"
                  ></el-option>
                </el-select>
              </el-form-item>

              <el-form-item class="tl" label="Skills">
                <el-select
                  v-model="form.skills"
                  multiple
                  placeholder="Select"
                  class="w-100"
                >
                  <el-option
                    v-for="skill in options.skills"
                    :key="skill.value"
                    :label="skill.label"
                    :value="skill.value"
                  ></el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="About">
                <el-input
                  v-model="user.bio"
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
    <ExploreLayout />
  </div>
</template>

<script>
import pick from 'ramda/src/pick';
import ExploreLayout from '@/components/ExploreLayout.vue';

export default {
  components: { ExploreLayout },
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
            'html_url',
            'avatar_url',
            'name',
            'location',
            'bio',
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

    user.bio = user.bio.trim();

    return {
      user,
      projects,
    };
  },
  data() {
    return {
      step: 0,
      visible: true,
      options: {
        interests: [
          { label: 'Front-end', value: 1 },
          { label: 'Back-end', value: 2 },
          { label: 'Python', value: 3 },
        ],
        skills: [
          { label: 'Android', value: 1 },
          { label: 'ML/AI', value: 2 },
          { label: 'Healthcare', value: 3 },
        ],
      },
      form: {
        skills: ['Android', 'Java', 'Javascript'],
        interests: ['Back-end', 'Networking'],
        bio:
          "I'm a senior software engineering student at SJSU, and a current MLH at Pod 1.0.1",
      },
    };
  },
  computed: {
    user_github_url() {
      return `https://github.com/${this.user.login}`;
    },
  },
  methods: {
    next() {
      this.step++;
    },
    back() {
      this.step--;
    },

    submit() {
      console.log(this.form);
      this.visible = false;
      this.$emit('complete');
    },
  },
};
</script>
