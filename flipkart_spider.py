import scrapy
from amazon.amazon.items import AmazonItem

class AmazonSpider(scrapy.Spider):
	name='flipkart' 
	#page_number=2  
	start_urls=[   

	'https://www.flipkart.com/books/educational-and-professional-books/computers-internet-books/pr?sid=bks%2Cenp%2Cwum&q=books&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree%27&sort=relevance&page=1'
	]

	def parse(self,response):
		items=AmazonItem()
		
		pr_name=response.css('._2cLu-l').css('::text').extract()
		pr_tag=response.css('._1rcHFq').css('::text').extract()
		pr_price=response.css('._1vC4OE').css('::text').extract()
		pr_imagelink= response.css('._3BTv9X img::attr(src)').extract()
		print(pr_name)
		for i in range(len(pr_name)):
			items['pr_name']=pr_name[i]
			items['pr_tag']=pr_tag[i]
			items['pr_price']=pr_price[i].replace("₹","")
			items['pr_imagelink']=pr_imagelink[i]
			print("new price: "+items['pr_price'])

			yield items
		# next_page='https://www.flipkart.com/books/educational-and-professional-books/computers-internet-books/pr?sid=bks%2Cenp%2Cwum&q=books&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree%27&page='+str(AmazonSpider.page_number)		
		# if(AmazonSpider.page_number <= 10):
		# 	AmazonSpider.page_number+=1
		# 	yield response.follow(next_page,callback = self.parse)
