import Vue from 'vue';

const theamedHexColors = [
  'FDB4C1',
  'FFDEDA',
  'C5C2DF',
  '9B94BE',
  'F9C8A0',
  'F28997',
  'FF9AA2',
  'FFB7B2',
  'FFDAC1',
  'B5EAD7',
  'C7CEEA',
  '77DD77',
  '89CFF0',
  '99C5C4',
  '9ADEDB',
  'AA9499',
  'AAF0D1',
  'B2FBA5',
  'B39EB5',
  'BDB0D0',
  'BEE7A5',
  'BEFD73',
  'C1C6FC',
  'C6A4A4',
  'CB99C9',
  'CEF0CC',
  'CFCFC4',
  'D6FFFE',
  'D8A1C4',
  'DEA5A4',
  'E9D1BF',
  'F49AC2',
  'F4BFFF',
  'FF6961',
  'FF964F',
  'FF9899',
  'FFB7CE',
  'CA9BF7',
];

Vue.filter('hexHash', function (str) {
  const hash = Array.from(str).reduce(
    (hash, char) => hash ^ char.charCodeAt(0),
    0
  );
  return '#' + theamedHexColors[hash % theamedHexColors.length];
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
