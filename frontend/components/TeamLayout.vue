<template>
  <div class="container mw9 overflow-hidden pa3" style="justify-content: none">
    <!-- not sure why the left and right col isn't aligning -->
    <el-row class="items-center w-100">
      <!-- hidden-xs doesn't seem to be working for me? -->
      <el-col :xs="1" :sm="6" :md="8" class="hidden-xs-only">
        <el-image
          class="relative z-0"
          style="top: 50px; left: 0px; width: 200%"
          :src="require('~/assets/images/team.png')"
        ></el-image>
      </el-col>
      <el-col :offset="2" :xs="22" :sm="18" :md="14">
        <div class="tl relative z-1">
          <p class="b mv3" style="font-size: 4em">Meet the Team</p>
          <el-row class="w-100 tl mt4 flex flex-wrap">
            <el-card class="team-card tl pa2 mr3 mb3 h-100">
              <el-row class="flex flex-box items-center">
                <el-col :span="8" class="tc">
                  <el-avatar
                    class="mr4"
                    icon="el-icon-user-solid"
                    :src="require('~/assets/images/noah.png')"
                    :size="90"
                  ></el-avatar>
                </el-col>
                <el-col :span="16">
                  <p class="f4 b">Noah Cardoza</p>
                  <p class="f5 mt3">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua.
                  </p>
                  <div class="flex flex-row items-center mt3 f5">
                    <iconify-icon icon="github" class="mr2 f4" />
                    <span>
                      <el-link
                        type="primary"
                        href="https://github.com/NoahCardoza/"
                      >
                        @NoahCardoza
                      </el-link>
                      on Github
                    </span>
                  </div>
                </el-col>
              </el-row>
            </el-card>
            <el-card class="team-card tl pa2 mr3 mb3 h-100">
              <el-row class="flex flex-box items-center">
                <el-col :span="8" class="tc">
                  <el-avatar
                    class="mr4"
                    icon="el-icon-user-solid"
                    :src="require('~/assets/images/jordan.jpg')"
                    :size="90"
                  ></el-avatar>
                </el-col>
                <el-col :span="16">
                  <p class="f4 b">Jordan Merrick</p>
                  <p class="f5 mt3">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua.
                  </p>
                  <div class="flex flex-row items-center mt3 f5">
                    <iconify-icon icon="github" class="mr2 f4" />
                    <span>
                      <el-link
                        type="primary"
                        href="https://github.com/jordanrmerrick"
                      >
                        @jordanrmerrick
                      </el-link>
                      on Github
                    </span>
                  </div>
                </el-col>
              </el-row>
            </el-card>
            <el-card class="team-card tl pa2 mr3 mb3 h-100">
              <el-row class="flex flex-box items-center">
                <el-col :span="8" class="tc">
                  <el-avatar
                    class="mr4"
                    icon="el-icon-user-solid"
                    :src="require('~/assets/images/calvin.jpg')"
                    :size="90"
                  ></el-avatar>
                </el-col>
                <el-col :span="16">
                  <p class="f4 b">Calvin Nguyen</p>
                  <p class="f5 mt3">
                    Hi, I'm a senior Software Engineering student based in San
                    Jose, CA. I love Cloud, Fintech, Stock, and back-end dev in
                    Javascript.
                  </p>
                  <div class="flex flex-row items-center mt3 f5">
                    <iconify-icon icon="github" class="mr2 f4" />
                    <span>
                      <el-link
                        type="primary"
                        href="https://github.com/calvinqc"
                      >
                        @calvinqc
                      </el-link>
                      on Github
                    </span>
                  </div>
                </el-col>
              </el-row>
            </el-card>
            <el-card class="team-card tl pa2 mr3 mb3 h-100">
              <el-row class="flex flex-box items-center">
                <el-col :span="8" class="tc">
                  <el-avatar
                    class="mr4"
                    icon="el-icon-user-solid"
                    :src="require('~/assets/images/grace.jpg')"
                    :size="90"
                  ></el-avatar>
                </el-col>
                <el-col :span="16">
                  <p class="f4 b">Grace Gao</p>
                  <p class="f5 mt3">
                    Hi! I'm from Ottawa, Canada and I'm currently a first-year
                    Software Engineering student at the University of Waterloo.
                  </p>
                  <div class="flex flex-row items-center mt3 f5">
                    <iconify-icon icon="github" class="mr2 f4" />
                    <span>
                      <el-link
                        type="primary"
                        href="https://github.com/gracewgao"
                      >
                        @gracewgao
                      </el-link>
                      on Github
                    </span>
                  </div>
                </el-col>
              </el-row>
            </el-card>
          </el-row>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import IconifyIcon from '@iconify/vue';
import Github from '@iconify/icons-mdi/github';

IconifyIcon.addIcon('github', Github);

export default {
  name: 'TeamLayout',
  components: {
    IconifyIcon,
  },
  data() {
    return {};
  },
};
</script>

<style scoped>
.grid {
  display: flex;
  flex-flow: row wrap;
  justify-content: center;
}
.team-card {
  max-width: 400px;
  min-width: 300px;
  height: 100%;
}
</style>
