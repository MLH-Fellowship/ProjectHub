<template>
  <el-dialog
    width="80%"
    :visible="value"
    :body-style="{ padding: '0px' }"
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
                  <el-avatar size="small" :src="project.user.avatar_url" />
                  <div class="ml3 f5">
                    <el-button type="text" @click="viewUserProfile">
                      @{{ project.user.login }}
                    </el-button>
                  </div>
                  <div
                    style="white-space: pre"
                    class="mt2"
                    v-text="project.user.bio"
                  />
                </div>
              </div>
            </div>
          </el-col>
          <el-col :sm="24" :md="15" class="ph4 tl">
            <div class="flex justify-between f2">
              <div class="flex flex-row items-center b black">
                {{ project.name }}
              </div>
              <div class="tr">
                <BookmarkButton />
                <iconify-icon
                  v-if="editable"
                  icon="lead-pencil"
                  class="ml2"
                  @click="editProject"
                />
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
              <p class="mt3">{{ project.description }}</p>
              <!-- <p class="mt4 flex flex-row items-center">
                <iconify-icon
                  v-if="editable"
                  icon="clock"
                  class="mr2"
                  @click="editProject"
                />
                Last updated {{ details.time }}
              </p> -->
            </el-row>
          </el-col>
        </el-row>
      </div>
    </div>
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
  name: 'ProjectDetailDialog',
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
      bookmarked: false,
      editable: true,
    };
  },
  computed: {},
  mounted() {
    console.log(this.project.user);
  },
  beforeDestroy() {},
  methods: {
    viewUserProfile() {
      this.$emit('input', false);
      this.$router.push(`/${this.project.user.login}`);
    },
    editProject() {
      // send request to backend
    },
  },
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
