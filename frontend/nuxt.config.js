export default {
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'Project Hub',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'stylesheet',
        href: 'https://unpkg.com/tachyons@4/css/tachyons.min.css',
      },
    ],
  },

  env: {
    GITHUB_CLIENT_ID: process.env.GITHUB_CLIENT_ID,
    APP_HOSTNAME: process.env.APP_HOSTNAME,
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: ['element-ui/lib/theme-chalk/index.css', '@/style/main.css'],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
    '@/plugins/element-ui',
    '@/plugins/persiste-state',
    '@/plugins/github',
    '@/plugins/axios',
    {
      src: '@/plugins/vue-social-auth',
      mode: 'client',
    },
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
  ],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    'cookie-universal-nuxt',
    // https://github.com/nuxt-community/proxy-module
    '@nuxtjs/proxy',
  ],

  proxy: {
    '/api': {
      target: `http://${process.env.BACKEND_HOST || 'localhost'}:8000`,
      pathRewrite: {
        '^/api': '',
      },
    },
  },

  // Axios module configuration (https://go.nuxtjs.dev/config-axios)
  axios: {},

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
    analyze: process.env.NUXT_ANALYZE === '1',
    transpile: [/^element-ui/],
  },
};
