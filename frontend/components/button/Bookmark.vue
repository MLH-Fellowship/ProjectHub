<template>
  <iconify-icon v-if="visible" :icon="bookmarkIcon" @click.stop="bookmark" />
</template>

<script>
import IconifyIcon from '@iconify/vue';
import BookmarkOutline from '@iconify/icons-mdi/bookmark-outline';
import Bookmark from '@iconify/icons-mdi/bookmark';

IconifyIcon.addIcon('bookmark-outline', BookmarkOutline);
IconifyIcon.addIcon('bookmark', Bookmark);

// TODO: accept project id and if it's been bookmarked yet

export default {
  name: 'BookmarkButton',
  components: {
    IconifyIcon,
  },
  props: {
    project: {
      required: true,
      type: Object,
    },
  },
  // data() {
  //   return {
  //     bookmarked: false,
  //   };
  // },
  computed: {
    bookmarkIcon() {
      return this.project.bookmarked ? 'bookmark' : 'bookmark-outline';
    },
    visible() {
      return !(
        this.$store.state.user.anonymous ||
        this.$store.state.user.meta.login === this.project.user.login
      );
    },
  },
  methods: {
    async bookmark() {
      await this.$axios.$post(`/api/bookmark/${this.project.id}`);
      this.project.bookmarked = !this.project.bookmarked;
    },
  },
};
</script>
