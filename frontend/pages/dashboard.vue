<template>
  <div class="container" style="align-items: none">
    <div>
      <div><h1>Filter By:</h1></div>
      <!-- <DropdownMenu :name="pod" :options="pods" />
    <DropdownMenu :name="language" :options="languages" /> -->
      <el-row class="w-100 pa3">
        <el-col
          v-for="(something, index) in 6"
          :key="index"
          :lg="8"
          :sm="6"
          :md="4"
        >
          <Card :index="index" style="margin-bottom: 3rem" />
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
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
      ].map((pod) => {
        return { value: pod, label: pod };
      }),
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
      ].map((pod) => {
        return { value: pod, label: pod };
      }),
      value: [],
    };
  },
};
</script>
