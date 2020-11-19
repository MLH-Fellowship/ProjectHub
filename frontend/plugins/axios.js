export default ({ $axios, store }) => {
  $axios.setToken(store.state.user.token, 'Bearer');
};
