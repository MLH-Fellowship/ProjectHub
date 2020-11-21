<template>
  <div class="pa3 tl">
    <p class="f4 b mb3">Project Overview</p>

    <div class="flex flex-row f5 mt3">
      <iconify-icon icon="code-tags" class="mr2" />
      <span style="word-break">
        {{ project.languages | joinWithComma }}
      </span>
    </div>

    <!-- <div class="flex flex-row f5 mt3">
      <iconify-icon icon="group" class="mr2" />
      Jordan, Noah, Calvin
    </div> -->

    <div class="flex flex-row f5 mt3">
      <iconify-icon icon="github" class="mr2" />
      <el-link :href="project.source">View Github</el-link>
    </div>

    <div class="flex flex-row f5 mt3">
      <iconify-icon icon="tags" class="mr2" />
      Tags
    </div>

    <ProjectTags class="mt3 mb2" :tags="project.tags" />
  </div>
</template>

<script>
import IconifyIcon from '@iconify/vue';
import CodeTags from '@iconify/icons-mdi/code-tags';
import TagMultiple from '@iconify/icons-mdi/tag-multiple';
import Clock from '@iconify/icons-mdi/clock-time-four-outline';
import Group from '@iconify/icons-mdi/account-group';
import Github from '@iconify/icons-mdi/github';

import ProjectTags from '@/components/ProjectTags';

IconifyIcon.addIcon('tag-multiple', TagMultiple);
IconifyIcon.addIcon('code-tags', CodeTags);
IconifyIcon.addIcon('clock', Clock);
IconifyIcon.addIcon('group', Group);
IconifyIcon.addIcon('github', Github);

export default {
  name: 'ProjectOverview',
  components: {
    IconifyIcon,
    ProjectTags,
  },
  props: {
    project: { type: Object, required: true },
  },
};
</script>
