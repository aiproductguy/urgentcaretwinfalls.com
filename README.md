# 🏗️ Website [JamStack](https://jamstack.org/)
Domain Registrar: Owner's choice
DNS: [CloudFlare.com](https://CloudFlare.com) (Free)
Hosting: [Github.com](https://www.github.com/) (Free)
Deployment: [Netlify.com](https://www.netlify.com/) (Free)
Site Builder: [Astro.build](https://astro.build/) (Free, MIT)
Base Theme: [Assessible Astro](https://accessible-astro.netlify.app/) (Free, MIT)

## 🎨 Theme Features & Accessibility
This accessible theme is a ready to use, SEO and a11y friendly blogging theme. It contains plenty of accessible components to build several page types, Tailwind CSS to help you build faster and example pages such as a dynamic Blog, 404, Markdown and MDX. This theme is designed to build faster and provide a solid base for accessibility!
- Astro 4.0
- Tailwind CSS support
- Prettier integration with `prettier-plugin-astro` and `prettier-plugin-tailwind`
- ESLint integration with strict accessibility settings for `eslint-plugin-jsx-a11y`
- Markdown and MDX support with examples included in the theme
- Uses the awesome `astro-icon` package for the icons
- Excellent Lighthouse/PageSpeed scores
- Accessible landmarks such as `header`, `main`, `footer`, `section` and `nav`
- Outline focus indicator which works on dark and light backgrounds
- Several `aria` attributes which provide a better experience for screen reader users
- `[...page].astro` and `[post].astro` demonstrate the use of dynamic routes and provide a basic blog with breadcrumbs and pagination
- `404.astro` provides a custom 404 error page which you can adjust to your needs
- `Header.astro` component included in the `DefaultLayout.astro` layout
- `Footer.astro` component included in the `DefaultLayout.astro` layout
- `SkipLinks.astro` component to skip to either the main menu or the main content
- `Navigation.astro` component with keyboard accessible (dropdown) navigation (arrow keys, escape key)
- `ResponsiveToggle.astro` component with an accessible responsive toggle button for the mobile navigation
- `DarkMode.astro` component toggle with accessible button and a user system preferred color scheme setting
- `SiteMeta.astro` SEO component for setting custom meta data on different pages
- `.sr-only` utility class for screen reader only text content (hides text visually)
- `prefers-reduced-motion` disables animations for users that have this preference turned on
- Ships with many components such as Accordions, Breadcrumbs, Modals, Pagination [and many more](https://accessible-astro.dev/accessible-components)
- A collection of utility classes such as breakpoints, button classes, font settings, resets and outlines in `src/assets/scss/base`
- View Transitions (⚠️ see [astro-docs](https://docs.astro.build/en/guides/view-transitions/#accessibility) for accessibility considerations)

## Development
Git clone this repo locally and run any of the following commands in your terminal:
- *Use `pnpm` (rather than `npm`) for more efficient content-addressed package management*

| Command            | Action                                       |
| :----------------- | :------------------------------------------- |
| `pnpm install`     | Installs dependencies                        |
| `pnpm run dev`     | Starts local dev server at `localhost:4321`  |
| `pnpm run build`   | Build your production site to `./dist/`      |
| `pnpm run preview` | Preview your build locally, before deploying |

## Helping out
If you find that something isn't working right then I'm always happy to hear it to improve this starter! You can contribute in many ways and forms. Let me know by either:

1. [Filing an issue](https://github.com/markteekman/accessible-astro-starter/issues)
2. [Submitting a pull request](https://github.com/markteekman/accessible-astro-starter/pulls)
3. [Starting a discussion](https://github.com/markteekman/accessible-astro-starter/discussions)
4. [Buying me a coffee!](https://www.buymeacoffee.com/markteekman)
