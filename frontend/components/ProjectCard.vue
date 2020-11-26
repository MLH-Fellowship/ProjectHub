<template>
  <div class="project-card tl">
    <div
      class="project-state-tag"
      :style="{
        opacity: Number(Boolean(project.state)),
      }"
    >
      {{ project.state | state }}
    </div>
    <el-card
      body-style="padding: 0px; padding-bottom: 14px"
      style="padding-bottom: 0"
      class="relative h-100"
      @click.native="openProject"
    >
      <img
        height="200"
        :src="project.source | socialify"
        alt="Project Banner"
      />
      <div class="ph3">
        <div class="flex flex-row items-center justify-between f3 lh-copy">
          <div>{{ project.name }}</div>
          <BookmarkButton :project="project" />
        </div>

        <ProjectOverview class="mt2" :project="project" :title="false" />
      </div>
      <el-button type="text" class="project-learn-more" @click="learnMore">
        Learn More
      </el-button>
    </el-card>
    <ProjectViewerDialog v-model="detailsVisible" :project="project" />
  </div>
</template>

<script>
import ProjectOverview from '@/components/ProjectOverview';
// import ProjectTags from '@/components/ProjectTags';
import BookmarkButton from '@/components/button/Bookmark';
import IconifyIcon from '@iconify/vue';
import TagMultiple from '@iconify/icons-mdi/tag-multiple';

IconifyIcon.addIcon('tag-multiple', TagMultiple);

export default {
  name: 'Project',
  components: {
    // IconifyIcon,
    ProjectOverview,
    // ProjectTags,
    BookmarkButton,
  },
  filters: {
    state(str) {
      return (str && str.toUpperCase()) || 'PLACEHOLDER';
    },
  },
  props: {
    project: { type: Object, required: true },
  },
  data: () => ({
    detailsVisible: false,
  }),

  methods: {
    learnMore() {},
    openProject() {
      this.detailsVisible = true;
    },
  },
};
</script>

<style>
.project-card {
  max-width: 400px;
  min-width: 300px;
}

.project-state-tag {
  padding: 0.5rem;
  border-radius: 10px 10px 0 0;
  background: #ffbe55;
  width: max-content;
  color: #fff;
}

.project-tag {
  color: #fff;
  border: none;
  border-radius: 1rem;
}

.project-learn-more {
  bottom: 5px;
  position: absolute;
  left: 15px;
}
</style>
