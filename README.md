# Urgent Care Twin Falls Website

A modern, accessible website for Urgent Care Twin Falls built with Astro.

## Recent Changes

Based on the website feedback report from December 16, 2024:

### 🎯 Improvements Made

1. **Site Structure**
   - Implemented consistent header and footer components
   - Organized URL hierarchy into 6 main sections
   - Added proper structural consistency across pages

2. **Content Coverage**
   - Added missing service pages:
     - X-Rays & Imaging
     - Treating Illnesses
     - Minor Injuries
   - Improved content coverage from 62.5% to 100%

3. **Navigation**
   - Implemented mobile-friendly navigation
   - Added consistent menu structure
   - Enhanced keyboard navigation accessibility

4. **Design & Accessibility**
   - Added proper alt text to all images (85.7% → 100%)
   - Implemented ARIA labels throughout
   - Enhanced responsive design

5. **Performance**
   - Optimized page load times
   - Implemented asset optimization
   - Added proper caching strategies

## 🚀 Development

### Prerequisites
- Node.js 20.x or later
- pnpm 8.x or later

### Setup
```bash
# Install pnpm if you haven't already
npm install -g pnpm

# Clone the repository
git clone https://github.com/yourusername/urgentcaretwinfalls.com.git
cd urgentcaretwinfalls.com

# Install dependencies
cd app
pnpm install
```

### Development Server
```bash
# Start the development server
pnpm run dev

# Open http://localhost:3000 in your browser
```

### Build
```bash
# Generate static files
pnpm run generate
```

## 📦 Deployment

### GitHub Pages

The site automatically deploys to GitHub Pages when changes are pushed to the `main` branch.

#### Manual Setup (if needed)
1. In your repository settings, go to Pages
2. Set the source to "GitHub Actions"
3. Ensure the following repository secrets are set:
   - `GITHUB_TOKEN` (automatically provided)

#### Deployment Process
1. Push your changes to the main branch:
   ```bash
   git add .
   git commit -m "Your update message"
   git push origin main
   ```
2. The GitHub Action will automatically:
   - Build the site
   - Deploy to GitHub Pages
   - Create a new release
3. Check the deployment status in the Actions tab
4. Once complete, your site will be live at:
   `https://{username}.github.io/urgentcaretwinfalls.com/`

Each successful deployment also creates a new release tagged as "latest" with deployment artifacts.
