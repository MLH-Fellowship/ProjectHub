<template>
  <el-row>
    <el-col :span="10">
      <div class="grid-content">
        <div class="relative" style="height: 270px">
          <el-image
            class="absolute"
            style="top: 0; left: 0; width: 400px"
            :src="require('~/assets/images/blob1.png')"
          ></el-image>
          <div class="absolute ma4 tc" style="top: 0; left: 0">
            <el-avatar
              icon="el-icon-user-solid"
              :src="avatar || user.avatar"
              :size="200"
            ></el-avatar>
            <el-link type="primary" :href="user.github" target="_blank">
              <h2 class="mt2">{{ user.name }}</h2>
            </el-link>
          </div>
        </div>
      </div>
    </el-col>
    <el-col class="z-999 relative" :span="14">
      <div class="grid-content">
        <slot />
        <el-form class="mv4" :model="form" label-width="100px">
          <el-form-item label="About Me">
            <el-input
              v-model="user.bio"
              class="user-details-bio"
              type="textarea"
              placeholer="Write a short bio..."
              rows="4"
              :disabled="disabled"
            ></el-input>
          </el-form-item>
          <el-form-item class="tl" label="Pod(s)">
            <el-select
              v-model="user.pods"
              multiple
              placeholder="Select"
              class="w-100"
              :disabled="disabled"
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
              :tags="user.interests"
              placeholder="Interest"
              :disabled="disabled"
              slug
            />
          </el-form-item>
          <el-form-item class="tl" label="Skills">
            <EditableTagsGroup
              :tags="user.skills"
              placeholder="Skill"
              :disabled="disabled"
            />
          </el-form-item>
        </el-form>
      </div>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: 'UserDetails',
  props: {
    user: {
      type: Object,
      required: true,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    avatar: {
      type: String,
      default: null,
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
  methods: {},
};
</script>

<style>
.user-details-bio.is-disabled textarea[disabled].el-textarea__inner {
  color: #909399 !important;
}
</style>
