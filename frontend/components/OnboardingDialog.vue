<template>
  <div>
    <el-dialog class="pa4" width="700px;" :visible.sync="visible">
      <template v-if="step === 0">
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

                <el-form-item class="tl" label="My Interests">
                  <el-select
                    v-model="form.interests"
                    multiple
                    placeholder="Select"
                  >
                    <el-option
                      v-for="interest in options.interests"
                      :key="interest.value"
                      :label="interest.label"
                      :value="interest.value"
                    ></el-option>
                  </el-select>
                </el-form-item>

                <el-form-item class="tl" label="My Skills">
                  <el-select
                    v-model="form.skills"
                    multiple
                    placeholder="Select"
                  >
                    <el-option
                      v-for="skill in options.skills"
                      :key="skill.value"
                      :label="skill.label"
                      :value="skill.value"
                    ></el-option>
                  </el-select>
                </el-form-item>
              </el-form>
            </div>
          </el-col>
        </el-row>
        <span slot="footer" class="dialog-footer">
          <el-button round type="success" @click="next">Next</el-button>
        </span>
      </template>
      <template v-else>
        <h1 style="font-size: 2em; text-align: center">You're all set!</h1>
        <el-row>
          <el-col :span="8">
            <div class="grid-content">
              <h3>1. Explore</h3>
            </div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content">
              <h3>2. Connect</h3>
            </div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content">
              <h3>3. Collaborate</h3>
            </div>
          </el-col>
        </el-row>

        <span slot="footer" class="dialog-footer">
          <el-button round @click="back">Back</el-button>
          <el-button round type="primary" @click="submit">
            Get Started
          </el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'OnboardingDialog',
  data() {
    return {
      step: 0,
      visible: true,
      options: {
        interests: [
          { label: 'Android', value: 1 },
          { label: 'ML/AI', value: 2 },
          { label: 'Healthcare', value: 3 },
        ],
        skills: [
          { label: 'Front-end', value: 1 },
          { label: 'Back-end', value: 2 },
          { label: 'Python', value: 3 },
        ],
      },
      form: {
        skills: [],
        interests: [],
        bio: '',
      },
    };
  },
  computed: mapState(['user']),
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

<style>
.dialog-footer {
  text-align: end;
}

.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>
