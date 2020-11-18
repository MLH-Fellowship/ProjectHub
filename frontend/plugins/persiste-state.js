import createPersistedState from 'vuex-persistedstate';

if (process.server) {
  global.atob = (s) => Buffer.from(s, 'base64').toString();
  global.btoa = (s) => Buffer.from(s).toString('base64');
}

export default ({ app: { $cookies }, store }) => {
  console.log($cookies.getAll());
  createPersistedState({
    key: 'state',
    paths: ['user'],
    storage: {
      getItem: (key) => {
        const item = $cookies.get(key);
        if (item === undefined) {
          return undefined;
        }
        const { value } = JSON.parse(atob(item));
        return value;
      },
      setItem: (key, value) => {
        $cookies.set(key, btoa(JSON.stringify({ value })), {
          maxAge: 24 * 60 * 60,
          secure: false,
        });
      },
      removeItem: (key) => {
        $cookies.remove(key);
      },
    },
  })(store);
};
