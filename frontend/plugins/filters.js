import Vue from 'vue';

Vue.filter('hexHash', function (str) {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = str.charCodeAt(i) + ((hash << 5) - hash);
  }
  // eslint-disable-next-line prettier/prettier
  const code = (hash & 0x00FFFFFF).toString(16);
  return '#' + '00000'.substring(0, 6 - code.length) + code;
});

Vue.filter('joinWithComma', function (list) {
  return list.join(', ');
});

Vue.filter('socialify', function (url) {
  const namespace = url.split('/').slice(-2).join('/');
  return `https://socialify.git.ci/${namespace}/image?forks=1&issues=1&language=1&owner=1&pulls=1&stargazers=1&theme=Light`;
});

Vue.filter('trim', function (str) {
  return str.trim();
});
