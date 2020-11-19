<template>
  <div>
    <el-dialog class="pa4" width="700px;" :visible.sync="dialog1Visible">
      <el-row>
        <el-col :span="10">
          <div class="grid-content">
            <div class="relative" style="height: 270px">
              <el-image
                class="absolute"
                style="top: 0; left: 0; width: 400px"
                src="/blob1.png"
                :fit="fit"
              ></el-image>
              <el-avatar
                class="absolute ma4"
                style="top: 0; left: 0"
                icon="el-icon-user-solid"
                src="pfpUrl"
                :size="200"
              ></el-avatar>
            </div>
            <el-button
              class="z-999 relative"
              round
              @click="pfpDialogVisible = 'true'"
            >
              Change photo
            </el-button>
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
                  v-model="form.userInterests"
                  multiple
                  placeholder="Select"
                >
                  <el-option
                    v-for="interest in form.interests"
                    :key="interest.value"
                    :label="interest.label"
                    :value="interest.value"
                  ></el-option>
                </el-select>
              </el-form-item>

              <el-form-item class="tl" label="My Skills">
                <el-select
                  v-model="form.userSkills"
                  multiple
                  placeholder="Select"
                >
                  <el-option
                    v-for="skill in form.skills"
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
        <el-button round @click="dialog1Visible = false">Back</el-button>
        <el-button
          round
          type="primary"
          @click="(dialog2Visible = true), (dialog1Visible = false)"
        >
          Next
        </el-button>
      </span>
    </el-dialog>

    <!-- Dialog to change profile picture -->
    <el-dialog :visible.sync="pfpDialogVisible" width="300px">
      <p class="mb4">Upload a new profile picture</p>
      <el-upload
        class="avatar-uploader"
        action="https://jsonplaceholder.typicode.com/posts/"
        :show-file-list="false"
        :on-success="handleAvatarSuccess"
        :before-upload="beforeAvatarUpload"
      >
        <img v-if="imageUrl" :src="imageUrl" class="avatar" />
        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
      </el-upload>
    </el-dialog>

    <!-- Tutorial dialog -->
    <el-dialog :visible.sync="dialog2Visible" center>
      <h1 style="font-size: 2em; text-align: center">You're all set!</h1>
      <el-row>
        <el-col :span="8">
          <div class="grid-content">
            <el-image src="/blob1.png" :fit="fit"></el-image>
            <h3>1. Explore</h3>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="grid-content">
            <el-image src="/blob1.png" :fit="fit"></el-image>
            <h3>2. Connect</h3>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="grid-content">
            <el-image src="/blob1.png" :fit="fit"></el-image>
            <h3>3. Collaborate</h3>
          </div>
        </el-col>
      </el-row>

      <span slot="footer" class="dialog-footer">
        <el-button
          round
          @click="(dialog1Visible = true), (dialog2Visible = false)"
        >
          Back
        </el-button>
        <el-button round type="primary" @click="dialog2Visible = false">
          Get Started
        </el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'OnboardingDialog',
  data() {
    return {
      dialog1Visible: true,
      dialog2Visible: false,
      pfpDialogVisible: false,
      pfpUrl: '',
      userName: 'Calvin',
      imageUrl: '',
      form: {
        pods: [
          { label: '1.0.1', value: 1 },
          { label: '1.0.2', value: 2 },
          { label: '1.0.3', value: 3 },
        ],
        timezones: [
          { label: 'EST (Eastern Standard Time)', value: 1 },
          { label: 'GMT (Greenwich Mean Time)', value: 2 },
          { label: 'PST (Pacific Standard Time)', value: 3 },
        ],
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
        contact: '',
        userSkills: [],
        userInterests: [],
        bio: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: '',
      },
      formLabelWidth: '50%',
    };
  },
  methods: {
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg';
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error('Avatar picture must be JPG format!');
      }
      if (!isLt2M) {
        this.$message.error('Avatar picture size can not exceed 2MB!');
      }
      return isJPG && isLt2M;
    },
  },
};
</script>

<style>
h1,
h2,
h4,
h5,
h6 {
  text-align: left;
}

h3 {
  text-align: center;
}

.mt-2 {
  margin-top: ;
}

.el-input {
  align-self: flex-start;
}

.dialog-footer {
  text-align: end;
}

.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>
