<template>
  <div class="mt4">
    <div class="flex flex-row flex-wrap justify-center">
      <div class="f3 lh-copy">Filters:</div>
      <el-select
        v-model="pods"
        multiple
        filterable
        allow-create
        default-first-option
        placeholder="Pods"
        class="mh3"
      >
        <el-option
          v-for="item in podOptions"
          :key="item"
          :label="item"
          :value="item"
        ></el-option>
      </el-select>
      <el-select
        v-model="languages"
        multiple
        filterable
        allow-create
        default-first-option
        placeholder="Lanuages"
      >
        <el-option
          v-for="item in languageOptions"
          :key="item"
          :label="item"
          :value="item"
        ></el-option>
      </el-select>
    </div>
    <div class="grid w-100 pa3">
      <ProjectCard
        v-for="project in filterd"
        :key="project.id"
        class="ma3"
        :project="project"
      />
    </div>
  </div>
</template>

<script>
import ProjectCard from '@/components/ProjectCard';

const someIncludes = (a, b) => {
  const s = new Set(b);
  console.log(a, b, s);
  return a.some((e) => s.has(e));
};

export default {
  name: 'Dashboard',
  componentd: { ProjectCard },
  props: {
    projects: {
      type: Array,
      required: true,
    },
    podOptions: {
      type: Array,
      required: true,
    },
    languageOptions: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      pods: [],
      languages: [],
    };
  },
  computed: {
    filterd() {
      let filtered = null;

      if (this.pods.length) {
        filtered = (filtered || this.projects).filter((project) =>
          someIncludes(this.pods, project.user.pods)
        );
      }

      if (this.languages.length) {
        filtered = (filtered || this.projects).filter((project) =>
          someIncludes(this.languages, project.languages)
        );
      }

      return filtered || this.projects;
    },
  },
};
</script>

<style scoped>
.grid {
  display: flex;
  flex-flow: row wrap;
  justify-content: center;
}
</style>
