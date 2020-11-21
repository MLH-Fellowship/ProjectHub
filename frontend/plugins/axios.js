export default function ({ $axios, redirect, store, route }) {
  $axios.onRequest((config) => {
    const { token } = store.state.user;
    if (!token) {
      return;
    }

    if (
      config.url.startsWith('/') ||
      config.url.startsWith(process.env.FRONTEND_BASE_URL)
    ) {
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
