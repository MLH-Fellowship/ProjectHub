<template>
  <el-dialog
    v-loading="loading"
    width="80%"
    :visible="value"
    :body-style="{ padding: '0px' }"
    @update:visible="$emit('input', $event)"
  >
    <div>
      <!-- idk how to make this go in the background -->
      <!-- <el-image
        class="relative"
        style="height: 300px; top: 0; left: 0; right: 0"
        src="https://socialify.git.ci/calvinqc/trivin/image?forks=1&issues=1&language=1&owner=1&pulls=1&stargazers=1&theme=Light"
        alt="Project Banner"
        :fit="cover"
      ></el-image> -->

      <div v-loading="loading" class="pa4 tc">
        <div>
          <el-row type="flex" align="center">
            <!-- left column -->
            <el-col :span="8">
              <el-card>
                <div class="pa3 tl">
                  <p class="f4 b mb3">Project Overview</p>

                  <div class="flex flex-row f5 mt3">
                    <iconify-icon icon="code" class="mr2" />
                    {{ details.languages.join(', ') }}
                  </div>

                  <div class="flex flex-row f5 mt3">
                    <iconify-icon icon="group" class="mr2" />
                    Jordan, Noah, Calvin
                  </div>

                  <div class="flex flex-row f5 mt3">
                    <iconify-icon icon="github" class="mr2" />
                    <a href="details.source">View Github repo</a>
                  </div>

                  <div class="flex flex-row f5 mt3">
                    <iconify-icon icon="tags" class="mr2" />
                    Tags
                  </div>

                  <!-- this shows up as blocks instead of inline and I'm not sure why  -->
                  <!-- <div v-for="tag in details.tags" :key="tag" class="mt3 mb2">
                    <el-tag color="#8991dc" class="project-tag mb1">
                      {{ tag }}
                    </el-tag>
                  </div> -->

                  <div class="mt3 mb2">
                    <el-tag color="#8991dc" class="project-tag mb1">
                      Javascript
                    </el-tag>
                    <el-tag color="#238aea" class="project-tag mb1">
                      Discord
                    </el-tag>
                    <el-tag color="#6fd3de" class="project-tag mb1">
                      Google
                    </el-tag>
                    <el-tag color="#238aea" class="project-tag mb1">
                      Python
                    </el-tag>
                    <el-tag color="#6fd3de" class="project-tag mb1">
                      Calendly
                    </el-tag>
                    <el-tag color="#8991dc" class="project-tag mb1">
                      Pod 1.0.1
                    </el-tag>
                  </div>
                </div>
              </el-card>
              <div class="tl mt4">
                <p class="b f4 mb3">Contact the creator</p>
                <div class="flex flex-row items-center tl">
                  <el-avatar
                    size="small"
                    src="https://avatars2.githubusercontent.com/u/38268331?s=460&u=121b7bd7d9dc5697e4728b21c34358cf416edf37&v=4"
                  />
                  <div class="ml3 f5">
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

            <!-- right column -->
            <el-col :span="16" class="pa4 pr0 tl">
              <el-row>
                <div class="flex flex-row f1 items-center b">
                  {{ details.title }}
                  <span class="f2">
                    <iconify-icon
                      :icon="bookmarkIcon"
                      class="ml4"
                      @click="bookmark"
                    />
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
                <p class="f3 b">Project Description</p>
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
import IconifyIcon from '@iconify/vue';
import BookmarkOutline from '@iconify/icons-mdi/bookmark-outline';
import Bookmark from '@iconify/icons-mdi/bookmark';
import TagMultiple from '@iconify/icons-mdi/tag-multiple';
import Edit from '@iconify/icons-mdi/lead-pencil';
import Clock from '@iconify/icons-mdi/clock-time-four-outline';
import Code from '@iconify/icons-mdi/code-tags';
import Group from '@iconify/icons-mdi/account-group';
import Github from '@iconify/icons-mdi/github';

IconifyIcon.addIcon('bookmark-outline', BookmarkOutline);
IconifyIcon.addIcon('bookmark', Bookmark);
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
  computed: {
    title() {
      return 'Project Title';
    },
    bookmarkIcon() {
      return this.bookmarked ? 'bookmark' : 'bookmark-outline';
    },
  },
  mounted() {},
  beforeDestroy() {},
  methods: {
    bookmark() {
      this.bookmarked = !this.bookmarked;
      // send request to backend
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
