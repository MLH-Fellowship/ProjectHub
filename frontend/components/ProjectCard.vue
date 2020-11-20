<template>
  <div class="project-card tl">
    <div class="help-wanted-tag">HELP WANTED</div>
    <el-card :body-style="{ padding: '0px' }" @click.native="openProject">
      <img
        height="250"
        :src="project.source | socialify"
        alt="Project Banner"
      />
      <div class="ph3 pb3">
        <div class="flex flex-row items-center justify-between f3 lh-copy">
          <div>{{ project.name }}</div>
          <BookmarkButton />
        </div>

        <div class="mv3">
          {{ project.description }}
        </div>

        <div class="flex flex-row items-center f4 lh-copy">
          <iconify-icon inline icon="tag-multiple" height="24" class="mr2" />
          Tags
        </div>

        <ProjectTags class="mt3 mb2" :tags="project.tags" />

        <!-- <div class="flex flex-row items-center">
          <el-avatar size="small" :src="ghUser.avatar_url" />
          <div class="ml2">
            Created 5 days ago by
            <el-button type="text" @click="$router.push('/NoahCardoza')">
              @NoahCardoza
            </el-button>
          </div>
        </div> -->

        <div>
          <el-button type="text" @click="learnMore">Learn More</el-button>
        </div>
      </div>
    </el-card>
    <ProjectDetailDialog v-model="detailsVisible" :project="project" />
  </div>
</template>

<script>
import ProjectDetailDialog from '@/components/ProjectDetailDialog';
import ProjectTags from '@/components/ProjectTags';
import BookmarkButton from '@/components/button/Bookmark';
import IconifyIcon from '@iconify/vue';
import TagMultiple from '@iconify/icons-mdi/tag-multiple';

IconifyIcon.addIcon('tag-multiple', TagMultiple);

export default {
  name: 'ProjectCard',
  components: {
    IconifyIcon,
    ProjectDetailDialog,
    ProjectTags,
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
</style>
