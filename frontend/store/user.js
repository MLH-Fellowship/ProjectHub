const metaFactory = () => ({
  login: '',
  name: '',
  avatar: '',
});

export const state = () => ({
  meta: metaFactory(),
  token: null,
});

export const mutations = {
  SET_TOKEN(state, token) {
    state.token = token;
  },
  SET_META(state, meta) {
    state.meta = meta;
  },
};

export const actions = {
  async login({ commit }, code) {
    const { token, meta } = await this.$axios.$get(`/api/auth/${code}`);

    commit('SET_TOKEN', token);
    commit('SET_META', meta);
  },
  logout({ commit }) {
    commit('SET_TOKEN', null);
    commit('SET_META', metaFactory());
  },
};
