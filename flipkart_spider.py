import scrapy
from amazon.amazon.items import AmazonItem
import MySQLdb

class AmazonSpider(scrapy.Spider):
	name = 'flipkart'   
	start_urls = [   

	'https://www.flipkart.com/books/educational-and-professional-books/computers-internet-books/pr?sid=bks%2Cenp%2Cwum&q=books&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree%27&sort=relevance&page=1'
	]

	custom_settings={
		'PROXY_POOL_ENABLED':'True',
		'DOWNLOADER_MIDDLEWARES':{
	    	# ...
    		'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    		'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
    		# ...
			},
		'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'	
	}

	def parse(self,response):
		
		pr_name = response.css('._2cLu-l').css('::text').extract()
		pr_tag = response.css('._1rcHFq').css('::text').extract()
		pr_price = response.css('._1vC4OE').css('::text').extract()
		pr_imagelink = response.css('._3BTv9X img::attr(src)').extract()
		
		for i in range(len(pr_name)):

			con=MySQLdb.connect(host ='localhost',user='',password='',database='')
			cur=con.cursor()
			cur.execute("INSERT INTO FLIP values('{}','{}','{}','{}')".format(pr_name[i].replace("'",""),pr_tag[i].replace("'"," "),pr_price[i].replace("₹",""),pr_imagelink[i]))
			con.commit()

			yield {'title':pr_name[i],'tags':pr_tag[i],'price':pr_price[i]}

		con.close()	
