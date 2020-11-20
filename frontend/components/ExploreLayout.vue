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
          v-for="item in options.pods"
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
          v-for="item in options.languages"
          :key="item"
          :label="item"
          :value="item"
        ></el-option>
      </el-select>
    </div>
    <div class="grid w-100 pa3">
      <ProjectCard
        v-for="project in project_array"
        :key="project.id"
        class="ma3"
        :project="project"
      />
    </div>
  </div>
</template>

<script>
import ProjectCard from '@/components/ProjectCard';

export default {
  name: 'Dashboard',
  componentd: { ProjectCard },
  props: {
    projects: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      project_array: [
        {
          user: '@calvinqc',
          helpWanted: true,
          title: 'Event-bot',
          desc:
            'Discord Bot to make announcements about upcoming sessions for the Fellows using Google Calendar.',
          tags: ['Python', 'Pod 1.0.1', 'Discord'],
        },
        {
          user: '@calvinqc',
          helpWanted: true,
          title: 'Event-bot',
          desc:
            'Discord Bot to make announcements about upcoming sessions for the Fellows using Google Calendar.',
          tags: ['Python', '1.0.1', 'Discord'],
        },
      ],

      options: {
        pods: [
          '1.0.0',
          '1.0.1',
          '1.0.2',
          '1.0.3',
          '1.0.5',
          '1.0.6',
          '1.1.0',
          '1.1.1',
          '1.1.2',
          '1.1.3',
          '1.1.5',
          '1.1.6',
          '1.2.0',
          '1.2.1',
          '1.2.2',
        ],
        languages: [
          'Javascript',
          'Python',
          'Java',
          'Scala',
          'Golang',
          'Swift',
          'C',
          'C++',
          'C#',
          'OCaml',
          'PHP',
          'Rust',
          'Julia',
          'Cobol',
        ],
      },
      pods: [],
      languages: [],
    };
  },
  methods: {
    filter() {
      this.project_array.reduce((item) => {
        return item.tags.every((i) => this.pods.include(i));
      });
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
