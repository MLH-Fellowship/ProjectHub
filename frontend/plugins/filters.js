import Vue from 'vue';

const theamedHexColors = [
  '#238AEA',
  '#6FD3DE',
  '#8991DC',
  '#E87613',
  '#81F7E5',
  '#CE563B',
  '#0A8754',
  '#4B3F72',
  '#A23B72',
  '#001F54',
  '#048A81',
  '#EF709D',
  '#439A86',
  '#FF8533',
  '#EF709D',
  '#70C1B3',
];

Vue.filter('hexHash', function (str) {
  const hash = Array.from(str).reduce(
    (hash, char) => hash + char.charCodeAt(0),
    0
  );

  return theamedHexColors[hash % theamedHexColors.length];
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
