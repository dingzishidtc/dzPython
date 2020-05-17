# from tkinter import *

# root = Tk()

# v = Intvar()

# c = Checkbutton(root,text="测试一下",variable=v)

# c.pack()

# mainloop()

import redis
import time
import json
import MySQLdb
import MySQLdb
pool=redis.ConnectionPool(host='192.168.60.21',port=6379,db=0)
r=redis.StrictRedis(connection_pool=pool)
#key='_'.join(["gamelog_queue",str(date),str(log),str(cmd),str(response),str(sname),str(uid)])
while True:
    aa=r.brpop("aa",0)

    if aa == None:
        continue

    #print "list brpop:",aa
    bb=aa[0]
    cc=aa[1]
    #print type(bb),cc
    value=[bb,cc]
    #print value
    try:
        dbcon = MySQLdb.connect(host='192.168.9.63', user='dlan', port=3306, passwd='root123', db='suo', charset='utf8')
        db_cursor = dbcon.cursor()
        db_insert="insert into redis_test.redis_data values(null,%s,%s)"
        db_cursor.execute(db_insert,value)
        db_cursor.execute('commit')
    except MySQLdb.Error, e:
        print "error%s", e
