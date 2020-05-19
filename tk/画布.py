from tkinter import *
import math as m


root=Tk()

w=Canvas(root,width=200,height=100)
w.pack()

# w.create_line(0,50,200,50,fill="yellow")
# w.create_line(100,0,100,100,fill="red",dash=(4,4))

# w.create_rectangle(50,25,150,75,fill="blue")

center_x=100
center_y=50
r=50

points=[
	#左上点
	center_x-int(r*m.sin(2*m.pi/5)),
	center_y-int(r*m.cos(2*m.pi/5)),
	#右上点
	center_x+int(r*m.sin(2*m.pi/5)),
	center_y-int(r*m.cos(2*m.pi/5)),
	#左下角
	center_x-int(r*m.sin(m.pi/5)),
	center_y+int(r*m.cos(m.pi/5)),
	#顶角
	center_x,
	center_y-r,
	#右下角
	center_x+int(r*m.sin(m.pi/5)),
	center_y+int(r*m.cos(m.pi/5))
]   

w.create_polygon(points,outline="green",fill="yellow")

mainloop()