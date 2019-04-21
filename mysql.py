import MySQLdb
con=MySQLdb.connect(host ='localhost',user='',password='',database='')
cur=con.cursor()

cur.execute('DROP TABLE IF EXISTS FLIP')
cur.execute('CREATE TABLE FLIP(title varchar(200) ,tags varchar(500),price varchar(100),link varchar(2000))')
con.close()
print("db all set")