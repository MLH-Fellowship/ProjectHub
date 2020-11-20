<template>
  <el-dialog
    v-loading="loading"
    width="80%"
    :visible="value"
    :body-style="{ padding: '0px' }"
    @update:visible="$emit('input', $event)"
  >
    <div>
      <div v-loading="loading" class="pa4 tc">
        <div>
          <el-row type="flex" align="center" class="flex-wrap">
            <el-col :sm="24" :md="9">
              <ProjectOverviewCard />
              <div class="tl mt4">
                <p class="b f4 mb3">Contact the creator</p>
                <div class="flex flex-row items-center tl">
                  <el-avatar
                    size="small"
                    src="https://avatars2.githubusercontent.com/u/38268331?s=460&u=121b7bd7d9dc5697e4728b21c34358cf416edf37&v=4"
                  />
                  <div class="ml3 f4">
                    <el-button
                      type="text"
                      @click="$router.push('/JordanMerrick')"
                    >
                      @JordanMerrick
                    </el-button>
                  </div>
                </div>
              </div>
            </el-col>
            <el-col :sm="24" :md="15" class="pa4 pr0 tl">
              <el-row>
                <div class="flex flex-row f1 items-center b">
                  {{ details.title }}
                  <span class="f2">
                    <BookmarkButton class="ml4" />
                    <iconify-icon
                      v-if="editable"
                      icon="pencil"
                      class="ml2"
                      @click="editProject"
                    />
                  </span>
                </div>
              </el-row>

              <el-row>
                <el-carousel trigger="click" arrow="always">
                  <el-carousel-item
                    v-for="image in details.images"
                    :key="image.url"
                  >
                    <el-image :src="image.url"></el-image>
                    <h3 class="pa3">{{ image.caption }}</h3>
                  </el-carousel-item>
                </el-carousel>
              </el-row>

              <el-row>
                <p class="f3 b mt4">Project Description</p>
                <p class="mt3">{{ details.description }}</p>
                <p class="mt4 flex flex-row items-center">
                  <iconify-icon
                    v-if="editable"
                    icon="clock"
                    class="mr2"
                    @click="editProject"
                  />
                  Last updated {{ details.time }}
                </p>
              </el-row>
            </el-col>
          </el-row>
        </div>
      </div>
    </div>
  </el-dialog>
</template>

<script>
import ProjectOverviewCard from '@/components/ProjectOverview/Card';
import BookmarkButton from '@/components/button/Bookmark';
import IconifyIcon from '@iconify/vue';
import TagMultiple from '@iconify/icons-mdi/tag-multiple';
import Edit from '@iconify/icons-mdi/lead-pencil';
import Clock from '@iconify/icons-mdi/clock-time-four-outline';
import Code from '@iconify/icons-mdi/code-tags';
import Group from '@iconify/icons-mdi/account-group';
import Github from '@iconify/icons-mdi/github';

IconifyIcon.addIcon('tags', TagMultiple);
IconifyIcon.addIcon('pencil', Edit);
IconifyIcon.addIcon('clock', Clock);
IconifyIcon.addIcon('code', Code);
IconifyIcon.addIcon('group', Group);
IconifyIcon.addIcon('github', Github);

const initDetails = () => ({
  title: 'Project Title',
  images: [
    {
      caption: '',
      url:
        'https://github.com/MLH-Fellowship/ProjectHub/raw/main/resources/projecthub.png',
    },
    {
      caption: 'Screenshots etc.',
      url:
        'https://socialify.git.ci/calvinqc/trivin/image?forks=1&issues=1&language=1&owner=1&pulls=1&stargazers=1&theme=Light',
    },
  ],
  description:
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
  source: 'https://github.com/MLH-Fellowship/ProjectHub',
  demo: 'https://github.com/MLH-Fellowship/ProjectHub',
  time: 'November 19, 2020',
  tags: ['Python', 'Pod 1.0.1', 'Discord'],
  languages: ['Python', 'Javascript'],
});

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
  },
  data() {
    return {
      loading: false,
      details: initDetails(),
      bookmarked: false,
      editable: true,
    };
  },
  computed: {},
  mounted() {},
  beforeDestroy() {},
  methods: {
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
