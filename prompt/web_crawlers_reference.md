# Web Crawlers Reference Guide

## Major Search Engine Crawlers

### Google
- **User-Agent**: `Googlebot`, `Googlebot-Image`, `Googlebot-News`, `Googlebot-Video`
- **Description**: Google's primary crawler for web pages, images, news, and video content
- **Rate**: ~200 requests per second per IP
- **Respects**: robots.txt, meta robots tags, noindex directives

### Bing (Microsoft)
- **User-Agent**: `Bingbot`, `msnbot`, `msnbot-media`
- **Description**: Microsoft's search engine crawler
- **Rate**: ~100 requests per second per IP
- **Respects**: robots.txt, meta robots tags

### Yahoo
- **User-Agent**: `Slurp`, `Yahoo! Slurp`
- **Description**: Yahoo's web crawler (now powered by Bing)
- **Rate**: Moderate
- **Respects**: robots.txt, meta robots tags

### DuckDuckGo
- **User-Agent**: `DuckDuckBot`
- **Description**: Privacy-focused search engine crawler
- **Rate**: Conservative
- **Respects**: robots.txt, meta robots tags

## Social Media Crawlers

### Facebook
- **User-Agent**: `facebookexternalhit`, `Facebot`
- **Description**: Crawls pages for link previews and sharing
- **Rate**: Moderate
- **Respects**: robots.txt, Open Graph tags

### Twitter
- **User-Agent**: `Twitterbot`
- **Description**: Crawls pages for Twitter card previews
- **Rate**: Moderate
- **Respects**: robots.txt, Twitter Card meta tags

### LinkedIn
- **User-Agent**: `LinkedInBot`
- **Description**: Crawls pages for LinkedIn link previews
- **Rate**: Moderate
- **Respects**: robots.txt

### Pinterest
- **User-Agent**: `Pinterest`
- **Description**: Crawls pages for Pinterest pin previews
- **Rate**: Moderate
- **Respects**: robots.txt

## E-commerce & Shopping Crawlers

### Amazon
- **User-Agent**: `Amazonbot`
- **Description**: Amazon's product search crawler
- **Rate**: Moderate
- **Respects**: robots.txt

### eBay
- **User-Agent**: `eBayBot`
- **Description**: eBay's product search crawler
- **Rate**: Moderate
- **Respects**: robots.txt

## Analytics & Monitoring Crawlers

### Ahrefs
- **User-Agent**: `AhrefsBot`
- **Description**: SEO tool crawler for backlink analysis
- **Rate**: Aggressive
- **Respects**: robots.txt

### Semrush
- **User-Agent**: `SemrushBot`
- **Description**: SEO tool crawler for competitive analysis
- **Rate**: Moderate
- **Respects**: robots.txt

### Moz
- **User-Agent**: `Mozbot`
- **Description**: SEO tool crawler (Moz)
- **Rate**: Moderate
- **Respects**: robots.txt

### Majestic
- **User-Agent**: `MJ12bot`
- **Description**: SEO tool crawler for link analysis
- **Rate**: Aggressive
- **Respects**: robots.txt

## Academic & Research Crawlers

### Internet Archive
- **User-Agent**: `ia_archiver`
- **Description**: Wayback Machine crawler for web archiving
- **Rate**: Conservative
- **Respects**: robots.txt

### Common Crawl
- **User-Agent**: `CCBot`
- **Description**: Open web crawling project
- **Rate**: Conservative
- **Respects**: robots.txt

## Malicious & Scraping Bots

### Generic Scrapers
- **User-Agent**: `Python-urllib`, `curl`, `wget`, `scraper`
- **Description**: Various scraping tools and scripts
- **Rate**: Variable (often aggressive)
- **Respects**: Sometimes robots.txt

### Content Thieves
- **User-Agent**: `CopyScrape`, `ContentThief`, `ArticleGrabber`
- **Description**: Bots designed to steal content
- **Rate**: Aggressive
- **Respects**: Rarely robots.txt

## Testing Environment Considerations

### For Your Web Crawler Testing Environment

#### Crawlers to Monitor:
1. **Googlebot** - Most important for SEO testing
2. **Bingbot** - Second most important
3. **Social media bots** - For link preview testing
4. **SEO tool bots** - For competitive analysis testing

#### robots.txt Configuration:
```
User-agent: *
Disallow: /logs/
Disallow: /prompt/
Disallow: /code/
Allow: /
```

#### Testing Scenarios:
1. **Crawler Discovery**: Test if crawlers can find your pages
2. **Link Following**: Test if crawlers follow internal links
3. **Image Crawling**: Test if crawlers access images
4. **Robots.txt Compliance**: Test if crawlers respect disallowed directories
5. **Sitemap Usage**: Test if crawlers use your sitemap.xml

#### Monitoring Tools:
- **Server logs** - Track crawler access patterns
- **Google Search Console** - Monitor Googlebot activity
- **Bing Webmaster Tools** - Monitor Bingbot activity
- **Analytics platforms** - Track crawler traffic

## Best Practices for Testing

### 1. Rate Limiting
- Implement reasonable rate limits
- Monitor for aggressive crawling
- Block malicious bots

### 2. Logging
- Log all crawler access
- Track User-Agent strings
- Monitor crawl patterns

### 3. Content Protection
- Use robots.txt for legitimate crawlers
- Implement technical measures for malicious bots
- Monitor for content theft

### 4. Testing Environment
- Use realistic content
- Implement proper link structures
- Test various crawler scenarios
- Monitor crawler behavior in logs

## Common User-Agent Patterns

### Search Engines:
- `*bot*`, `*crawler*`, `*spider*`
- `Googlebot`, `Bingbot`, `Slurp`

### Social Media:
- `*externalhit*`, `*bot*`
- `facebookexternalhit`, `Twitterbot`

### SEO Tools:
- `*bot*` (AhrefsBot, SemrushBot, etc.)
- Often include company names

### Malicious:
- Generic tools: `curl`, `wget`, `Python-urllib`
- Custom names: `scraper`, `thief`, `grabber`

This reference can help you understand and test against various web crawlers in your testing environment. 