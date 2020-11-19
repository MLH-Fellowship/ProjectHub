export const state = () => ({
  meta: {
    login: '',
    name: '',
    avatar: '',
  },
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

    commit('user/SET_TOKEN', token);
    commit('user/SET_META', meta);
  },
};
