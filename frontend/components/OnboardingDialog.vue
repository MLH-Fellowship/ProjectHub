<template>
  <el-dialog
    class="pa4"
    width="90%"
    body-style="max-width: 1000px"
    :visible="value"
    @update:visible="$emit('input', $event)"
  >
    <div v-if="step === 0" v-loading="loading">
      <el-row>
        <el-col :span="10">
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
                :src="user.meta.avatar"
                :size="200"
              ></el-avatar>
            </div>
          </div>
        </el-col>
        <el-col class="z-999 relative" :span="14">
          <div class="grid-content">
            <h2>Tell us a bit about yourself...</h2>

            <el-form class="mv4" :model="form" label-width="100px">
              <el-form-item label="About Me">
                <el-input
                  v-model="form.bio"
                  type="textarea"
                  placeholer="Write a short bio..."
                ></el-input>
              </el-form-item>
              <el-form-item class="tl" label="Pod(s)">
                <el-select
                  v-model="form.pods"
                  multiple
                  placeholder="Select"
                  class="w-100"
                >
                  <el-option
                    v-for="pod in options.pods"
                    :key="pod"
                    :label="pod"
                    :value="pod"
                  ></el-option>
                </el-select>
              </el-form-item>
              <el-form-item class="tl" label="Interests">
                <EditableTagsGroup
                  :tags="form.interests"
                  placeholder="Interest"
                />
              </el-form-item>
              <el-form-item class="tl" label="Skills">
                <EditableTagsGroup :tags="form.skills" placeholder="Skill" />
              </el-form-item>
            </el-form>
          </div>
        </el-col>
      </el-row>
      <div style="text-align: end">
        <el-button round type="primary" @click="next">Next</el-button>
      </div>
    </div>
    <div v-show="step === 1">
      <h1 class="black" style="font-size: 2em; text-align: center">
        You're all set!
      </h1>
      <el-row class="flex flex-row items-center tc">
        <el-col :span="8">
          <div class="grid-content">
            <el-image
              class="pa4 w-100"
              :src="require('~/assets/images/explore.png')"
            ></el-image>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="grid-content">
            <el-image
              class="pa4 w-100"
              :src="require('~/assets/images/create.png')"
            ></el-image>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="grid-content">
            <el-image
              class="pa4 w-100"
              :src="require('~/assets/images/collaborate.png')"
            ></el-image>
          </div>
        </el-col>
      </el-row>
      <el-row class="flex flex-row items-center tc black">
        <el-col>
          <h3>1. Explore</h3>
        </el-col>
        <el-col>
          <h3>2. Create</h3>
        </el-col>
        <el-col>
          <h3>3. Collaborate</h3>
        </el-col>
      </el-row>

      <div class="mt4 mh3 flex justify-between">
        <el-button type="text" @click="back">Back</el-button>
        <el-button round type="primary" @click="submit">Get Started!</el-button>
      </div>
    </div>
  </el-dialog>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'OnboardingDialog',
  props: {
    value: {
      type: Boolean,
      required: true,
    },
    onBoarding: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      loading: false,
      step: 0,
      options: {
        pods: [
          'Pod 1.0.0',
          'Pod 1.0.1',
          'Pod 1.0.2',
          'Pod 1.0.3',
          'Pod 1.0.5',
          'Pod 1.0.6',
          'Pod 1.1.0',
          'Pod 1.1.1',
          'Pod 1.1.2',
          'Pod 1.1.3',
          'Pod 1.1.5',
          'Pod 1.1.6',
          'Pod 1.2.0',
          'Pod 1.2.1',
          'Pod 1.2.2',
        ],
      },
      form: {
        bio: '',
        pods: [],
        skills: [],
        interests: [],
      },
    };
  },
  computed: mapState(['user']),
  watch: {
    async value(val) {
      if (val && this.onBoarding) {
        this.loading = true;
        const user = await this.$github.get('users', this.user.meta.login);
        this.form.bio = user.bio.trim();
        this.loading = false;
      }
    },
  },
  methods: {
    next() {
      this.step++;
    },
    back() {
      this.step--;
    },
    async submit() {
      const payload = {
        ...this.form,
        timezone_offset: new Date().getTimezoneOffset() / 60,
      };
      await this.$axios.$post('/api/user', payload);
      this.visible = false;
      this.$emit('complete');
    },
  },
};
</script>

<style></style>
