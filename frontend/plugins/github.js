import Vue from 'vue';

export default ({ $axios }) => {
  Vue.use({
    install(Vue) {
      Vue.prototype.$github = {
        get(...params) {
          return $axios.$get(`https://api.github.com/${params.join('/')}`);
        },
      };
    },
  });
};
