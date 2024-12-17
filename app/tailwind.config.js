/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {
          100: '#e6f7ff',
          300: '#40a9ff',
          500: '#1890ff',
          700: '#096dd9',
        },
        secondary: {
          100: '#f6ffed',
          300: '#73d13d',
          500: '#52c41a',
          700: '#389e0d',
        },
        dark: {
          100: '#141414',
          200: '#1f1f1f',
          300: '#262626',
          400: '#434343',
        },
      },
      container: {
        center: true,
        padding: '1rem',
      },
      typography: {
        DEFAULT: {
          css: {
            maxWidth: 'none',
            color: 'inherit',
            a: {
              color: 'var(--primary-500)',
              '&:hover': {
                color: 'var(--primary-700)',
              },
            },
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
} 