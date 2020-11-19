const metaFactory = () => ({
  login: '',
  name: '',
  avatar: '',
});

export const state = () => ({
  meta: metaFactory(),
  isLoggedIn: false,
  token: null,
});

export const mutations = {
  SET_TOKEN(state, token) {
    state.token = token;
  },
  SET_IS_LOGGED_IN(state, isLoggedIn) {
    state.isLoggedIn = isLoggedIn;
  },
  SET_META(state, meta) {
    state.meta = meta;
  },
};

export const actions = {
  async login({ commit }, code) {
    // onBoarding
    const { token, meta } = await this.$axios.$get(`/api/auth/${code}`);

    commit('SET_TOKEN', token);
    commit('SET_META', meta);

    return {
      onBoarding: true,
      finish: () => commit('SET_IS_LOGGED_IN', true),
    };
  },
  logout({ commit }) {
    commit('SET_TOKEN', null);
    commit('SET_META', metaFactory());
    commit('SET_IS_LOGGED_IN', false);
  },
};
