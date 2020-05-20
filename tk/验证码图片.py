#!/usr/bin/python 
# -*- coding : utf-8 -*-


import random,string
from PIL import Image,ImageFont, ImageDraw,ImageFilter


fontPath="./"

#生成随机四个字母
#random.choice(string.ascii_letters)是随机字母
#random.choice(string.digits)是随机数组
def getRandomChar():
	return [random.choice(string.ascii_letters+string.digits) for i in range(4)]

#生成颜色
def getRandomColor():
	return (random.randint(30,100),random.randint(30,100),random.randint(30,100))

#获得验证码图片
def getCodePicture():
	width=240
	height=60	
	#创建画布
	image = Image.new('RGB',(width,height),(180,180,180))
	#设置字体路径+字体+大小
	font = ImageFont.truetype(fontPath+'微软vista楷体.ttf',60)
	draw = ImageDraw.Draw(image)

	#创建验证码对象
	code = getRandomChar()
	#将验证码放到画布上
	for i in range(4):
		draw.text((60*i+10,0),code[i],font = font,fill = getRandomColor())
	#填充噪点
	for i in range(random.randint(1500,3000)):
		draw.point((random.randint(0,width),random.randint(0,height)),fill = getRandomColor())

	#模糊处理
	image = image.filter(ImageFilter.EDGE_ENHANCE)
	#保存名字为验证码的图片
	image.save("验证码"+"".join(code)+".jpg","jpeg");
	print(code)

if __name__=='__main__':
	getCodePicture()