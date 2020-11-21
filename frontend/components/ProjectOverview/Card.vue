<template>
  <el-card>
    <ProjectOverview :project="project" />
  </el-card>
</template>

<script>
import ProjectOverview from './index';

export default {
  name: 'ProjectOverviewCard',
  components: {
    ProjectOverview,
  },
  props: {
    project: { type: Object, required: true },
  },
};
</script>
