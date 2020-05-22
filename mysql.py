import csv
import MySQLdb

connection = MySQLdb.connect(
	host='192.168.1.7',
	port=3306,
	db='test',
	user='test',
	password='123',
	charset='utf8'
	)
# data=pandas.read_sql("select * from user;",con = connection)
# print(data)
# connection.close();

# 逐行打印的方法
#c.rowcount里可以查看sql里总共多少条记录
c=connection.cursor()
c.execute("INSERT INTO user(username,`password`,`age`,sex) "
          "VALUES('as1 s','123','12','男')")
connection.commit()

c.execute("select * from user;")
# c.fetchone()该方法可以打印一条sql记录，每执行一次往下读取一条
#c.fetchmany()可以查询指定条数的记录
raw=[]
for i in range(c.rowcount):
    raw.append(c.fetchone())
    print("第",i+1,"值为：",raw[i])
#c.fetchall()可打印所有数据
# raws=c.fetchall()
print(raw)
