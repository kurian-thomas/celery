# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector


class AmazonPipeline(object):
   
	def __init__(self):
		self.create_connection()
		self.create_table()

	def create_connection(self):
		self.conn=mysql.connector.connect(host ='localhost',user ='root',passwd ='123456789',database = 'scrapy')	
		self.curr=self.conn.cursor()

	def create_table(self):
		self.curr.execute("""DROP TABLE IF EXISTS FLIP""")
		self.curr.execute("""CREATE TABLE FLIP(title varchar(200) PRIMARY KEY,tags varchar(500),price varchar(100),link varchar(2000))""")

	def process_item(self, item, spider):
		self.store_db(item)
		return item
    
	def store_db(self,item):
		self.curr.execute("""INSERT INTO FLIP values(%s,%s,%s,%s)""",(item['pr_name'],item['pr_tag'],item['pr_price'],item['pr_imagelink']))
		self.conn.commit()	

