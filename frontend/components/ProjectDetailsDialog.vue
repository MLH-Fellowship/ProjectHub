<template>
  <el-dialog
    :visible="value"
    :title="title"
    body-style="max-width: 1000px"
    :center="center"
    :append-to-body="nestedDialog"
    @update:visible="$emit('input', $event)"
  >
    <div v-loading="loading" :class="{ tc: center }">
      <div v-if="step === 0">
        <div>
          <el-button
            class="w-100"
            type="primary"
            @click="startImportFromGithub"
          >
            Import from Github
          </el-button>
        </div>
        <div class="mt3">
          <el-button type="text" @click="step = 2">Start new project</el-button>
        </div>
      </div>
      <div v-else-if="step === 1">
        <div>
          <el-input ref="githubLinkInput" v-model="form.source" />
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
          <el-col :span="18"><el-input v-model="form.name" /></el-col>
        </el-row>
        <el-row type="flex" align="center" class="mt3">
          <el-col :span="6">Description</el-col>
          <el-col :span="18">
            <el-input v-model="form.description" type="textarea" />
          </el-col>
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
            <EditableTagsGroup :tags="form.tags" slug placeholder="Tag" />
          </el-col>
        </el-row>
        <el-row type="flex" align="center" class="mv3">
          <el-col :span="6">Lanuages</el-col>
          <el-col :span="18">
            <EditableTagsGroup :tags="form.languages" placeholder="Lanuage" />
          </el-col>
        </el-row>
        <el-row type="flex" align="center" class="mv3">
          <el-col :span="6">State</el-col>
          <el-col :span="18">
            <el-radio-group v-model="form.state" size="mini">
              <el-radio-button label="None" />
              <el-radio-button label="Need Help" />
              <el-radio-button label="Featured" />
            </el-radio-group>
          </el-col>
        </el-row>
        <el-button class="w-100" type="primary" @click="submit">
          Submit
        </el-button>
      </div>
    </div>
  </el-dialog>
</template>

<script>
import { mapState } from 'vuex';
import EditableTagsGroup from '@/components/EditableTagsGroup';
import toSlug from '@/utils/toSlug';

const initForm = (project) =>
  project
    ? { ...project, state: project.state || 'None' }
    : {
        name: '',
        description: '',
        source: '',
        demo: '',
        tags: [],
        languages: [],
        state: 'None',
      };

export default {
  name: 'ProjectDetailsDialog',
  components: { EditableTagsGroup },
  props: {
    value: {
      required: true,
      type: Boolean,
    },
    project: {
      default: null,
      type: Object,
    },
    nestedDialog: {
      default: false,
      type: Boolean,
    },
  },
  data() {
    return {
      step: this.project ? 2 : 0,
      loading: false,
      imported: false,
      form: initForm(this.project),
    };
  },
  computed: {
    ...mapState(['user']),
    title() {
      return [
        'How would you like to add the project?',
        'Enter a Github project URL!',
        this.project
          ? 'What would you like to update?'
          : this.imported
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
        this.step = this.project ? 2 : 0;
        this.form = initForm(this.project);
      }
    },
  },
  methods: {
    startImportFromGithub() {
      this.step = 1;
      this.$nextTick(() => {
        console.log(this.$refs.githubLinkInput);
        this.$refs.githubLinkInput.focus();
      });
    },
    async importFromGithub() {
      // TODO: error checking to make sure the url/repo is valid
      this.loading = true;
      const url = new URL(this.form.source);
      const [login, repository] = url.pathname.slice(1).split('/', 2);
      // https://github.com/NoahCardoza/CaptchaHarvester
      const [
        { description, homepage },
        { names },
        languages,
      ] = await Promise.all([
        this.$github.get('repos', login, repository),
        this.$github.get('repos', login, repository, 'topics'),
        this.$github.get('repos', login, repository, 'languages'),
      ]);
      this.imported = true;
      this.form.name = repository;
      this.form.description = description || '';
      this.form.demo = homepage || '';
      this.form.tags = names.map(toSlug);
      this.form.languages = Object.keys(languages);
      this.step = 2;
      this.loading = false;
    },
    async submit() {
      this.loading = true;
      const form = {
        ...this.form,
        state: this.form.sate === 'None' ? null : this.form.sate,
      };

      if (this.project) {
        Object.assign(this.project, form);
        await this.$axios.$put('/api/project', this.project);
      } else {
        const project = await this.$axios.$post('/api/project', form);
        this.$router.push(`/${this.user.meta.login}?project=${project.slug}`);
        this.$nuxt.refresh();
      }
      this.$emit('input', false);
      this.loading = false;
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
