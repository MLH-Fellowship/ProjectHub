<template>
  <el-card>
    <ProjectOverview />
  </el-card>
</template>

<script>
import ProjectOverview from './index';

export default {
  name: 'ProjectOverviewCard',
  components: {
    ProjectOverview,
  },
  props: {},
};
</script>
