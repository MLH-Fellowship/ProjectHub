<template>
  <div class="project-card tl">
    <svg
      width="101"
      height="35"
      viewBox="0 0 101 35"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      style="margin-bottom: -5px"
    >
      <path
        d="M0 10C0 4.47715 4.47715 0 10 0H91C96.5229 0 101 4.47715 101 10V35H0V10Z"
        fill="#FFBE55"
        style="margin-left: -100px"
      ></path>
      <path
        d="M19.6355 16H17.9562V12.507H14.6815V16H13.0022V7.84961H14.6815V11.1523H17.9562V7.84961H19.6355V16ZM26.0114 12.4678H22.7871V14.6509H26.5712V16H21.1078V7.84961H26.56V9.20987H22.7871V11.1523H26.0114V12.4678ZM29.2358 14.6509H32.8016V16H27.5564V7.84961H29.2358V14.6509ZM35.4493 13.1283V16H33.77V7.84961H36.9495C37.5616 7.84961 38.0989 7.96157 38.5617 8.18548C39.0282 8.40939 39.3864 8.72846 39.6365 9.1427C39.8865 9.55321 40.0115 10.0216 40.0115 10.5477C40.0115 11.3464 39.7372 11.9771 39.1887 12.4398C38.6438 12.8988 37.8881 13.1283 36.9215 13.1283H35.4493ZM35.4493 11.7681H36.9495C37.3936 11.7681 37.7314 11.6636 37.9627 11.4546C38.1978 11.2456 38.3154 10.9471 38.3154 10.5589C38.3154 10.1596 38.1978 9.83683 37.9627 9.59052C37.7276 9.34422 37.403 9.21734 36.9887 9.20987H35.4493V11.7681ZM50.373 13.6489L51.4702 7.84961H53.144L51.3359 16H49.6453L48.3187 10.5477L46.992 16H45.3014L43.4934 7.84961H45.1671L46.2699 13.6377L47.6133 7.84961H49.0352L50.373 13.6489ZM58.4115 14.3207H55.467L54.9073 16H53.1216L56.1556 7.84961H57.7118L60.7626 16H58.9769L58.4115 14.3207ZM55.9205 12.9604H57.9581L56.9337 9.9096L55.9205 12.9604ZM68.1516 16H66.4723L63.2032 10.6373V16H61.5239V7.84961H63.2032L66.4779 13.2235V7.84961H68.1516V16ZM75.5855 9.20987H73.0889V16H71.4096V9.20987H68.9465V7.84961H75.5855V9.20987ZM81.452 12.4678H78.2277V14.6509H82.0118V16H76.5483V7.84961H82.0006V9.20987H78.2277V11.1523H81.452V12.4678ZM82.997 16V7.84961H85.5048C86.2213 7.84961 86.8613 8.01195 87.4249 8.33662C87.9921 8.65756 88.4343 9.11658 88.7515 9.71368C89.0687 10.307 89.2273 10.9825 89.2273 11.7401V12.1151C89.2273 12.8727 89.0706 13.5463 88.7571 14.1359C88.4474 14.7256 88.0089 15.1827 87.4417 15.5074C86.8744 15.8321 86.2344 15.9963 85.5216 16H82.997ZM84.6763 9.20987V14.6509H85.488C86.1448 14.6509 86.6468 14.4363 86.9938 14.0072C87.3409 13.578 87.5182 12.9641 87.5256 12.1655V11.7345C87.5256 10.906 87.354 10.2791 87.0106 9.85362C86.6673 9.42446 86.1654 9.20987 85.5048 9.20987H84.6763Z"
        fill="white"
      ></path>
    </svg>
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
        <v-chip-group
          v-model="selection"
          active-class="deep-purple accent-4 white--text"
          column
        >
          <v-chip style="background: #8991dc; color: white">Javascript</v-chip>
          <v-chip style="background: #238aea; color: white">Discord</v-chip>
          <v-chip style="background: #6fd3de; color: white">Google</v-chip>
          <v-chip style="background: #238aea; color: white">Python</v-chip>
          <v-chip style="background: #6fd3de; color: white">Calendly</v-chip>
          <v-chip style="background: #8991dc; color: white">Pod 1.0.1</v-chip>
        </v-chip-group>
      </div>
      <div>
        <svg
          width="25"
          height="25"
          viewBox="0 0 25 25"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          xmlns:xlink="http://www.w3.org/1999/xlink"
        >
          <g filter="url(#filter0_d)">
            <ellipse
              cx="12.5"
              cy="8.40767"
              rx="8.5"
              ry="8.27632"
              fill="url(#pattern0)"
            />
          </g>
          <defs>
            <filter
              id="filter0_d"
              x="0.178571"
              y="0.131348"
              width="24.6429"
              height="24.1955"
              filterUnits="userSpaceOnUse"
              color-interpolation-filters="sRGB"
            >
              <feFlood flood-opacity="0" result="BackgroundImageFix" />
              <feColorMatrix
                in="SourceAlpha"
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
              />
              <feOffset dy="3.82143" />
              <feGaussianBlur stdDeviation="1.91071" />
              <feColorMatrix
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"
              />
              <feBlend
                mode="normal"
                in2="BackgroundImageFix"
                result="effect1_dropShadow"
              />
              <feBlend
                mode="normal"
                in="SourceGraphic"
                in2="effect1_dropShadow"
                result="shape"
              />
            </filter>
            <pattern
              id="pattern0"
              patternContentUnits="objectBoundingBox"
              width="1"
              height="1"
            >
              <use
                xlink:href="#image0"
                transform="translate(0 -0.0136844) scale(0.000333444)"
              />
            </pattern>
            <image
              id="image0"
              width="2999"
              height="3000"
              xlink:href="https://media-exp1.licdn.com/dms/image/C4E03AQH69LzLRoU5zw/profile-displayphoto-shrink_800_800/0?e=1611187200&v=beta&t=TOSrV5pgMqHsCS83OlQTEq6UX0-1BqweYZVd6e6WH0E"
            />
          </defs>
        </svg>

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
</style>
