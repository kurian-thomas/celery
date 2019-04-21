import scrapy
from scrapy.crawler import CrawlerProcess as cp
from scrapy.utils.project import get_project_settings
from flipkart_spider import AmazonSpider
import MySQLdb
def run_crawler():    
    # process = cp({
    #     'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
    #     })
    process = cp(get_project_settings())
    process.crawl(AmazonSpider)
    process.start(stop_after_crawl=False)
