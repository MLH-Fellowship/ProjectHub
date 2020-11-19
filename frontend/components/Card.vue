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
      <div class="row mx-0 align-center" style="margin-left: 0" @click="save">
        <div>Event-bot</div>
        <span style="padding-top: 22px">
          <iconify-icon icon="bookmark-outline" height="24" />
        </span>
      </div>

      <div>
        Discord Bot to make announcements about upcoming sessions for the
        Fellows using Google Calendar.
      </div>

      <div>
        <span style="padding-top: 5px; margin-right: 10px">
          <iconify-icon icon="tag-multiple" height="24" />
        </span>
        Tags
      </div>

      <div>
        <el-tag color="#8991dc" style="color: #fff">Javascript</el-tag>
        <el-tag color="#238aea" style="color: #fff">Discord</el-tag>
        <el-tag color="#6fd3de" style="color: #fff">Google</el-tag>
        <el-tag color="#238aea" style="color: #fff">Python</el-tag>
        <el-tag color="#6fd3de" style="color: #fff">Calendly</el-tag>
        <el-tag color="#8991dc" style="color: #fff">Pod 1.0.1</el-tag>
      </div>
      <div>
        <el-avatar
          src="https://media-exp1.licdn.com/dms/image/C4E03AQH69LzLRoU5zw/profile-displayphoto-shrink_800_800/0?e=1611187200&v=beta&t=TOSrV5pgMqHsCS83OlQTEq6UX0-1BqweYZVd6e6WH0E"
        />

        Created 5 days ago by&nbsp;
        <b><a href="">@noahcardoza</a></b>
      </div>

      <div>
        <v-btn text color="teal accent-4" @click="learn_more">Learn More</v-btn>
      </div>
    </el-card>
  </div>
</template>

<script>
// npm install --save-dev @iconify/react @iconify-icons/mdi
import IconifyIcon from '@iconify/vue';
import BookmarkOutline from '@iconify/icons-mdi/bookmark-outline';
import TagMultiple from '@iconify/icons-mdi/tag-multiple';

IconifyIcon.addIcon('bookmark-outline', BookmarkOutline);
IconifyIcon.addIcon('tag-multiple', TagMultiple);

export default {
  components: {
    IconifyIcon,
  },
  props: {
    index: { type: Number, required: true },
  },
  data: () => ({
    selection: 1,
    selected: false,
  }),
  methods: {
    learn_more() {},
    save() {
      const saveButton = this.$refs.savePath;
      if (this.selected) {
        saveButton.setAttribute(
          'd',
          'M0 3.01443C0 2.36154 0.239476 1.7354 0.665747 1.27375C1.09202 0.81209 1.67017 0.552734 2.273 0.552734H9.09202C9.69485 0.552734 10.273 0.81209 10.6993 1.27375C11.1255 1.7354 11.365 2.36154 11.365 3.01443V17.7846L5.68251 14.092L0 17.7846V3.01443Z'
        );
        saveButton.setAttribute('fill', '#238AEA');
      } else {
        saveButton.setAttribute(
          'd',
          'M5.41007 13.6728L0.5 16.8634V3.01443C0.5 2.48186 0.695715 1.97833 1.0331 1.61294C1.36924 1.24889 1.81622 1.05273 2.273 1.05273H9.09202C9.5488 1.05273 9.99578 1.24889 10.3319 1.61294C10.6693 1.97833 10.865 2.48186 10.865 3.01443V16.8634L5.95495 13.6728L5.68251 13.4957L5.41007 13.6728Z'
        );
        saveButton.setAttribute('fill', 'white');
        saveButton.setAttribute('stroke', 'black');
      }
      this.selected = !this.selected;
    },
  },
};
</script>

<style>
.v-card--reveal {
  bottom: 0;
  opacity: 1 !important;
  position: absolute;
  width: 100%;
}

.help-wanted-tag {
  padding: 0.5rem;
  border-radius: 10px 10px 0 0;
  background: #ffbe55;
  width: max-content;
  color: #fff;
}
</style>
