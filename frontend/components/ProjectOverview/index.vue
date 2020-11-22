<template>
  <div class="tl">
    <p v-if="title" class="f4 b mb3">Project Overview</p>

    <div v-if="project.languages.length" class="flex flex-row f5">
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
      <template v-if="isGithub">
        <iconify-icon icon="github" class="mr2" />
        <el-link :href="project.source" target="_blank" @click.native.stop>
          View Github
        </el-link>
      </template>
      <template v-else>
        <iconify-icon icon="test-tube" class="mr2" />
        <el-link :href="project.source" target="_blank" @click.native.stop>
          View Project
        </el-link>
      </template>
    </div>

    <div v-if="project.demo" class="flex flex-row f5 mt3">
      <iconify-icon icon="airballoon" class="mr2" />
      <el-link :href="project.demo" target="_blank" @click.native.stop>
        View Demo
      </el-link>
    </div>

    <div v-if="project.tags.length">
      <div class="flex flex-row f5 mt3">
        <iconify-icon icon="tags" class="mr2" />
        Tags
      </div>
      <ProjectTags class="mt3 mb2" :tags="project.tags" />
    </div>
  </div>
</template>

<script>
import IconifyIcon from '@iconify/vue';
import CodeTags from '@iconify/icons-mdi/code-tags';
import TagMultiple from '@iconify/icons-mdi/tag-multiple';
import Clock from '@iconify/icons-mdi/clock-time-four-outline';
import Group from '@iconify/icons-mdi/account-group';
import Github from '@iconify/icons-mdi/github';
import TestTube from '@iconify/icons-mdi/test-tube';
import AirBalloon from '@iconify/icons-mdi/airballoon';

import ProjectTags from '@/components/ProjectTags';

IconifyIcon.addIcon('tag-multiple', TagMultiple);
IconifyIcon.addIcon('code-tags', CodeTags);
IconifyIcon.addIcon('clock', Clock);
IconifyIcon.addIcon('group', Group);
IconifyIcon.addIcon('github', Github);
IconifyIcon.addIcon('test-tube', TestTube);
IconifyIcon.addIcon('airballoon', AirBalloon);

export default {
  name: 'ProjectOverview',
  components: {
    IconifyIcon,
    ProjectTags,
  },
  props: {
    project: { type: Object, required: true },
    title: { type: Boolean, default: true },
  },
  computed: {
    isGithub() {
      return this.project.source.includes('://github.com');
    },
  },
};
</script>
