from tkinter import *

def callback():
	var.set("傻屌")

root=Tk()

frame1=Frame(root)
frame2=Frame(root)

var=StringVar()
var.set("你又在打飞机了\n带我一起打飞机吧")
textLabel=Label(frame1,
	textvariable=var,
	justify=LEFT,
	padx=10
	)
textLabel.pack(side=LEFT)

photo= PhotoImage(file="正在读取数据.gif")
imgLabel=Label(frame2,image=photo)
imgLabel.pack(side=RIGHT)

theButton=Button(frame2,text="不行",command=callback)
theButton.pack()

frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)
mainloop()