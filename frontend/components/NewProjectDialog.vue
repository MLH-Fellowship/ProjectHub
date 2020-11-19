<template>
  <el-dialog
    :visible="value"
    :title="title"
    width="500px"
    :center="center"
    @update:visible="$emit('input', $event)"
  >
    <div v-loading="loading" :class="{ tc: center }">
      <div v-if="step === 0">
        <div>
          <el-button class="w-100" type="primary" @click="step = 1">
            Import from Github
          </el-button>
        </div>
        <div class="mt3">
          <el-button type="text" @click="step = 2">Start new project</el-button>
        </div>
      </div>
      <div v-else-if="step === 1">
        <div>
          <el-input v-model="form.source" />
        </div>
        <div class="mt3">
          <el-button class="w-100" type="primary" @click="importFromGithub">
            Import
          </el-button>
        </div>
      </div>
      <div v-else>
        <el-row type="flex" align="center">
          <el-col :span="6">Project Name</el-col>
          <el-col :span="18"><el-input v-model="form.title" /></el-col>
        </el-row>
        <el-row type="flex" align="center" class="mt3">
          <el-col :span="6">Description</el-col>
          <el-col :span="18"><el-input v-model="form.description" /></el-col>
        </el-row>
        <el-row type="flex" align="center" class="mt3">
          <el-col :span="6">Source Link</el-col>
          <el-col :span="18"><el-input v-model="form.source" /></el-col>
        </el-row>
        <el-row type="flex" align="center" class="mt3">
          <el-col :span="6">Demo Link</el-col>
          <el-col :span="18"><el-input v-model="form.demo" /></el-col>
        </el-row>
        <el-row type="flex" align="center" class="mv3">
          <el-col :span="6">Tags</el-col>
          <el-col :span="18">
            <el-tag
              v-for="tag in form.tags"
              :key="tag"
              closable
              :disable-transitions="false"
              @close="removeTag(tag)"
            >
              {{ tag }}
            </el-tag>
            <el-input
              v-if="tags.inputVisible"
              ref="saveTagInput"
              v-model="tags.inputValue"
              class="input-new-tag"
              size="mini"
              placeholder="add-tag"
              @keyup.enter.native="handleInputConfirm"
              @blur="handleInputConfirm"
            ></el-input>
          </el-col>
        </el-row>
        <el-button class="w-100" type="primary" @click="createNewProject">
          Submit
        </el-button>
      </div>
    </div>
  </el-dialog>
</template>

<script>
const initForm = () => ({
  imported: false,
  title: '',
  description: '',
  source: '',
  demo: '',
  tags: [],
});

export default {
  name: 'NewProjectDialog',
  components: {},
  props: {
    value: {
      required: true,
      type: Boolean,
    },
  },
  data() {
    return {
      step: 0,
      loading: false,
      form: initForm(),
      tags: {
        inputVisible: true,
        inputValue: '',
      },
    };
  },
  computed: {
    title() {
      return [
        'How would you like to add the project?',
        'Enter a Github project URL!',
        this.form.imported
          ? 'How does this look?'
          : 'Tell us about your project!',
      ][this.step];
    },
    center() {
      return this.step !== 2;
    },
  },
  watch: {
    value(val) {
      if (val) {
        this.step = 0;
        this.form = initForm();
      }
    },
  },
  mounted() {},
  beforeDestroy() {},
  methods: {
    async importFromGithub() {
      // TODO: error checking to make sure the url/repo is valid
      this.loading = true;
      const url = new URL(this.form.source);
      const [login, repository] = url.pathname.slice(1).split('/', 2);
      const [{ description, homepage }, { names }] = await Promise.all([
        this.$github.get('repos', login, repository),
        this.$github.get('repos', login, repository, 'topics'),
      ]);
      this.form.imported = true;
      this.form.title = repository;
      this.form.description = description;
      this.form.demo = homepage;
      this.form.tags = names;
      this.step = 2;
      this.loading = false;
    },
    createNewProject() {
      // TODO: post to api
      // this.$axios.$post('/api/project/new', this.form)
    },
    removeTag(tag) {
      this.form.tags.splice(this.form.tags.indexOf(tag), 1);
    },
    showInput() {
      this.inputVisible = true;
      this.$nextTick((_) => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },
    handleInputConfirm() {
      const inputValue = this.tags.inputValue;
      if (inputValue) {
        this.form.tags.push(inputValue);
      }
      this.inputVisible = false;
      this.tags.inputValue = '';
    },
  },
};
</script>

<style lang="css" scoped>
.el-tag {
  margin-right: 10px;
  margin-bottom: 10px;
}

.input-new-tag {
  width: 90px;
}
</style>
