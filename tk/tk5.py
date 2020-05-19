from tkinter import *



root=Tk()



Label(root,text='用户名：').grid(row=0,column=0)

Label(root,text='密码：').grid(row=1,column=0)

v1=StringVar()
v2=StringVar()
b1=Entry(root,textvariable=v1)
b1.grid(row=0,column=1,padx=10,pady=5)
b2=Entry(root,textvariable=v2,show="*")
b2.grid(row=1,column=1,padx=10,pady=5)

def show():
	print("用户名：	《%s》"% b1.get())
	print("密码：	%s"% b2.get())
	# .delete(0,END)

Button(root,text="假的登录",command=show)\
	.grid(row=3,column=0,padx=10,pady=5,sticky=W)


Button(root,text="退出",command=root.quit)\
	.grid(row=3,column=1,padx=10,pady=5,sticky=E)



# e.delete(0,END)
# e.insert(0,"66666")


# root.mainloop()
mainloop()
