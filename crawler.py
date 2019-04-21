import scrapy

from scrapy.crawler import CrawlerProcess as cp

from flipkart_spider import AmazonSpider

def run_crawler():    
    process = cp({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })

    process.crawl(AmazonSpider)
    process.start()