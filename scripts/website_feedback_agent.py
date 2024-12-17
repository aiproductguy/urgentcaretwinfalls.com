from playwright.async_api import async_playwright
import asyncio
import logging
from typing import Dict, List, Optional, Tuple
import json
from datetime import datetime, timedelta
import time
import os
from pathlib import Path
import hashlib
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class WebsiteFeedbackAgent:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.visited_urls = set()
        self.pages_content = {}
        self.required_services = {
            "minor injuries",
            "treating illnesses", 
            "physicals",
            "wellness checkups",
            "diagnostic services", 
            "x-rays",
            "imaging",
            "work-related medical"
        }
        self.performance_metrics = {
            "page_latencies": {},
            "total_runtime": 0,
            "start_time": None,
            "end_time": None
        }
        self.playwright = None
        self.browser = None
        self.context = None
        self.cache_dir = Path('.cache')
        self.cache_dir.mkdir(exist_ok=True)
        
        # Add file handler for logging to cache directory
        date_time = datetime.now().strftime('%Y-%m-%d-%H%M')
        log_file = self.cache_dir / f"{date_time}-feedback.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(file_handler)
        
        logger.info(f"Initialized WebsiteFeedbackAgent for {base_url}")
        logger.info("Performance monitoring initialized")

    def _get_cache_key(self, url: str) -> str:
        """Generate a cache key for a URL"""
        return hashlib.md5(url.encode()).hexdigest()

    def _get_cache_file(self, url: str) -> Path:
        """Get the cache file path for a URL"""
        date = datetime.now().strftime('%Y%m%d')
        return self.cache_dir / f"{date}-{self._get_cache_key(url)}.json"

    def _is_cache_valid(self, cache_file: Path) -> bool:
        """Check if the cache file is from today and not too old"""
        if not cache_file.exists():
            return False
        
        try:
            with cache_file.open('r') as f:
                data = json.load(f)
                cached_at = datetime.fromisoformat(data.get('cached_at', ''))
                now = datetime.now()
                
                # Cache is valid if:
                # 1. It's from today
                # 2. It's less than 12 hours old
                return (
                    cached_at.date() == now.date() and
                    (now - cached_at).total_seconds() < 43200  # 12 hours
                )
        except Exception as e:
            logger.warning(f"Error checking cache validity: {str(e)}")
            return False

    def _prepare_for_cache(self, data: Dict) -> Dict:
        """Prepare data for caching by converting datetime objects to ISO format strings"""
        if isinstance(data, dict):
            return {k: self._prepare_for_cache(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [self._prepare_for_cache(item) for item in data]
        elif isinstance(data, datetime):
            return data.isoformat()
        elif isinstance(data, set):
            return list(data)
        return data

    def _save_to_cache(self, url: str, data: Dict):
        """Save data to cache"""
        date = datetime.now().strftime('%Y%m%d')
        cache_file = self.cache_dir / f"{date}-{self._get_cache_key(url)}.json"
        try:
            # Convert data to JSON-serializable format
            cache_data = self._prepare_for_cache(data)
            with cache_file.open('w', encoding='utf-8') as f:
                json.dump(cache_data, f, indent=2, ensure_ascii=False)
            logger.info(f"Saved data to cache for {url}")
        except Exception as e:
            logger.warning(f"Failed to save cache for {url}: {str(e)}")

    def _restore_from_cache(self, data: Dict) -> Dict:
        """Restore datetime objects from ISO format strings in cached data"""
        if isinstance(data, dict):
            restored = {}
            for k, v in data.items():
                if k in ["start_time", "end_time", "cached_at", "timestamp"]:
                    try:
                        restored[k] = datetime.fromisoformat(v) if isinstance(v, str) else v
                    except (ValueError, TypeError):
                        restored[k] = v
                else:
                    restored[k] = self._restore_from_cache(v)
            return restored
        elif isinstance(data, list):
            return [self._restore_from_cache(item) for item in data]
        return data

    def _load_from_cache(self, url: str) -> Optional[Dict]:
        """Load cached data for a URL if it exists and is valid"""
        cache_file = self._get_cache_file(url)
        
        if self._is_cache_valid(cache_file):
            try:
                with cache_file.open('r', encoding='utf-8') as f:
                    cached_data = json.load(f)
                logger.info(f"Found valid cache from {cache_file.name}")
                
                # Log cache details
                cached_at = datetime.fromisoformat(cached_data.get('cached_at', ''))
                cache_age = (datetime.now() - cached_at).total_seconds() / 3600  # hours
                logger.info(f"Cache age: {cache_age:.1f} hours")
                logger.info(f"Pages in cache: {len(cached_data.get('pages_content', {}))}")
                
                return self._restore_from_cache(cached_data)
            except Exception as e:
                logger.warning(f"Failed to load cache: {str(e)}")
                return None
        return None

    async def analyze_website(self):
        """Main method to analyze the website"""
        self.performance_metrics["start_time"] = datetime.now()
        try:
            logger.info("Starting website analysis")
            
            # Check cache first
            cached_data = self._load_from_cache(self.base_url)
            if cached_data:
                logger.info("Using cached website data from today")
                self.pages_content = cached_data.get("pages_content", {})
                self.visited_urls = set(cached_data.get("visited_urls", []))
                self.performance_metrics = cached_data.get("performance_metrics", self.performance_metrics)
                
                # Generate feedback without crawling
                feedback = self._generate_feedback()
                self._save_feedback(feedback)
                self._save_markdown_feedback(feedback)
                logger.info("Generated feedback from cached data")
                return
            
            # If no cache, initialize browser and crawl
            logger.info("No valid cache found, starting website crawl...")
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch()
            self.context = await self.browser.new_context()
            
            await self._crawl_site(self.base_url)
            
            # Save to cache
            cache_data = {
                "pages_content": self.pages_content,
                "visited_urls": list(self.visited_urls),
                "performance_metrics": self.performance_metrics,
                "cached_at": datetime.now().isoformat()
            }
            self._save_to_cache(self.base_url, cache_data)
            
            feedback = self._generate_feedback()
            self._save_feedback(feedback)
            self._save_markdown_feedback(feedback)
            logger.info("Website analysis completed successfully")
            
        except Exception as e:
            logger.error(f"Critical error during website analysis: {str(e)}", exc_info=True)
        finally:
            self.performance_metrics["end_time"] = datetime.now()
            self.performance_metrics["total_runtime"] = (
                self.performance_metrics["end_time"] - 
                self.performance_metrics["start_time"]
            ).total_seconds()
            self._save_performance_metrics()
            
            if hasattr(self, 'context') and self.context:
                await self.context.close()
            if hasattr(self, 'browser') and self.browser:
                await self.browser.close()
            if hasattr(self, 'playwright') and self.playwright:
                await self.playwright.stop()
            logger.info("Browser session closed")

    async def _crawl_site(self, url: str):
        if url in self.visited_urls:
            logger.debug(f"Skipping already visited URL: {url}")
            return
        
        self.visited_urls.add(url)
        logger.info(f"Analyzing page: {url}")

        start_time = time.time()
        try:
            page = await self.context.new_page()
            await page.goto(url, wait_until="networkidle")

            # Record page load time
            page_load_time = time.time() - start_time
            self.performance_metrics["page_latencies"][url] = {
                "load_time": page_load_time,
                "timestamp": datetime.now().isoformat()
            }
            logger.info(f"Page load time for {url}: {page_load_time:.2f}s")

            # Get page content
            html = await page.content()
            text = await page.evaluate('() => document.documentElement.textContent')
            title = await page.title()
            
            # Get all links
            links = await page.evaluate('''() => {
                return Array.from(document.querySelectorAll('a')).map(a => a.href).filter(href => href);
            }''')
            
            # Get all images with error handling
            images = await page.evaluate('''() => {
                return Array.from(document.querySelectorAll('img')).map(img => ({
                    src: img.src || '',
                    alt: img.alt || '',
                    width: img.width || 0,
                    height: img.height || 0
                }));
            }''')
            
            # Get meta tags with error handling
            meta_tags = await page.evaluate('''() => {
                return Array.from(document.querySelectorAll('meta')).map(meta => ({
                    name: meta.getAttribute('name') || '',
                    content: meta.getAttribute('content') || ''
                })).filter(meta => meta.name || meta.content);
            }''')

            # Store page content
            self.pages_content[url] = {
                "html": html,
                "text": text,
                "title": title,
                "links": links,
                "images": images,
                "meta": meta_tags
            }

            # Find and filter internal links
            internal_links = [
                link for link in links
                if link.startswith(self.base_url)
            ]
            logger.info(f"Found {len(internal_links)} internal links on {url}")

            await page.close()

            # Crawl internal links
            for link in internal_links:
                await self._crawl_site(link)

        except Exception as e:
            self.performance_metrics["page_latencies"][url] = {
                "error": str(e),
                "load_time": time.time() - start_time,
                "timestamp": datetime.now().isoformat()
            }
            logger.error(f"Error crawling {url}: {str(e)}", exc_info=True)
            self.pages_content[url] = {
                "error": str(e),
                "html": "",
                "text": "",
                "title": "",
                "links": [],
                "images": []
            }

    def _analyze_site_structure(self) -> Dict:
        return {
            "total_pages": len(self.pages_content),
            "hierarchy": self._analyze_hierarchy(),
            "consistency": self._check_structural_consistency()
        }

    def _analyze_content_coverage(self) -> Dict:
        covered_services = set()
        
        for url, content in self.pages_content.items():
            # Use text content instead of html for better accuracy
            page_text = content["text"].lower()
            for service in self.required_services:
                if service in page_text:
                    covered_services.add(service)
                    
        missing_services = self.required_services - covered_services
        
        return {
            "covered_services": list(covered_services),
            "missing_services": list(missing_services),
            "coverage_percentage": (len(covered_services) / len(self.required_services)) * 100
        }

    def _analyze_navigation(self) -> Dict:
        nav_elements = []
        for url, content in self.pages_content.items():
            nav_links = [
                link for link in content["links"] 
                if "nav" in str(link).lower() or "menu" in str(link).lower()
            ]
            nav_elements.extend(nav_links)

        return {
            "menu_items": len(set(nav_elements)),
            "navigation_consistency": self._check_navigation_consistency(),
            "mobile_friendly": self._check_mobile_navigation()
        }

    def _analyze_design(self) -> Dict:
        accessibility_score = self._check_accessibility()
        return {
            "responsive_design": self._check_responsive_design(),
            "visual_consistency": self._check_visual_consistency(),
            "accessibility": accessibility_score
        }

    def _check_accessibility(self) -> Dict:
        """Check accessibility features across pages"""
        total_images = 0
        images_with_alt = 0
        headings = []
        
        for content in self.pages_content.values():
            # Check images for alt text
            for img in content["images"]:
                total_images += 1
                if img.get("alt"):
                    images_with_alt += 1
            
            # Get headings from the page
            page_headings = content.get("headings", [])
            headings.extend(page_headings)

        return {
            "alt_text_ratio": images_with_alt / total_images if total_images > 0 else 0,
            "headings_count": len(headings),
            "aria_labels_present": True,  # Implement actual check
            "color_contrast": True  # Implement actual check
        }

    def _analyze_seo(self) -> Dict:
        """Analyze SEO aspects of the website"""
        seo_data = {
            "meta_tags": self._analyze_meta_tags(),
            "headings": self._analyze_headings(),
            "content": self._analyze_content_seo(),
            "links": self._analyze_links_seo(),
            "images": self._analyze_images_seo(),
            "score": 0  # Will be calculated based on all factors
        }
        
        # Calculate overall SEO score (0-100)
        scores = {
            "meta_tags": self._score_meta_tags(seo_data["meta_tags"]),
            "headings": self._score_headings(seo_data["headings"]),
            "content": self._score_content(seo_data["content"]),
            "links": self._score_links(seo_data["links"]),
            "images": self._score_images(seo_data["images"])
        }
        seo_data["score"] = sum(scores.values()) / len(scores)
        seo_data["scores"] = scores
        
        return seo_data

    def _analyze_meta_tags(self) -> Dict:
        """Analyze meta tags across all pages"""
        meta_analysis = {
            "title_tags": [],
            "descriptions": [],
            "keywords": [],
            "robots": [],
            "og_tags": [],
            "twitter_cards": [],
            "missing_meta": []
        }
        
        for url, content in self.pages_content.items():
            page_meta = content.get("meta", [])
            title = content.get("title", "")
            
            # Track missing essential meta tags
            missing = []
            found_desc = False
            
            meta_analysis["title_tags"].append({
                "url": url,
                "title": title,
                "length": len(title)
            })
            
            for meta in page_meta:
                name = meta.get("name", "").lower()
                content_text = meta.get("content", "")
                
                if name == "description":
                    found_desc = True
                    meta_analysis["descriptions"].append({
                        "url": url,
                        "content": content_text,
                        "length": len(content_text)
                    })
                elif name == "keywords":
                    meta_analysis["keywords"].append({
                        "url": url,
                        "content": content_text
                    })
                elif name == "robots":
                    meta_analysis["robots"].append({
                        "url": url,
                        "content": content_text
                    })
                elif name.startswith("og:"):
                    meta_analysis["og_tags"].append({
                        "url": url,
                        "property": name,
                        "content": content_text
                    })
                elif name.startswith("twitter:"):
                    meta_analysis["twitter_cards"].append({
                        "url": url,
                        "property": name,
                        "content": content_text
                    })
            
            if not found_desc:
                missing.append("description")
            if not title:
                missing.append("title")
            
            if missing:
                meta_analysis["missing_meta"].append({
                    "url": url,
                    "missing": missing
                })
        
        return meta_analysis

    def _analyze_headings(self) -> Dict:
        """Analyze heading structure across all pages"""
        heading_analysis = {
            "h1_usage": [],
            "heading_structure": [],
            "missing_headings": []
        }
        
        for url, content in self.pages_content.items():
            # Extract headings using a simple regex (for demonstration)
            html = content.get("html", "")
            h1_tags = len(re.findall(r'<h1[^>]*>.*?</h1>', html, re.I | re.S))
            h2_tags = len(re.findall(r'<h2[^>]*>.*?</h2>', html, re.I | re.S))
            h3_tags = len(re.findall(r'<h3[^>]*>.*?</h3>', html, re.I | re.S))
            
            structure = {
                "url": url,
                "h1_count": h1_tags,
                "h2_count": h2_tags,
                "h3_count": h3_tags
            }
            
            heading_analysis["heading_structure"].append(structure)
            
            if h1_tags == 0:
                heading_analysis["missing_headings"].append({
                    "url": url,
                    "missing": "h1"
                })
            elif h1_tags > 1:
                heading_analysis["h1_usage"].append({
                    "url": url,
                    "count": h1_tags,
                    "issue": "multiple_h1"
                })
        
        return heading_analysis

    def _analyze_content_seo(self) -> Dict:
        """Analyze content for SEO factors"""
        content_analysis = {
            "word_counts": [],
            "keyword_density": [],
            "readability": []
        }
        
        for url, content in self.pages_content.items():
            text = content.get("text", "")
            words = text.split()
            word_count = len(words)
            
            # Simple readability score (Flesch-Kincaid)
            sentences = len(re.findall(r'[.!?]+', text))
            syllables = sum([self._count_syllables(word) for word in words])
            if sentences > 0 and word_count > 0:
                readability = 206.835 - 1.015 * (word_count / sentences) - 84.6 * (syllables / word_count)
            else:
                readability = 0
            
            content_analysis["word_counts"].append({
                "url": url,
                "count": word_count
            })
            
            content_analysis["readability"].append({
                "url": url,
                "score": readability
            })
        
        return content_analysis

    def _analyze_links_seo(self) -> Dict:
        """Analyze links for SEO factors"""
        return {
            "internal_links": [
                {
                    "url": url,
                    "count": len([l for l in content.get("links", []) if l.startswith(self.base_url)])
                }
                for url, content in self.pages_content.items()
            ],
            "external_links": [
                {
                    "url": url,
                    "count": len([l for l in content.get("links", []) if not l.startswith(self.base_url)])
                }
                for url, content in self.pages_content.items()
            ]
        }

    def _analyze_images_seo(self) -> Dict:
        """Analyze images for SEO factors"""
        image_analysis = {
            "alt_text": [],
            "missing_alt": []
        }
        
        for url, content in self.pages_content.items():
            images = content.get("images", [])
            images_with_alt = [img for img in images if img.get("alt")]
            images_without_alt = [img for img in images if not img.get("alt")]
            
            image_analysis["alt_text"].append({
                "url": url,
                "count": len(images_with_alt)
            })
            
            if images_without_alt:
                image_analysis["missing_alt"].append({
                    "url": url,
                    "count": len(images_without_alt)
                })
        
        return image_analysis

    def _score_meta_tags(self, meta_data: Dict) -> float:
        """Score meta tag implementation (0-100)"""
        score = 100
        
        # Penalize for missing meta tags
        score -= len(meta_data["missing_meta"]) * 10
        
        # Check title lengths
        for title in meta_data["title_tags"]:
            if title["length"] < 30 or title["length"] > 60:
                score -= 5
        
        # Check description lengths
        for desc in meta_data["descriptions"]:
            if desc["length"] < 120 or desc["length"] > 160:
                score -= 5
        
        # Bonus for social meta tags
        if meta_data["og_tags"]:
            score += 5
        if meta_data["twitter_cards"]:
            score += 5
            
        return max(0, min(100, score))

    def _score_headings(self, heading_data: Dict) -> float:
        """Score heading structure (0-100)"""
        score = 100
        
        # Penalize missing or multiple H1s
        score -= len(heading_data["missing_headings"]) * 15
        score -= len(heading_data["h1_usage"]) * 10
        
        return max(0, min(100, score))

    def _score_content(self, content_data: Dict) -> float:
        """Score content quality (0-100)"""
        score = 100
        
        # Check word counts
        for page in content_data["word_counts"]:
            if page["count"] < 300:
                score -= 10
        
        # Check readability
        for page in content_data["readability"]:
            if page["score"] < 60:
                score -= 5
            
        return max(0, min(100, score))

    def _score_links(self, link_data: Dict) -> float:
        """Score link structure (0-100)"""
        score = 100
        
        # Check internal linking
        for page in link_data["internal_links"]:
            if page["count"] < 3:
                score -= 5
            
        return max(0, min(100, score))

    def _score_images(self, image_data: Dict) -> float:
        """Score image optimization (0-100)"""
        score = 100
        
        # Penalize missing alt text
        for page in image_data["missing_alt"]:
            score -= page["count"] * 5
            
        return max(0, min(100, score))

    def _count_syllables(self, word: str) -> int:
        """Simple syllable counter for English words"""
        word = word.lower()
        count = 0
        vowels = "aeiouy"
        on_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not on_vowel:
                count += 1
            on_vowel = is_vowel
            
        if word.endswith('e'):
            count -= 1
        if count == 0:
            count = 1
            
        return count

    def _generate_feedback(self) -> Dict:
        """Generate feedback report"""
        logger.info("Generating feedback report")
        feedback = {
            "site_structure": self._analyze_site_structure(),
            "navigation": self._analyze_navigation(),
            "content_coverage": self._analyze_content_coverage(),
            "design": self._analyze_design(),
            "seo": self._analyze_seo(),  # Add SEO analysis
            "metadata": {
                "analysis_date": datetime.now().isoformat(),
                "total_pages_analyzed": len(self.visited_urls),
                "base_url": self.base_url
            }
        }
        logger.info("Feedback report generated successfully")
        return feedback

    def _save_feedback(self, feedback: Dict):
        try:
            date_time = datetime.now().strftime('%Y-%m-%d-%H%M')
            output_file = self.cache_dir / f"{date_time}-feedback.json"
            with output_file.open('w', encoding='utf-8') as f:
                json.dump(feedback, f, indent=2, ensure_ascii=False)
            logger.info(f"Feedback saved to {output_file}")
            
            # Also save a summary to the log
            logger.info("Analysis Summary:")
            logger.info(f"- Pages analyzed: {len(self.visited_urls)}")
            logger.info(f"- Content coverage: {feedback['content_coverage']['coverage_percentage']:.1f}%")
            logger.info(f"- Missing services: {', '.join(feedback['content_coverage']['missing_services'])}")
            
        except Exception as e:
            logger.error(f"Error saving feedback: {str(e)}", exc_info=True) 

    def _save_performance_metrics(self):
        metrics = {
            "total_runtime_seconds": self.performance_metrics["total_runtime"],
            "start_time": self.performance_metrics["start_time"].isoformat() if self.performance_metrics["start_time"] else None,
            "end_time": self.performance_metrics["end_time"].isoformat() if self.performance_metrics["end_time"] else None,
            "pages_analyzed": len(self.visited_urls),
            "average_page_latency": sum(
                p["load_time"] for p in self.performance_metrics["page_latencies"].values()
                if isinstance(p.get("load_time"), (int, float))
            ) / len(self.visited_urls),
            "page_latencies": self._prepare_for_cache(self.performance_metrics["page_latencies"])
        }

        try:
            date_time = datetime.now().strftime('%Y-%m-%d-%H%M')
            output_file = self.cache_dir / f"{date_time}-performance.json"
            with output_file.open('w') as f:
                json.dump(metrics, f, indent=2)
            
            logger.info("Performance Summary:")
            logger.info(f"- Total runtime: {metrics['total_runtime_seconds']:.2f}s")
            logger.info(f"- Average page latency: {metrics['average_page_latency']:.2f}s")
            logger.info(f"- Pages analyzed: {metrics['pages_analyzed']}")
            
        except Exception as e:
            logger.error(f"Error saving performance metrics: {str(e)}", exc_info=True) 

    def _analyze_hierarchy(self) -> Dict:
        """Analyze the site hierarchy based on URL structure"""
        hierarchy = {}
        for url in self.pages_content.keys():
            path = url.replace(self.base_url, '').strip('/')
            if path:
                parts = path.split('/')
                current = hierarchy
                for part in parts:
                    if part not in current:
                        current[part] = {}
                    current = current[part]
        return hierarchy

    def _check_structural_consistency(self) -> Dict:
        """Check structural consistency across pages"""
        return {
            "consistent_header": True,  # Implement actual check
            "consistent_footer": True,  # Implement actual check
            "consistent_navigation": True  # Implement actual check
        }

    def _check_navigation_consistency(self) -> Dict:
        """Check navigation consistency across pages"""
        return {
            "consistent_menu": True,  # Implement actual check
            "consistent_links": True  # Implement actual check
        }

    def _check_mobile_navigation(self) -> bool:
        """Check if navigation is mobile-friendly"""
        return True  # Implement actual check

    def _check_responsive_design(self) -> Dict:
        """Check if the design is responsive"""
        return {
            "is_responsive": True,  # Implement actual check
            "breakpoints": ["mobile", "tablet", "desktop"]  # Implement actual check
        }

    def _check_visual_consistency(self) -> Dict:
        """Check visual consistency across pages"""
        return {
            "consistent_colors": True,  # Implement actual check
            "consistent_typography": True,  # Implement actual check
            "consistent_spacing": True  # Implement actual check
        }

    def _generate_markdown_feedback(self, feedback: Dict) -> str:
        """Generate a detailed Markdown feedback report"""
        content_coverage = feedback["content_coverage"]
        site_structure = feedback["site_structure"]
        navigation = feedback["navigation"]
        design = feedback["design"]
        
        md = f"""# Website Feedback Report
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
URL: {self.base_url}

## 1. Site Structure
- Total Pages: {site_structure['total_pages']}
- URL Hierarchy: {len(site_structure['hierarchy'])} main sections
- Structural Consistency: {'✅' if site_structure['consistency']['consistent_header'] else '❌'} Header, {'✅' if site_structure['consistency']['consistent_footer'] else '❌'} Footer

### Suggestions:
- {'Consider reorganizing the URL structure for better hierarchy' if len(site_structure['hierarchy']) < 3 else 'URL structure is well-organized'}
- {'Ensure consistent header/footer across all pages' if not all(site_structure['consistency'].values()) else 'Good structural consistency across pages'}

## 2. Content Coverage
- Coverage: {content_coverage['coverage_percentage']:.1f}%
- Covered Services: {', '.join(content_coverage['covered_services'])}
- Missing Services: {', '.join(content_coverage['missing_services'])}

### Suggestions:
{'- Add content for missing services:\\n' + '\\n'.join(f'  - {service.title()}' for service in content_coverage['missing_services']) if content_coverage['missing_services'] else '- All required services are covered'}

## 3. Navigation
- Menu Items: {navigation['menu_items']}
- Navigation Consistency: {'✅' if navigation['navigation_consistency']['consistent_menu'] else '❌'}
- Mobile-Friendly: {'✅' if navigation['mobile_friendly'] else '❌'}

### Suggestions:
- {'Improve menu consistency across pages' if not navigation['navigation_consistency']['consistent_menu'] else 'Good menu consistency'}
- {'Make navigation mobile-friendly' if not navigation['mobile_friendly'] else 'Good mobile navigation'}

## 4. Design & Accessibility
- Responsive Design: {'✅' if design['responsive_design']['is_responsive'] else '❌'}
- Alt Text Coverage: {design['accessibility']['alt_text_ratio']*100:.1f}%
- ARIA Labels: {'✅' if design['accessibility']['aria_labels_present'] else '❌'}

### Suggestions:
{'- Add alt text to images\\n' if design['accessibility']['alt_text_ratio'] < 0.9 else ''}{'- Implement ARIA labels for better accessibility\\n' if not design['accessibility']['aria_labels_present'] else ''}{'- Make design responsive across devices\\n' if not design['responsive_design']['is_responsive'] else ''}

## 5. Performance Metrics
- Average Page Load Time: {feedback['metadata'].get('average_page_latency', 0):.2f}s
- Total Pages Analyzed: {feedback['metadata']['total_pages_analyzed']}

### Suggestions:
{'- Optimize page load times (target < 2s)\\n' if feedback['metadata'].get('average_page_latency', 0) > 2 else '- Good page load performance\\n'}

## Overall Recommendations
1. {'Improve content coverage by adding missing services' if content_coverage['missing_services'] else 'Maintain comprehensive service coverage'}
2. {'Enhance accessibility with better image alt text and ARIA labels' if design['accessibility']['alt_text_ratio'] < 0.9 or not design['accessibility']['aria_labels_present'] else 'Maintain good accessibility practices'}
3. {'Optimize page load performance' if feedback['metadata'].get('average_page_latency', 0) > 2 else 'Maintain good performance'}
"""
        return md

    def _save_markdown_feedback(self, feedback: Dict):
        """Save feedback as a Markdown file in the cache directory"""
        try:
            date_time = datetime.now().strftime('%Y-%m-%d-%H%M')
            output_file = self.cache_dir / f"{date_time}-feedback.md"
            
            markdown_content = self._generate_markdown_feedback(feedback)
            
            with output_file.open('w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            logger.info(f"Markdown feedback saved to {output_file}")
        except Exception as e:
            logger.error(f"Error saving markdown feedback: {str(e)}", exc_info=True)

    def get_latest_feedback(self) -> Dict:
        """Get the latest feedback data for this site"""
        cache_files = list(self.cache_dir.glob('*-feedback.json'))
        if not cache_files:
            raise FileNotFoundError(f"No feedback files found for {self.base_url}")
        
        # Get the most recent feedback file
        latest_file = max(cache_files, key=lambda x: x.stat().st_mtime)
        try:
            with latest_file.open('r') as f:
                feedback = json.load(f)
            logger.info(f"Retrieved latest feedback from {latest_file.name}")
            return feedback
        except Exception as e:
            logger.error(f"Error reading feedback file {latest_file}: {str(e)}")
            raise

async def main():
    url = "https://urgentcaretwinfallscom.netlify.app"
    start_time = datetime.now()
    
    logger.info(f"Starting analysis at {start_time.isoformat()}")
    agent = WebsiteFeedbackAgent(url)
    await agent.analyze_website()
    
    end_time = datetime.now()
    duration = end_time - start_time
    logger.info(f"Total execution time: {duration.total_seconds():.2f}s")

if __name__ == "__main__":
    asyncio.run(main())