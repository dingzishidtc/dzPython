from tkinter import *


root=Tk()
photo= PhotoImage(file="背景图.gif")
textLabel=Label(root,
	text="你又在打飞机了\n带我一起打飞机吧",
	justify=LEFT,
	padx=10,
	image=photo,
	compound=CENTER,
	font=("华文行楷",20),
	fg="white"
	)
textLabel.pack()

mainloop()