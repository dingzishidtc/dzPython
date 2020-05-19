from tkinter import *



root=Tk()

text=Text(root,width=30,height=30)
text.pack()

# text.insert(INSERT,"i lov2 \n")
# text.insert(INSERT,"123123123")

photo=PhotoImage(file="正在读取数据.gif")

def show():
	text.image_create(END,image=photo)
	# print("ssasd")

b1=Button(text,text="dianwo",command=show)
text.window_create(INSERT,window=b1)


mainloop()