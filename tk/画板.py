from tkinter import *


root=Tk()

#生成画布
w=Canvas(root,width=400,height=200)
w.pack()

def paint(enent):
	x1,y1=(enent.x-1),(enent.y-1)
	x2,y2=(enent.x+1),(enent.y+1)
	w.create_oval(x1,y1,x2,y2,fill="red")

#画布绑定鼠标左键
w.bind("<B1-Motion>",paint)

Label(root,text="开始画画吧").pack(side=BOTTOM)

mainloop()