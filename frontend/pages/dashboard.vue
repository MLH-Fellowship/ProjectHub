<template>
  <div class="container pt4" style="align-items: none">
    <div>
      <div class="flex flex-row flex-wrap justify-center">
        <div class="f3 lh-copy">Filters:</div>
        <el-select
          v-model="pods"
          multiple
          filterable
          allow-create
          default-first-option
          placeholder="Pods"
          class="mh3"
        >
          <el-option
            v-for="item in options.pods"
            :key="item"
            :label="item"
            :value="item"
          ></el-option>
        </el-select>
        <el-select
          v-model="languages"
          multiple
          filterable
          allow-create
          default-first-option
          placeholder="Lanuages"
        >
          <el-option
            v-for="item in options.languages"
            :key="item"
            :label="item"
            :value="item"
          ></el-option>
        </el-select>
      </div>
      <div class="grid w-100 pa3">
        <Card
          v-for="(something, index) in 6"
          :key="index"
          :index="index"
          class="ma3"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      options: {
        pods: [
          '1.0.0',
          '1.0.1',
          '1.0.2',
          '1.0.3',
          '1.0.5',
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
        ],
        languages: [
          'Javascript',
          'Python',
          'Java',
          'Scala',
          'Golang',
          'Swift',
          'C',
          'C++',
          'C#',
          'OCaml',
          'PHP',
          'Rust',
          'Julia',
          'Cobol',
        ],
      },
      pods: [],
      languages: [],
    };
  },
};
</script>

<style scoped>
.grid {
  display: flex;
  flex-flow: row wrap;
  justify-content: center;
}
</style>
