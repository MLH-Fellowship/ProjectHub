<template>
  <el-select
    v-model="value"
    multiple
    filterable
    allow-create
    default-first-option
    :placeholder="name"
  >
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value"
    ></el-option>
  </el-select>
</template>

<script>
export default {
  data() {
    return {
      options: [
        '1.0.0',
        '1.0.1',
        '1.0.2',
        '1.0.3',
        '1.0.5 ',
        '1.0.6',
        '1.1.0',
        '1.1.1',
        '1.1.2',
        '1.1.3',
        '1.1.5',
        '1.1.6',
        '1.2.0',
        '1.2.1',
        '1.2.2',
      ].map((pod) => {
        return { value: pod, label: pod };
      }),
      value: [],
    };
  },
};
</script>
