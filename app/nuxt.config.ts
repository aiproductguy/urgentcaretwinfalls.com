// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    '@nuxtjs/tailwindcss',
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
    buildAssetsDir: 'assets',
    head: {
      title: 'Urgent Care Twin Falls',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { 
          name: 'description', 
          content: 'Urgent Care Twin Falls offers prompt, compassionate medical care for non-life-threatening illnesses and injuries in Twin Falls, Idaho.'
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
    base: process.env.GITHUB_ACTIONS ? '/urgentcaretwinfalls.com/' : '/',
    build: {
      assetsDir: 'assets',
      rollupOptions: {
        output: {
          assetFileNames: 'assets/[name].[hash][extname]',
          chunkFileNames: 'assets/[name].[hash].js',
          entryFileNames: 'assets/[name].[hash].js'
        }
      }
    },
    server: {
      hmr: {
        protocol: 'ws',
        host: 'localhost'
      }
    }
  },

  nitro: {
    preset: process.env.GITHUB_ACTIONS ? 'github-pages' : 'node-server',
    static: true
  },

  routeRules: {
    '/**': {
      headers: {
        'Cross-Origin-Embedder-Policy': 'unsafe-none',
        'Cross-Origin-Opener-Policy': 'unsafe-none',
        'Cross-Origin-Resource-Policy': 'cross-origin'
      }
    }
  },

  runtimeConfig: {
    public: {
      baseURL: process.env.GITHUB_ACTIONS ? '/urgentcaretwinfalls.com/' : '/',
      contact: {
        address: {
          street: '260 Falls Avenue, Suite D',
          city: 'Twin Falls',
          state: 'ID',
          zip: '83301'
        },
        phone: '(208) 555-5555',
        email: 'info@urgentcaretwinfalls.com',
        googleMapsUrl: 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2937.9623927753546!2d-114.47637859999999!3d42.5773207!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x54aca2457605db65%3A0x24920c41025270b7!2s260%20Falls%20Ave%2C%20Twin%20Falls%2C%20ID%2083301!5e0!3m2!1sen!2sus!4v1726347046896!5m2!1sen!2sus'
      },
      hours: {
        weekdays: {
          open: '8:00 AM',
          close: '5:00 PM'
        },
        weekend: 'Closed',
        holidays: 'Closed on major holidays',
        shortSchedule: '8:00 AM - 5:00 PM M-F',
        longSchedule: [
          'Monday - Friday: 8:00 AM - 5:00 PM',
          'Saturday - Sunday: Closed'
        ]
      }
    }
  },

  ssr: false,

  experimental: {
    payloadExtraction: false
  },

  compatibilityDate: '2025-01-14'
})