const DOCKER_BACKEND_HOST = process.env.DOCKER_BACKEND_HOST || 'localhost';
const FRONTEND_BASE_URL =
  process.env.FRONTEND_BASE_URL || 'http://localhost:3000';

const theme = '#FBC6FD';

export default {
  loading: {
    color: theme,
  },
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'Project Hub',
    link: [
      {
        rel: 'stylesheet',
        href: 'https://unpkg.com/tachyons@4/css/tachyons.min.css',
      },
    ],
  },

  env: {
    GITHUB_CLIENT_ID: process.env.GITHUB_CLIENT_ID,
    FRONTEND_BASE_URL: process.env.FRONTEND_BASE_URL,
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: ['@/style/index.css', '@/style/main.css'],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
    '@/plugins/element-ui',
    '@/plugins/persiste-state',
    '@/plugins/github',
    '@/plugins/axios',
    '@/plugins/filters',
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

  pwa: {
    meta: {
      name: 'Project Hub',
      theme_color: theme,
      description:
        'Introducing a new way for MLH students to find and share the projects they love!',
      ogHost: FRONTEND_BASE_URL,
    },
    manifest: {
      name: 'Project Hub',
      short_name: 'PH',
      description:
        'Introducing a new way for MLH students to find and share the projects they love!',
    },
  },

  proxy: {
    '/api': {
      target: `http://${DOCKER_BACKEND_HOST}:8000`,
      pathRewrite: {
        '^/api': '',
      },
    },
  },

  // Axios module configuration (https://go.nuxtjs.dev/config-axios)
  axios: {
    baseURL: FRONTEND_BASE_URL,
  },

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
    analyze: process.env.NUXT_ANALYZE === '1',
    transpile: [/^element-ui/],
  },
};
