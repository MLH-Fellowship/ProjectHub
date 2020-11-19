<template>
  <div class="project-card tl">
    <div class="help-wanted-tag">HELP WANTED</div>
    <el-card
      v-loading="loading"
      style="max-width: 395px"
      :body-style="{ padding: '0px' }"
    >
      <img
        height="250"
        src="https://socialify.git.ci/calvinqc/trivin/image?forks=1&issues=1&language=1&owner=1&pulls=1&stargazers=1&theme=Light"
        alt="Project Banner"
      />
      <div class="ph3 pb3">
        <div class="flex flex-row items-center justify-between f3 lh-copy">
          <div>Event-bot</div>
          <iconify-icon :icon="bookmarkIcon" @click="bookmark" />
        </div>

        <div class="mv3">
          Discord Bot to make announcements about upcoming sessions for the
          Fellows using Google Calendar.
        </div>

        <div class="flex flex-row items-center f3 lh-copy">
          <iconify-icon inline icon="tag-multiple" height="24" class="mr2" />
          Tags
        </div>

        <div class="mt3 mb2">
          <el-tag color="#8991dc" class="project-tag mb1">Javascript</el-tag>
          <el-tag color="#238aea" class="project-tag mb1">Discord</el-tag>
          <el-tag color="#6fd3de" class="project-tag mb1">Google</el-tag>
          <el-tag color="#238aea" class="project-tag mb1">Python</el-tag>
          <el-tag color="#6fd3de" class="project-tag mb1">Calendly</el-tag>
          <el-tag color="#8991dc" class="project-tag mb1">Pod 1.0.1</el-tag>
        </div>
        <div class="flex flex-row items-center">
          <el-avatar
            size="small"
            src="https://avatars2.githubusercontent.com/u/38268331?s=460&u=121b7bd7d9dc5697e4728b21c34358cf416edf37&v=4"
          />
          <div class="ml2">
            Created 5 days ago by
            <el-button type="text" @click="$router.push('/NoahCardoza')">
              @NoahCardoza
            </el-button>
          </div>
        </div>

        <div>
          <el-button type="text" @click="learn_more">Learn More</el-button>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
import IconifyIcon from '@iconify/vue';
import BookmarkOutline from '@iconify/icons-mdi/bookmark-outline';
import Bookmark from '@iconify/icons-mdi/bookmark';
import TagMultiple from '@iconify/icons-mdi/tag-multiple';

IconifyIcon.addIcon('bookmark-outline', BookmarkOutline);
IconifyIcon.addIcon('bookmark', Bookmark);
IconifyIcon.addIcon('tag-multiple', TagMultiple);

export default {
  components: {
    IconifyIcon,
  },
  props: {
    index: { type: Number, required: true },
  },
  data: () => ({
    loading: false,
    bookmarked: false,
  }),
  computed: {
    bookmarkIcon() {
      return this.bookmarked ? 'bookmark' : 'bookmark-outline';
    },
  },
  methods: {
    learn_more() {},
    bookmark() {
      this.bookmarked = !this.bookmarked;
      // send request to backend
    },
  },
};
</script>

<style>
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
