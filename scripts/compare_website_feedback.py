import asyncio
import logging
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from website_feedback_agent import WebsiteFeedbackAgent
import aiohttp

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WebsiteComparator:
    def __init__(self, url1: str, url2: str):
        self.url1 = url1
        self.url2 = url2
        self.agent1 = WebsiteFeedbackAgent(url1)
        self.agent2 = WebsiteFeedbackAgent(url2)
        self.cache_dir = Path('.cache')
        self.cache_dir.mkdir(exist_ok=True)

    async def check_sites_accessibility(self) -> Tuple[bool, bool]:
        """Check if both sites are accessible using simple HTTP requests"""
        logger.info("Checking sites accessibility...")
        
        async def check_url(url: str) -> bool:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        return 200 <= response.status < 400
            except Exception as e:
                logger.error(f"Error accessing {url}: {str(e)}")
                return False

        site1_accessible = await check_url(self.url1)
        site2_accessible = await check_url(self.url2)

        if not site1_accessible:
            logger.error(f"Original site {self.url1} is not accessible")
        if not site2_accessible:
            logger.error(f"New site {self.url2} is not accessible")

        return site1_accessible, site2_accessible

    async def analyze_both_sites(self) -> Tuple[Dict, Dict]:
        """Analyze both websites and return their feedback data"""
        # First check if both sites are accessible
        site1_accessible, site2_accessible = await self.check_sites_accessibility()
        
        if not site1_accessible or not site2_accessible:
            raise RuntimeError(
                f"Cannot proceed with comparison.\n"
                f"Original site ({self.url1}) accessible: {'✅' if site1_accessible else '❌'}\n"
                f"New site ({self.url2}) accessible: {'✅' if site2_accessible else '❌'}"
            )

        # Analyze both sites using their respective agents
        await self.agent1.analyze_website()
        await self.agent2.analyze_website()

        # Get the latest feedback from each agent
        feedback1 = self.agent1.get_latest_feedback()
        feedback2 = self.agent2.get_latest_feedback()

        return feedback1, feedback2

    def _compare_content_coverage(self, feedback1: Dict, feedback2: Dict) -> str:
        """Compare content coverage between sites"""
        coverage1 = feedback1['content_coverage']
        coverage2 = feedback2['content_coverage']

        comparison = [
            "## Content Coverage Comparison",
            f"\n### Original Site ({self.url1})",
            f"- Coverage: {coverage1['coverage_percentage']:.1f}%",
            f"- Covered Services: {', '.join(coverage1['covered_services'])}",
            f"- Missing Services: {', '.join(coverage1['missing_services']) if coverage1['missing_services'] else 'None'}",
            f"\n### New Site ({self.url2})",
            f"- Coverage: {coverage2['coverage_percentage']:.1f}%",
            f"- Covered Services: {', '.join(coverage2['covered_services'])}",
            f"- Missing Services: {', '.join(coverage2['missing_services']) if coverage2['missing_services'] else 'None'}",
            "\n### Improvements",
        ]

        # Calculate improvements
        if coverage2['coverage_percentage'] > coverage1['coverage_percentage']:
            improvement = coverage2['coverage_percentage'] - coverage1['coverage_percentage']
            comparison.append(f"✅ Content coverage improved by {improvement:.1f}%")
            
            new_services = set(coverage2['covered_services']) - set(coverage1['covered_services'])
            if new_services:
                comparison.append(f"✅ New services added: {', '.join(new_services)}")
        elif coverage2['coverage_percentage'] < coverage1['coverage_percentage']:
            decrease = coverage1['coverage_percentage'] - coverage2['coverage_percentage']
            comparison.append(f"❌ Content coverage decreased by {decrease:.1f}%")
            
            removed_services = set(coverage1['covered_services']) - set(coverage2['covered_services'])
            if removed_services:
                comparison.append(f"❌ Services removed: {', '.join(removed_services)}")
        else:
            comparison.append("✓ Content coverage unchanged")

        return '\n'.join(comparison)

    def _compare_performance(self, feedback1: Dict, feedback2: Dict) -> str:
        """Compare performance metrics between sites"""
        # Get metrics from the performance metrics file
        perf1 = feedback1.get('performance_metrics', {}).get('total_runtime', 0)
        perf2 = feedback2.get('performance_metrics', {}).get('total_runtime', 0)
        
        # Get average page latencies
        latency1 = feedback1.get('performance_metrics', {}).get('average_page_latency', 0)
        latency2 = feedback2.get('performance_metrics', {}).get('average_page_latency', 0)

        comparison = [
            "## Performance Comparison",
            f"\n### Original Site ({self.url1})",
            f"- Total Analysis Time: {perf1:.2f}s",
            f"- Average Page Load Time: {latency1:.2f}s",
            f"\n### New Site ({self.url2})",
            f"- Total Analysis Time: {perf2:.2f}s",
            f"- Average Page Load Time: {latency2:.2f}s",
            "\n### Analysis"
        ]

        if latency1 == 0 or latency2 == 0:
            comparison.append("⚠️ Unable to compare page load times - missing data")
        elif latency2 < latency1:
            improvement = ((latency1 - latency2) / latency1) * 100
            comparison.append(f"✅ Page load time improved by {improvement:.1f}%")
        else:
            degradation = ((latency2 - latency1) / latency1) * 100
            comparison.append(f"❌ Page load time increased by {degradation:.1f}%")

        return '\n'.join(comparison)

    def _compare_design(self, feedback1: Dict, feedback2: Dict) -> str:
        """Compare design aspects between sites"""
        design1 = feedback1['design']
        design2 = feedback2['design']

        comparison = [
            "## Design Comparison",
            "\n### Accessibility",
            f"Original Site: {design1['accessibility']['alt_text_ratio']*100:.1f}% alt text coverage",
            f"New Site: {design2['accessibility']['alt_text_ratio']*100:.1f}% alt text coverage",
            "\n### Responsive Design",
            f"Original Site: {'✅' if design1['responsive_design']['is_responsive'] else '❌'}",
            f"New Site: {'✅' if design2['responsive_design']['is_responsive'] else '❌'}"
        ]

        return '\n'.join(comparison)

    def _compare_seo(self, feedback1: Dict, feedback2: Dict) -> str:
        """Compare SEO implementation between sites"""
        seo1 = feedback1.get('seo', {})
        seo2 = feedback2.get('seo', {})

        if not seo1 or not seo2:
            return "## SEO Comparison\n\n⚠️ SEO data not available"

        comparison = [
            "## SEO Comparison",
            f"\n### Original Site ({self.url1})",
            f"- Overall SEO Score: {seo1.get('score', 0):.1f}/100",
            "- Component Scores:",
            f"  - Meta Tags: {seo1.get('scores', {}).get('meta_tags', 0):.1f}/100",
            f"  - Headings: {seo1.get('scores', {}).get('headings', 0):.1f}/100",
            f"  - Content: {seo1.get('scores', {}).get('content', 0):.1f}/100",
            f"  - Links: {seo1.get('scores', {}).get('links', 0):.1f}/100",
            f"  - Images: {seo1.get('scores', {}).get('images', 0):.1f}/100",
            f"\n### New Site ({self.url2})",
            f"- Overall SEO Score: {seo2.get('score', 0):.1f}/100",
            "- Component Scores:",
            f"  - Meta Tags: {seo2.get('scores', {}).get('meta_tags', 0):.1f}/100",
            f"  - Headings: {seo2.get('scores', {}).get('headings', 0):.1f}/100",
            f"  - Content: {seo2.get('scores', {}).get('content', 0):.1f}/100",
            f"  - Links: {seo2.get('scores', {}).get('links', 0):.1f}/100",
            f"  - Images: {seo2.get('scores', {}).get('images', 0):.1f}/100",
            "\n### Analysis & Suggestions"
        ]

        # Compare meta tags
        meta2 = seo2.get('meta_tags', {})
        if meta2.get('missing_meta'):
            comparison.append("\n#### Meta Tags Issues:")
            for missing in meta2['missing_meta']:
                comparison.append(f"- {missing['url']}: Missing {', '.join(missing['missing'])}")

        # Compare headings
        headings2 = seo2.get('headings', {})
        if headings2.get('missing_headings') or headings2.get('h1_usage'):
            comparison.append("\n#### Heading Structure Issues:")
            for missing in headings2.get('missing_headings', []):
                comparison.append(f"- {missing['url']}: Missing H1 tag")
            for h1_issue in headings2.get('h1_usage', []):
                comparison.append(f"- {h1_issue['url']}: Multiple H1 tags ({h1_issue['count']})")

        # Compare content
        content2 = seo2.get('content', {})
        content_issues = []
        for page in content2.get('word_counts', []):
            if page['count'] < 300:
                content_issues.append(f"- {page['url']}: Low word count ({page['count']} words)")
        if content_issues:
            comparison.append("\n#### Content Issues:")
            comparison.extend(content_issues)

        # Compare images
        images2 = seo2.get('images', {})
        if images2.get('missing_alt'):
            comparison.append("\n#### Image Optimization Issues:")
            for missing in images2['missing_alt']:
                comparison.append(f"- {missing['url']}: {missing['count']} images missing alt text")

        # Add improvement suggestions
        comparison.append("\n### Improvement Suggestions:")
        score1 = seo1.get('score', 0)
        score2 = seo2.get('score', 0)
        if score2 < score1:
            decrease = score1 - score2
            comparison.append(f"❌ Overall SEO score decreased by {decrease:.1f} points")
        else:
            improvement = score2 - score1
            comparison.append(f"✅ Overall SEO score improved by {improvement:.1f} points")

        # Add specific recommendations
        recommendations = []
        scores2 = seo2.get('scores', {})
        if scores2.get('meta_tags', 0) < 90:
            recommendations.append("- Add missing meta descriptions and optimize title lengths (30-60 characters)")
        if scores2.get('headings', 0) < 90:
            recommendations.append("- Ensure each page has exactly one H1 tag and proper heading hierarchy")
        if scores2.get('content', 0) < 90:
            recommendations.append("- Increase content length to at least 300 words per page")
        if scores2.get('links', 0) < 90:
            recommendations.append("- Improve internal linking structure (aim for at least 3 internal links per page)")
        if scores2.get('images', 0) < 90:
            recommendations.append("- Add descriptive alt text to all images")

        if recommendations:
            comparison.append("\nPriority Improvements:")
            comparison.extend(recommendations)

        return '\n'.join(comparison)

    def generate_comparison_report(self, feedback1: Dict, feedback2: Dict) -> str:
        """Generate a comprehensive comparison report"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Get metrics for summary
        perf1 = feedback1.get('performance_metrics', {}).get('average_page_latency', 0)
        perf2 = feedback2.get('performance_metrics', {}).get('average_page_latency', 0)
        seo1 = feedback1.get('seo', {}).get('score', 0)
        seo2 = feedback2.get('seo', {}).get('score', 0)
        
        report = [
            "# Website Comparison Report",
            f"Generated on: {timestamp}",
            f"\nOriginal Site: {self.url1}",
            f"New Site: {self.url2}",
            "\n## Summary",
            f"- Content Coverage: {feedback2['content_coverage']['coverage_percentage']:.1f}% ({feedback1['content_coverage']['coverage_percentage']:.1f}% → {feedback2['content_coverage']['coverage_percentage']:.1f}%)",
            f"- Page Load Time: {perf2:.2f}s ({perf1:.2f}s → {perf2:.2f}s)",
            f"- SEO Score: {seo2:.1f}/100 ({seo1:.1f} → {seo2:.1f})",
            f"- Accessibility: {feedback2['design']['accessibility']['alt_text_ratio']*100:.1f}%",
            "\n---",
            self._compare_content_coverage(feedback1, feedback2),
            "\n---",
            self._compare_performance(feedback1, feedback2),
            "\n---",
            self._compare_design(feedback1, feedback2),
            "\n---",
            self._compare_seo(feedback1, feedback2),
            "\n## Overall Assessment"
        ]

        # Add overall assessment
        improvements = []
        if feedback2['content_coverage']['coverage_percentage'] > feedback1['content_coverage']['coverage_percentage']:
            improvements.append(f"- Content coverage improved by {feedback2['content_coverage']['coverage_percentage'] - feedback1['content_coverage']['coverage_percentage']:.1f}%")
        if perf2 < perf1:
            improvements.append(f"- Page load time improved by {((perf1 - perf2) / perf1) * 100:.1f}%")
            improvements.append("- Content coverage has improved")
        if feedback2.get('performance_metrics', {}).get('average_page_latency', 0) < feedback1.get('performance_metrics', {}).get('average_page_latency', 0):
            improvements.append("- Performance has improved")
        if feedback2['design']['accessibility']['alt_text_ratio'] > feedback1['design']['accessibility']['alt_text_ratio']:
            improvements.append("- Accessibility has improved")

        if improvements:
            report.extend(["\n### Improvements", *improvements])
        else:
            report.append("\nNo significant improvements detected")

        return '\n'.join(report)

    def save_comparison_report(self, report: str):
        """Save the comparison report to a file"""
        timestamp = datetime.now().strftime('%Y%m%d-%H%M')
        output_file = self.cache_dir / f"{timestamp}-compare.md"
        
        try:
            with output_file.open('w', encoding='utf-8') as f:
                f.write(report)
            logger.info(f"Comparison report saved to {output_file}")
        except Exception as e:
            logger.error(f"Error saving comparison report: {str(e)}", exc_info=True)

async def main():
    original_url = "https://urgentcaretwinfallscom.netlify.app"
    new_url = "http://localhost:3000"
    
    try:
        comparator = WebsiteComparator(original_url, new_url)
        feedback1, feedback2 = await comparator.analyze_both_sites()
        report = comparator.generate_comparison_report(feedback1, feedback2)
        comparator.save_comparison_report(report)
        logger.info("Comparison completed successfully")
    except Exception as e:
        logger.error(f"Error during comparison: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    asyncio.run(main()) 