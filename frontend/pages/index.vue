<template>
  <div class="container">
    <el-row class="items-center mw8">
      <el-col :span="16">
        <div>
          <div class="tl">
            <p class="f1">Welcome to</p>
            <p class="b mv3" style="font-size: 5em">Project Hub</p>
            <p class="mt5">
              Introducing a new way to find and share your projects
            </p>
            <el-row class="mt4">
              <el-button round type="primary">Explore Projects</el-button>
              <LoginBox />
            </el-row>
          </div>
        </div>
      </el-col>
      <el-col :span="8">
        <div>
          <el-image
            class="relative"
            style="top: 50px; left: -300px; width: 700px"
            src="/humans1.png"
          ></el-image>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'LandingPage',
  data() {
    return {};
  },
};
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
