import os
import re
a=""
with open('三国演义.txt', 'r', encoding='utf-8') as f:
    a=f.read()

os.mkdir(os.getcwd()+'\\三国演义') if not os.path.exists('三国演义') else ""
b=a.split("------------")
n=1
for i in b:
    # print(i)
    pattern = re.compile(r'(第\S+回\s+\S+\s+\S+)')
    result = pattern.findall(i)
    print(result[0])
    f = open(os.getcwd()+"\\三国演义\\%s %s.txt"% (n,result[0]), 'w',encoding="utf-8")
    n+=1
    f.write(i)
    f.close



