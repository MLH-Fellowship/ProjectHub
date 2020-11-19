<template>
  <div class="layout-none">
    <Nuxt />
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.layout-none >>> .container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
