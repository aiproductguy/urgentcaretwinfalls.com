import { SitemapStream, streamToPromise } from 'sitemap'
import { defineEventHandler } from 'h3'
import { promises as fs } from 'fs'
import { join } from 'path'

async function getPages(dir: string): Promise<string[]> {
  const pages: string[] = []
  const items = await fs.readdir(dir, { withFileTypes: true })
  
  for (const item of items) {
    const path = join(dir, item.name)
    if (item.isDirectory()) {
      // Add the directory index route
      pages.push(path.replace(/^.*?pages/, '').replace(/\/index$/, '') || '/')
      // Get all sub-pages
      const subPages = await getPages(path)
      pages.push(...subPages)
    } else if (item.name.endsWith('.vue')) {
      // Convert file path to URL path
      let urlPath = path
        .replace(/^.*?pages/, '') // Remove everything before 'pages'
        .replace(/\.vue$/, '') // Remove .vue extension
      
      // Handle index files
      if (item.name === 'index.vue') {
        urlPath = urlPath.replace(/\/index$/, '') // Remove /index from the end
      }
      
      pages.push(urlPath || '/') // Use / for home page
    }
  }
  
  return [...new Set(pages)] // Remove duplicates
}

export default defineEventHandler(async (event) => {
  // Create a new sitemap stream
  const sitemap = new SitemapStream({
    hostname: 'https://aiproductguy.github.io/urgentcaretwinfalls.com'
  })

  try {
    // Get all pages from the pages directory
    const pagesDir = join(process.cwd(), 'pages')
    const pages = await getPages(pagesDir)

    // Define priority and changefreq based on URL patterns
    for (const page of pages) {
      let priority = 0.7
      let changefreq = 'monthly'

      // Adjust priority and changefreq based on URL patterns
      if (page === '/') {
        priority = 1.0
        changefreq = 'daily'
      } else if (page === '/location') {
        priority = 0.8
        changefreq = 'monthly'
      } else if (page === '/services') {
        priority = 0.9
        changefreq = 'weekly'
      } else if (page === '/articles') {
        priority = 0.9
        changefreq = 'weekly'
      } else if (page.startsWith('/services/')) {
        priority = 0.8
      } else if (page.startsWith('/articles/')) {
        priority = 0.7
      }

      sitemap.write({
        url: page,
        changefreq,
        priority,
        lastmod: new Date().toISOString()
      })
    }

    sitemap.end()

    // Set response headers
    event.node.res.setHeader('Content-Type', 'application/xml')
    event.node.res.setHeader('Cache-Control', 'public, max-age=3600')

    // Convert stream to string and return
    const sitemapContent = await streamToPromise(sitemap)
    return sitemapContent.toString()
  } catch (error) {
    console.error('Error generating sitemap:', error)
    throw error
  }
}) 