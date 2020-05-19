from tkinter import *

root = Tk()



# 多选框用法
GIRLS=['西施',"貂蝉",'王昭君','杨玉环']
v=[]

for girl in GIRLS:
	v.append(IntVar())
	b=Checkbutton(root,text=girl,variable=v[-1])
	b.pack(anchor='w')
	l=Label(root,textvariable=v[-1])
	l.pack()

# #单选框用法
# v=IntVar()
# Radiobutton(root,text="one",variable=v,value=122).pack(anchor=W)
# Radiobutton(root,text="two",variable=v,value=2).pack(anchor=W)
# Radiobutton(root,text="three",variable=v,value=3).pack(anchor=W)
# l=Label(root,textvariable=v)
# l.pack()



# #### 单选框配合框架
# group = LabelFrame(root,text="最好的脚本语言是？",padx=5,pady=5)
# group.pack(padx=10,pady=10)

# LANGUAGES = [
# 	('python',1),
# 	('java',2),
# 	('html',3),
# 	('ruby',4),
# 	('css',5)
# 	]
# v=IntVar()
# v.set(1)

# for lang,num in LANGUAGES:
# 	b=Radiobutton(group,text=lang,variable=v,value=num)
# 	b.pack(anchor=W)	#横向对齐
# 	# b.pack(fill=X)		#纵向对齐


mainloop()



