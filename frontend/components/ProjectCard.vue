<template>
  <div class="project-card tl">
    <div class="help-wanted-tag">HELP WANTED</div>
    <el-card
      :body-style="{ padding: '0px', paddingBottom: '20px' }"
      style="min-height: 500px"
      class="relative"
      @click.native="openProject"
    >
      <img
        height="200"
        :src="project.source | socialify"
        alt="Project Banner"
      />
      <div class="ph3 pb3">
        <div class="flex flex-row items-center justify-between f3 lh-copy">
          <div>{{ project.name }}</div>
          <BookmarkButton />
        </div>

        <ProjectOverview :project="project" :title="false" />
      </div>
      <el-button type="text" class="project-learn-more" @click="learnMore">
        Learn More
      </el-button>
    </el-card>
    <ProjectDetailDialog v-model="detailsVisible" :project="project" />
  </div>
</template>

<script>
import ProjectDetailDialog from '@/components/ProjectDetailDialog';
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
    ProjectDetailDialog,
    ProjectOverview,
    // ProjectTags,
    BookmarkButton,
  },
  props: {
    project: { type: Object, required: true },
  },
  data: () => ({
    detailsVisible: false,
  }),
  computed: {},
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

.help-wanted-tag {
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
