import easygui as g
import sys

while 1:
	g.msgbox('show time')
	msg="你是傻屌吗"
	
	title="傻屌鉴定器"
	choices=['大傻吊','小傻吊',"老傻吊"]

	choice = g.choicebox(msg,title,choices)



	g.msgbox("你是："+str(choice),"结果")

	msg="你想再当一次傻屌吗"
	title="请选择"

	if g.ccbox(msg,title):
		pass
	else:
		sys.exit(0)