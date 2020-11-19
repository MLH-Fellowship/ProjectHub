<template>
  <v-container class="grey lighten-5">
    <h1>Filter By:</h1>
    <!-- <DropdownMenu :name="pod" :options="pods" />
    <DropdownMenu :name="language" :options="languages" /> -->
    <br />
    <br />
    <hr />
    <br />
    <v-row no-gutters>
      <v-col
        v-for="(something, index) in 6"
        :key="index"
        cols="8"
        sm="6"
        md="4"
      >
        <Card :index="index" style="margin-bottom: 75px; padding-right: 25px" />
      </v-col>
    </v-row>
  </v-container>
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
