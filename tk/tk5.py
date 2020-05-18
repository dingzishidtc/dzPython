from tkinter import *



root=Tk()

frame3=Frame(root)
frame1=Frame(frame3)
frame2=Frame(frame3)
frame4=Frame(root)



a1=Label(frame1,text='作品：')
a1.pack(side=TOP,padx=10,pady=20)

a2=Label(frame1,text='作者：')
a2.pack(side=BOTTOM,padx=10,pady=20)


b1=Entry(frame2)
# b1.insert(0,"零基础入门学习python")
b1.pack(padx=10,pady=20,side=TOP)
b2=Entry(frame2)
# b2.insert(0,"初学者：丁枝")
b2.pack(padx=10,pady=20,side=BOTTOM)


def show():
	print("作品：	《%s》"% b1.get())
	print("作者：	%s"% b2.get())
	# .delete(0,END)

Button(frame4,text="获取信息",command=show()).pack(padx=10,pady=20,side=LEFT)

c2=Button(frame4,text="退出",command=root.quit)
c2.pack(padx=10,pady=20,side=RIGHT)


# e.delete(0,END)
# e.insert(0,"66666")



frame1.pack(padx=10,pady=10,side=LEFT)
frame2.pack(padx=10,pady=10,side=RIGHT)
frame3.pack(padx=10,pady=10,side=TOP)
frame4.pack(side=BOTTOM)

root.mainloop()
