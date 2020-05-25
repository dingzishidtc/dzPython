#我方坦克移动优化

import pygame
import time

SCREEN_WIDTH=700
SCREEN_HEIGHT=500
BG_COLOR=pygame.Color(0,0,0) #三个0是黑色
TEXT_COLOR=pygame.Color(255,0,0)#这是红色
class MainGame():
	window=None
	my_tank=None

	def __init__(self):
		pass

	#开始游戏
	def startGame(self):
		#加载主窗口
		#初始化窗口
		pygame.display.init()
		#设置窗口大小及显示
		MainGame.window = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
		
		#初始化我方坦克
		MainGame.my_tank=Tank(350,250)

		#设置窗口标题
		pygame.display.set_caption('坦克大战僵尸')
		#使窗口保持显示状态，不加下面的会一闪而过
		while True:
			#使坦克移动的速度慢一点
			time.sleep(0.02)
			#给窗口设置填充色
			MainGame.window.fill(BG_COLOR)
			#获取事件
			self.getEvent()
			#绘制文字
			MainGame.window.blit(self.getTextSuface("敌方坦克剩余数量:%d"%6),(10,10))
			#调用坦克显示的方法
			MainGame.my_tank.displayTank()
			#调用移动方法，使得坦克可以一直移动
			#如果坦克的开关是开启才可以移动
			if not (MainGame.my_tank.l_stop and MainGame.my_tank.r_stop and MainGame.my_tank.u_stop and MainGame.my_tank.d_stop):
				MainGame.my_tank.move()	
			
			pygame.display.update()


	# 结束游戏
	def endGame(self):
		print("谢谢使用")
		exit()

	#左上角文字汇智
	def getTextSuface(self,text):
		#初始化字体模块
		pygame.font.init()
		#获取字体font对象
		# print(pygame.font.get_font())#该方法可显示所有可用字体
		font = pygame.font.SysFont("kaiti",18)
		#绘制文字信息
		textSurface = font.render(text,True,TEXT_COLOR)
		return textSurface

	#获取事件
	def getEvent(self):
		#获取所有事件
		eventList = pygame.event.get()

		#遍历事件
		for event in eventList:
			#判断是点击关闭还是键盘按键
			#如果是点击关闭，关闭程序
			if event.type == pygame.QUIT:
				self.endGame()
			#如果是键盘的按下
			if event.type == pygame.KEYDOWN:
				#判断按下的是上下左右
				if event.key == pygame.K_LEFT:
					#切换方向
					MainGame.my_tank.direction.append("L")
					#修改坦克移动的开关状态
					MainGame.my_tank.l_stop=False
					print("zuo")
					print(MainGame.my_tank.direction)
				elif event.key == pygame.K_RIGHT:
					#切换方向
					MainGame.my_tank.direction.append("R")
					#修改坦克移动的开关状态
					MainGame.my_tank.r_stop=False
					print("you")
					print(MainGame.my_tank.direction)
				elif event.key == pygame.K_UP:
					#切换方向
					MainGame.my_tank.direction.append("U")
					#修改坦克移动的开关状态
					MainGame.my_tank.u_stop=False
					print("shang")
					print(MainGame.my_tank.direction)
				elif event.key == pygame.K_DOWN:
					#切换方向
					MainGame.my_tank.direction.append("D")
					#修改坦克移动的开关状态 stop
					MainGame.my_tank.d_stop=False
					print("xia")
					print(MainGame.my_tank.direction)
				elif event.key == pygame.K_SPACE:
					print("发射biubiubiu~")
			#松开方向键，坦克停止移动，修改坦克的移动开关
			if event.type == pygame.KEYUP:
				#判断松开的键是上下左右的时候才停止，释放空格键（子弹）是不停止移动的
				if event.key == pygame.K_UP:
					if len(MainGame.my_tank.direction)==1:
						MainGame.my_tank.dircache="U"
					MainGame.my_tank.direction.remove("U")
					MainGame.my_tank.u_stop=True
				elif event.key == pygame.K_DOWN:
					if len(MainGame.my_tank.direction)==1:
						MainGame.my_tank.dircache="D"
					MainGame.my_tank.direction.remove("D")
					MainGame.my_tank.d_stop=True
				elif event.key == pygame.K_LEFT:
					if len(MainGame.my_tank.direction)==1:
						MainGame.my_tank.dircache="L"
					MainGame.my_tank.direction.remove("L")
					MainGame.my_tank.l_stop=True
				elif event.key == pygame.K_RIGHT:
					if len(MainGame.my_tank.direction)==1:
						MainGame.my_tank.dircache="R"
					MainGame.my_tank.direction.remove("R")
					MainGame.my_tank.r_stop=True



class Tank():
	#添加距离左边多少，距离顶部多少
	def __init__(self,left,top):
		#保存加载的图片
		self.images={
		"U":pygame.image.load("img/U.jpg"),
		"D":pygame.image.load("img/D.jpg"),
		"L":pygame.image.load("img/L.jpg"),
		"R":pygame.image.load("img/R.jpg")
		}
		#坦克的默认方向
		self.direction=[]
		self.dircache=""
		#根据当前图片的方向获取图片
		if self.direction==[] and self.dircache=="":
			self.image = self.images["U"]
		elif self.direction==[]:
			self.image = self.images[self.dircache]
		else:
			self.image = self.images[self.direction[-1]]
		#根据图片获取区域
		self.rect=self.image.get_rect()
		#设置区域的left和top
		self.rect.left=left
		self.rect.top=top 
		#速度决斗移动的快慢
		self.speed=1
		#坦克移动的开关
		self.l_stop=self.r_stop=self.u_stop=self.d_stop=True



	#移动
	def move(self):
		# 判断坦克的方向进行移动
		if self.direction[-1]=="L" and int(self.rect.left)>0:
			self.rect.left-=self.speed
		elif self.direction[-1]=="U" and int(self.rect.top)>0:
			self.rect.top-=self.speed
		elif self.direction[-1]=="D" and int(self.rect.top+self.rect.height)<500:
			self.rect.top+=self.speed
		elif self.direction[-1]=="R" and int(self.rect.left+self.rect.height)<700:
			self.rect.left+=self.speed
	# 射击
	def shot(self):
		pass

	#展示坦克
	def displayTank(self):
		#获取展示的对象
		if self.direction==[] and self.dircache=="":
			self.image = self.images["U"]
		elif self.direction==[]:
			self.image = self.images[self.dircache]
		else:
			self.image = self.images[self.direction[-1]]
		#调用blit方法展示
		MainGame.window.blit(self.image,self.rect)

#我方坦克
class MyTank(Tank):
	def __init__(self):
		pass

#敌方坦克
class EnemyTank(Tank):
	def __init__(self):
		pass

#子弹类
class Buller():
	def __init__(self):
		pass
	#移动
	def move(self):
		pass
	#展示子弹
	def displayBuller(self):
		pass

#墙壁类
class Wall():
	def __init__(self):
		pass
	# 展示墙壁
	def displayWall(self):
		pass

# 爆炸效果类
class Explode():
	def __init__(self):
		pass
	# 展示爆炸效果
	def displayExplode(self):
		pass

# 音乐类
class Music():
	def __init__(self):
		pass
	# 播放音乐
	def play(self):
		pass


#
if __name__=="__main__":
	MainGame().startGame()