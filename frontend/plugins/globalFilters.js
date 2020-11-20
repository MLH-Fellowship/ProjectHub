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
