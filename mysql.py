import pandas
import MySQLdb

connection = MySQLdb.connect(
	host='192.168.1.7',
	port=3306,
	db='test',
	user='test',
	password='123',
	charset='utf8'
	)
data=pandas.read_sql("select * from user;",con = connection)
print(data)
connection.close();