import scrapy
from scrapy.crawler import CrawlerProcess as cp
from scrapy.utils.project import get_project_settings
from flipkart_spider import AmazonSpider
import MySQLdb

def run_crawler():    

    process = cp(get_project_settings())
    process.crawl(AmazonSpider)
    process.start(stop_after_crawl=False)

