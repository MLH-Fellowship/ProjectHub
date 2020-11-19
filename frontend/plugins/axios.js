export default function ({ $axios, redirect, store }) {
  $axios.onRequest((config) => {
    if (new URL(config.url).hostname === process.env.APP_HOSTNAME) {
      const { token } = store.state.user;
      if (token) {
        config.headers.common.Authorization = `Bearer ${token}`;
      }
    }
  });

  $axios.onError((error) => {
    const code = parseInt(error.response && error.response.status);
    if (code === 403) {
      // TODO: redirect & show message
      redirect('/login');
    }
  });
}
