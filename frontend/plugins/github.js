export default ({ $axios }, inject) => {
  inject('github', {
    get(...params) {
      return $axios.$get(`https://api.github.com/${params.join('/')}`, {
        headers: {
          Accept: 'application/vnd.github.mercy-preview+json',
        },
      });
    },
  });
};
