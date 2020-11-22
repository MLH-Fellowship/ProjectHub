<template>
  <div class="container mw9 overflow-hidden pa3" style="justify-content: none">
    <!-- not sure why the left and right col isn't aligning -->
    <el-row class="items-center w-100 meet-the-team-container">
      <!-- hidden-xs doesn't seem to be working for me? -->
      <el-col :xs="1" :sm="6" :md="8" class="hidden-md-and-down">
        <el-image
          class="relative z-0"
          style="top: 50px; left: 0px; width: 200%"
          :src="require('~/assets/images/team.png')"
        ></el-image>
      </el-col>
      <el-col :offset="1" :xs="22" :sm="18" :md="15">
        <div class="tl relative z-1 w-100">
          <p class="meet-the-team-title b mv3" style="font-size: 4em">
            Meet the Team
          </p>
          <div class="grid tl mt4">
            <div class="pa2 pr3 pb3">
              <el-card class="team-card tl h-100">
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
                      Hi, I'm an open-source maintainer based in San Jose, CA. I
                      love producing reliable code and routinely breaking
                      <el-link
                        type="primary"
                        href="https://github.com/NoahCardoza/CloudProxy"
                        target="_blank"
                      >
                        CloudFlare
                      </el-link>
                      and
                      <el-link
                        type="primary"
                        href="https://github.com/NoahCardoza/CaptchaHarvester"
                        target="_blank"
                      >
                        ReCaptcha </el-link
                      >. I spend most of my time between Python and JavaScript
                      and hope never to touch assembly.
                    </p>
                  </el-col>
                </el-row>
                <el-row class="team-member-link f5 w-100">
                  <el-col class="flex items-center" :offset="8" :span="16">
                    <iconify-icon icon="github" class="mr2 f4" />
                    <span>
                      <el-link
                        type="primary"
                        href="https://github.com/NoahCardoza"
                        target="_blank"
                      >
                        @NoahCardoza
                      </el-link>
                      on Github
                    </span>
                  </el-col>
                </el-row>
              </el-card>
            </div>
            <div class="pa2 pr3 pb3">
              <el-card class="team-card tl h-100">
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
                      Hi, I'm a senior at American University in Washington, DC.
                      I love working with high-performance systems and work
                      primarily in finance. I do most of my work in a language
                      called OCaml, an awesome functional language!
                    </p>
                  </el-col>
                </el-row>
                <el-row class="team-member-link f5 w-100">
                  <el-col class="flex items-center" :offset="8" :span="16">
                    <iconify-icon icon="github" class="mr2 f4" />
                    <span>
                      <el-link
                        type="primary"
                        href="https://github.com/jordanrmerrick"
                        target="_blank"
                      >
                        @jordanrmerrick
                      </el-link>
                      on Github
                    </span>
                  </el-col>
                </el-row>
              </el-card>
            </div>
            <div class="pa2 pr3 pb3">
              <el-card class="team-card tl h-100">
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
                      Jose, CA. I love Cloud, Fintech, Stock, and back-end dev
                      in Javascript.
                    </p>
                  </el-col>
                </el-row>
                <el-row class="team-member-link f5 w-100">
                  <el-col class="flex items-center" :offset="8" :span="16">
                    <iconify-icon icon="github" class="mr2 f4" />
                    <span>
                      <el-link
                        type="primary"
                        href="https://github.com/calvinqc"
                        target="_blank"
                      >
                        @calvinqc
                      </el-link>
                      on Github
                    </span>
                  </el-col>
                </el-row>
              </el-card>
            </div>
            <div class="pa2 pr3 pb3">
              <el-card class="team-card tl h-100">
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
                      Software Engineering student at the University of
                      Waterloo.
                    </p>
                  </el-col>
                </el-row>
                <el-row class="team-member-link f5 w-100">
                  <el-col class="flex items-center" :offset="8" :span="16">
                    <iconify-icon icon="github" class="mr2 f4" />
                    <span>
                      <el-link
                        type="primary"
                        href="https://github.com/gracewgao"
                        target="_blank"
                      >
                        @gracewgao
                      </el-link>
                      on Github
                    </span>
                  </el-col>
                </el-row>
              </el-card>
            </div>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import IconifyIcon from '@iconify/vue';
import Github from '@iconify/icons-mdi/github';
import 'element-ui/lib/theme-chalk/display.css';

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

<style>
@media only screen and (max-width: 1516px) {
  .grid {
    justify-content: center;
  }
  .meet-the-team-title {
    text-align: center;
  }
}

@media only screen and (max-width: 1199px) {
  .meet-the-team-container {
    display: flex;
    justify-content: center;
  }
}

.grid {
  display: flex;
  flex-flow: row wrap;
  justify-content: center;
}
.team-card {
  max-width: 440px;
  min-width: 300px;
  height: 100%;
  position: relative;
}

.team-member-link {
  position: absolute;
  bottom: 0;
  left: 0;
  padding: 20px 20px;
  padding-top: 0;
}

.el-card {
  padding-bottom: 40px;
}
</style>
