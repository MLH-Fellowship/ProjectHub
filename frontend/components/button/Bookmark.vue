<template>
  <iconify-icon :icon="bookmarkIcon" @click.stop="bookmark" />
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
    // projectId: {
    //   required: true,
    //   type: Number,
    // },
    // value: {
    //   required: true,
    //   type: Boolean,
    // },
  },
  data() {
    return {
      bookmarked: false,
    };
  },
  computed: {
    bookmarkIcon() {
      return this.bookmarked ? 'bookmark' : 'bookmark-outline';
    },
  },
  methods: {
    bookmark() {
      this.bookmarked = !this.bookmarked;
      // send request to backend
    },
  },
};
</script>
