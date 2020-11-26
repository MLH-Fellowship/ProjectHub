<template>
  <div>
    <el-tag
      v-for="tag in tags"
      :key="tag"
      :color="tag | hexHash"
      class="project-tag mb1"
    >
      {{ tag }}
    </el-tag>
  </div>
</template>

<script>
export default {
  name: 'ProjectTags',
  props: {
    tags: { type: Array, required: true },
  },
};
</script>

<style lang="css" scoped>
.el-tag {
  margin-right: 10px;
  margin-bottom: 10px;
}

.project-tag {
  color: #fff;
  text-shadow: black 0px 0px 50px;
  overflow: hidden;
  font-weight: 900;
  font-size: 11px;
  border: none;
  border-radius: 1rem;
}
</style>
