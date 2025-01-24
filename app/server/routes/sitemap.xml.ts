import { SitemapStream, streamToPromise } from 'sitemap'
import { defineEventHandler } from 'h3'
import { promises as fs } from 'fs'
import { join } from 'path'
import { useRuntimeConfig } from '#imports'

async function getPages(dir: string): Promise<string[]> {
  const pages = new Set<string>()
  const items = await fs.readdir(dir, { withFileTypes: true })
  
  for (const item of items) {
    const path = join(dir, item.name)
    
    if (item.isDirectory()) {
      const subPages = await getPages(path)
      subPages.forEach(page => pages.add(page))
    } else if (item.name.endsWith('.vue')) {
      let urlPath = path
        .split('pages')[1] // Get everything after 'pages'
        .replace(/\.vue$/, '') // Remove .vue extension
        .replace(/\/index$/, '') // Remove trailing /index
        || '/' // Use / for empty path
      
      pages.add(urlPath)
    }
  }
  
  return Array.from(pages).sort()
}

export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig()
  const baseURL = process.env.GITHUB_ACTIONS 
    ? 'https://aiproductguy.github.io/urgentcaretwinfalls.com'
    : 'http://localhost:3000'

  // Create a new sitemap stream with proper XML formatting
  const sitemap = new SitemapStream({
    hostname: baseURL
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

    // Set response headers for XML
    event.node.res.setHeader('Content-Type', 'application/xml; charset=UTF-8')
    event.node.res.setHeader('Cache-Control', 'public, max-age=3600')

    // Convert stream to string and return
    const sitemapContent = await streamToPromise(sitemap)
    return sitemapContent.toString()
  } catch (error) {
    console.error('Error generating sitemap:', error)
    throw error
  }
}) 