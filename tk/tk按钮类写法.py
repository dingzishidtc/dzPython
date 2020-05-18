import tkinter as tk

class APP:
	def __init__(self,master):
		frame = tk.Frame(master)
		frame.pack(side=tk.LEFT,padx=100,pady=100)

		self.hi_there=tk.Button(frame,text="打飞机",fg="red",command=self.say_hi)
		self.hi_there.pack()

	def say_hi(self):
		print("请不要天天打飞机")

root = tk.Tk()
app = APP(root)

#主事件循环
root.mainloop()

