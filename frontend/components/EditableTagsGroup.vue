<template>
  <div>
    <el-tag
      v-for="tag in tags"
      :key="tag"
      closable
      :disable-transitions="false"
      @close="removeTag(tag)"
    >
      {{ tag }}
    </el-tag>
    <el-input
      v-if="input.visible && !disabled"
      ref="tags"
      v-model="input.value"
      class="input-new-tag"
      size="mini"
      :placeholder="placeholder"
      @keyup.enter.native="handleInputConfirm"
      @blur="handleInputConfirm"
    ></el-input>
  </div>
</template>

<script>
import toSlug from '@/utils/toSlug';

export default {
  name: 'EditableTagsGroup',
  components: {},
  props: {
    tags: {
      required: true,
      type: Array,
    },
    limit: {
      default: -1,
      type: Number,
    },
    placeholder: {
      default: 'Tag',
      type: String,
    },
    disabled: {
      default: false,
      type: Boolean,
    },
  },
  data() {
    return {
      input: {
        value: '',
        visible: true,
      },
    };
  },
  methods: {
    removeTag(tag) {
      this.tags.splice(this.tags.indexOf(tag), 1);
    },
    // showInput() {
    //   this.input.visible = true;
    //   this.$nextTick((_) => {
    //     this.$refs.tags.$refs.input.focus();
    //   });
    // },
    handleInputConfirm() {
      const value = toSlug(this.input.value);
      if (value && !this.tags.includes(value)) {
        this.tags.push(value);
      }
      this.input.value = '';
      if (this.limit !== -1 && this.tags.length >= this.limit) {
        this.input.visible = false;
      }
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
</style>
