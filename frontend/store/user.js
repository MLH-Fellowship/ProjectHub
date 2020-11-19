const metaFactory = () => ({
  login: '',
  name: '',
  avatar: '',
});

export const state = () => ({
  meta: metaFactory(),
  anonymous: true,
  token: null,
});

export const mutations = {
  SET_TOKEN(state, token) {
    state.token = token;
  },
  SET_ANONYMOUS(state, anonymous) {
    state.anonymous = anonymous;
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
      finish: () => commit('SET_ANONYMOUS', false),
    };
  },
  logout({ commit }) {
    commit('SET_TOKEN', null);
    commit('SET_META', metaFactory());
    commit('SET_ANONYMOUS', true);
  },
};
