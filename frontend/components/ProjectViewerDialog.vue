<template>
  <el-dialog
    width="80%"
    custom-class="project-diolog"
    :visible="value"
    @update:visible="$emit('input', $event)"
  >
    <div>
      <div class="tc">
        <el-row type="flex" align="center" class="flex-wrap">
          <el-col :sm="24" :md="9">
            <ProjectOverviewCard :project="project" />
            <div class="tl mv4">
              <p class="b f4 mb3">Creator</p>
              <div class="flex flex-col items-center tl">
                <div class="flex flex-row flex-wrap items-center">
                  <el-avatar size="small" :src="project.user.avatar" />
                  <div class="ml3 f5">
                    <el-button type="text" @click="viewUserProfile">
                      @{{ project.user.login }}
                    </el-button>
                  </div>
                  <div
                    class="mt2 ph2 word-break pre-wrap"
                    v-text="project.user.bio"
                  />
                  <!-- <p class="mt4 b ph2 flex flex-row items-center">
                    Last updated {{ project.updated }}
                  </p> -->
                </div>
              </div>
            </div>
          </el-col>
          <el-col :sm="24" :md="15" class="ph4 tl">
            <div class="flex justify-between items-center f2 mb2">
              <div class="flex flex-row items-center b black">
                {{ project.name }}
              </div>
              <div class="tr f4">
                <iconify-icon
                  v-if="isUsersProject"
                  icon="lead-pencil"
                  class="ml2"
                  @click="editingProject = true"
                />
                <BookmarkButton :project="project" />
              </div>
            </div>
            <el-row>
              <el-carousel trigger="click" arrow="always">
                <el-carousel-item>
                  <el-image :src="project.source | socialify"></el-image>
                  <!-- <h3 class="pa3">{{ image.caption }}</h3> -->
                </el-carousel-item>
              </el-carousel>
            </el-row>

            <el-row>
              <p class="f3 b">Project Description</p>
              <p class="mt3 pre-wrap" v-text="project.description" />
            </el-row>
          </el-col>
        </el-row>
      </div>
    </div>
    <ProjectDetailsDialog
      v-model="editingProject"
      :project="project"
      nested-dialog
    />
  </el-dialog>
</template>

<script>
import ProjectOverviewCard from '@/components/ProjectOverview/Card';
import BookmarkButton from '@/components/button/Bookmark';
import IconifyIcon from '@iconify/vue';
import TagMultiple from '@iconify/icons-mdi/tag-multiple';
import LeadPencil from '@iconify/icons-mdi/lead-pencil';
import Clock from '@iconify/icons-mdi/clock-time-four-outline';
import Code from '@iconify/icons-mdi/code-tags';
import Group from '@iconify/icons-mdi/account-group';
import Github from '@iconify/icons-mdi/github';

IconifyIcon.addIcon('tags', TagMultiple);
IconifyIcon.addIcon('lead-pencil', LeadPencil);
IconifyIcon.addIcon('clock', Clock);
IconifyIcon.addIcon('code', Code);
IconifyIcon.addIcon('group', Group);
IconifyIcon.addIcon('github', Github);

export default {
  name: 'ProjectViewerDialog',
  components: {
    IconifyIcon,
    ProjectOverviewCard,
    BookmarkButton,
  },
  props: {
    value: {
      required: true,
      type: Boolean,
    },
    project: { type: Object, required: true },
  },
  data() {
    return {
      editingProject: false,
    };
  },
  computed: {
    isUsersProject() {
      return this.$store.state.user.meta.login === this.project.user.login;
    },
  },
  methods: {
    viewUserProfile() {
      this.$emit('input', false);
      this.$router.push(`/${this.project.user.login}`);
    },
  },
};
</script>

<style lang="css">
.pre-wrap {
  word-break: break-word;
  white-space: pre-line;
}

.project-diolog {
  padding: 0px;
  max-width: 1200px;
}
</style>
