export const state = () => ({
  login: 'NoahCardoza',
  name: 'Noah Cardoza',
  avatar: 'https://avatars0.githubusercontent.com/u/10343470?v=4',
});

export const mutations = {
  SET_NAME(state, name) {
    state.name = name;
  },
};
