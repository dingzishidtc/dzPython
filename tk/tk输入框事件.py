from tkinter import *

root=Tk()

def test():
	if e1.get()=="dingzhi":
		print("right")
		return True
	else:
		print("cuowu")
		e1.delete(0,END)
		return False	

def test1():
	if e2.get() in ("0123456789"):
		print("正确")
		return True
	else:
		print("错误")
		e2.delete(0,END)
		return False

def test1():
	return

# v=StringVar()
v1=StringVar()

#关于输入框的validate参数
#"focusout"会在失去焦点时进行验证（执行validatecommand后面的函数）
#focus，获得失去焦点都会验证
#focusin获得焦点时验证
#key，输入框被编辑时验证
#all，获得、失去焦点、输入框被编辑都会验证
#none，关闭验证，默认即关闭验证
# e1=Entry(root,textvariable=v,validate="focusout",validatecommand=test)
# e1=Entry(root,textvariable=v,validate="key",validatecommand=test)
e2=Entry(root,textvariable=v1,validate="key",validatecommand=test1,
	invalidcommand=test1)


# e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)

mainloop()