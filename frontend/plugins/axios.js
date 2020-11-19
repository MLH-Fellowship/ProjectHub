export default function ({ $axios, redirect, store, route }) {
  $axios.onRequest((config) => {
    const { token } = store.state.user;
    if (!token) {
      return;
    }

    // If you are good at binary math plz halp!
    if (!/^https?:\/\//.test(config.url)) {
      config.headers.common.Authorization = `Bearer ${token}`;
    } else if (new URL(config.url).hostname === process.env.APP_HOSTNAME) {
      config.headers.common.Authorization = `Bearer ${token}`;
    }
  });

  $axios.onError((error) => {
    const code = parseInt(error.response && error.response.status);
    if (code === 403) {
      // TODO: show message when auth=expired on login page
      redirect(`/?login=1&auth=expired&redirect=${route.path}`);
    }
  });
}
