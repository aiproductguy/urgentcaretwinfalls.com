// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/content',
    '@vueuse/nuxt',
    '@nuxt/image',
    '@nuxtjs/color-mode'
  ],

  postcss: {
    plugins: {
      'postcss-import': {},
      'tailwindcss/nesting': 'postcss-nesting',
      tailwindcss: {},
      autoprefixer: {
        grid: true
      }
    }
  },

  colorMode: {
    classSuffix: '',
    preference: 'light',
    fallback: 'light'
  },

  app: {
    baseURL: process.env.GITHUB_ACTIONS ? '/urgentcaretwinfalls.com/' : '/',
    buildAssetsDir: '_nuxt',
    cdnURL: process.env.GITHUB_ACTIONS ? 'https://aiproductguy.github.io/urgentcaretwinfalls.com' : '',
    head: {
      title: 'Urgent Care of Twin Falls',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { 
          name: 'description', 
          content: 'Urgent Care of Twin Falls offers prompt, compassionate medical care for non-life-threatening illnesses and injuries in Twin Falls, Idaho.'
        }
      ],
      link: [
        { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' },
        {
          rel: 'canonical',
          href: 'https://urgentcaretwinfallscom.netlify.app'
        }
      ]
    }
  },

  css: [
    '@/assets/css/globals.css'
  ],

  vite: {
    css: {
      modules: {
        localsConvention: 'camelCase'
      }
    },
    esbuild: {
      supported: {
        'top-level-await': true
      }
    },
    optimizeDeps: {
      include: [
        '@vueuse/core',
        '@vueuse/shared'
      ]
    },
    base: process.env.GITHUB_ACTIONS ? '/urgentcaretwinfalls.com/' : '/'
  },

  content: {
    highlight: {
      theme: 'github-dark'
    },
    documentDriven: true,
    markdown: {
      remarkPlugins: ['remark-gfm'],
      rehypePlugins: ['rehype-external-links']
    }
  },

  nitro: {
    preset: 'github-pages',
    static: true,
    prerender: {
      crawlLinks: true,
      routes: [
        '/services/minor-injuries',
        '/services/illness-treatment',
        '/services/work-medical',
        '/services/diagnostic',
        '/services/xray',
        '/services/physicals',
        '/services/illnesses'
      ]
    },
    routeRules: {
      '/**': {
        headers: {
          'Cross-Origin-Embedder-Policy': 'unsafe-none',
          'Cross-Origin-Opener-Policy': 'unsafe-none',
          'Cross-Origin-Resource-Policy': 'cross-origin'
        }
      }
    }
  },

  compatibilityDate: '2024-12-18',
  ssr: false,
  experimental: {
    payloadExtraction: false
  }
})