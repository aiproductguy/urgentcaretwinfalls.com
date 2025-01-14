import { defineConfig } from 'astro/config'
import mdx from '@astrojs/mdx'
import tailwind from '@astrojs/tailwind'
import compress from 'astro-compress'
import icon from "astro-icon"

// https://astro.build/config
export default defineConfig({
  compressHTML: true,
  integrations: [mdx(), icon(), tailwind({
    applyBaseStyles: false,
  }), compress()],
  output: 'static',
  build: {
    assets: 'assets/astro_old',
    inlineStylesheets: 'auto'
  },
  vite: {
    build: {
      cssCodeSplit: true,
      rollupOptions: {
        output: {
          manualChunks: {
            'vendor': ['./src/scripts/vendor.js']
          }
        }
      }
    }
  }
})
