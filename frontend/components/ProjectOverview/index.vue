<template>
  <div class="pa3 tl">
    <p class="f4 b mb3">Project Overview</p>

    <div class="flex flex-row f5 mt3">
      <iconify-icon icon="code" class="mr2" />
      {{ details.languages.join(', ') }}
    </div>

    <!-- <div class="flex flex-row f5 mt3">
      <iconify-icon icon="group" class="mr2" />
      Jordan, Noah, Calvin
    </div> -->

    <div class="flex flex-row f5 mt3">
      <iconify-icon icon="github" class="mr2" />
      <el-link :href="details.source">View Github</el-link>
    </div>

    <div class="flex flex-row f5 mt3">
      <iconify-icon icon="tags" class="mr2" />
      Tags
    </div>

    <div v-for="tag in details.tags" :key="tag" class="mt3 mb2"></div>

    <div class="mt3 mb2">
      <el-tag
        v-for="tag in details.tags"
        :key="tag"
        :color="tag | hexHash"
        class="project-tag mb1"
      >
        {{ tag }}
      </el-tag>
    </div>
  </div>
</template>

<script>
import IconifyIcon from '@iconify/vue';
import TagMultiple from '@iconify/icons-mdi/tag-multiple';
import Clock from '@iconify/icons-mdi/clock-time-four-outline';
import Group from '@iconify/icons-mdi/account-group';
import Github from '@iconify/icons-mdi/github';

IconifyIcon.addIcon('tags', TagMultiple);
IconifyIcon.addIcon('clock', Clock);
IconifyIcon.addIcon('group', Group);
IconifyIcon.addIcon('github', Github);

export default {
  name: 'ProjectOverview',
  components: {
    IconifyIcon,
  },
  props: {},
  data() {
    return {
      details: {
        title: 'Project Title',
        source: 'https://github.com/MLH-Fellowship/ProjectHub',
        tags: ['Python', 'Pod 1.0.1', 'Discord'],
        languages: ['Python', 'Javascript'],
      },
    };
  },
  computed: {},
  mounted() {},
  beforeDestroy() {},
  methods: {},
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

.project-tag {
  color: #fff;
  border: none;
  border-radius: 1rem;
}
</style>
