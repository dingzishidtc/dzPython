#敌方坦克随机移动
#敌方坦克数量动态修改
#


import pygame
import time,random

SCREEN_WIDTH=700
SCREEN_HEIGHT=500
BG_COLOR=pygame.Color(0,0,0) #三个0是黑色
TEXT_COLOR=pygame.Color(255,0,0)#这是红色
class MainGame():
	window=None
	my_tank=None
	#存储地方坦克的列表
	enemyTankList=[]
	#定义敌方坦克的数量
	enemyTankCount=5

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

		#初始化敌方坦克，并将敌方坦克添加到列表中
		self.createEnemyTank()

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
			MainGame.window.blit(self.getTextSuface("敌方坦克剩余数量:%d"%len(MainGame.enemyTankList)),(10,10))
			#调用坦克显示的方法
			MainGame.my_tank.displayTank()
			#遍历敌方坦克列表，展示敌方坦克
			self.blitEnemyTank()
			#调用移动方法，使得坦克可以一直移动
			#如果坦克的开关是开启才可以移动
			if not MainGame.my_tank.stop:
				MainGame.my_tank.move()	
			
			pygame.display.update()

	##初始化敌方坦克，并将敌方坦克添加到列表中
	def createEnemyTank(self):
		top = 100
		#循环生成敌方坦克
		for i in range(MainGame.enemyTankCount):
			left =random.randint(0,600)
			speed = random.randint(1,3)
			#随机生成一个敌方坦克
			enemy = EnemyTank(left,top,speed)
			MainGame.enemyTankList.append(enemy)

	# 循环遍历敌方坦克列表，展示敌方坦克
	def blitEnemyTank(self):
		for enemyTank in MainGame.enemyTankList:
			enemyTank.displayTank()
			enemyTank.randMove()

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
					MainGame.my_tank.direction="L"
					#修改坦克移动的开关状态
					MainGame.my_tank.stop=False
					print("zuo")
				elif event.key == pygame.K_RIGHT:
					#切换方向
					MainGame.my_tank.direction="R"
					#修改坦克移动的开关状态
					MainGame.my_tank.stop=False
					print("you")
				elif event.key == pygame.K_UP:
					#切换方向
					MainGame.my_tank.direction="U"
					#修改坦克移动的开关状态
					MainGame.my_tank.stop=False
					print("shang")
				elif event.key == pygame.K_DOWN:
					#切换方向
					MainGame.my_tank.direction="D"
					#修改坦克移动的开关状态
					MainGame.my_tank.stop=False
					print("xia")
				elif event.key == pygame.K_SPACE:
					print("发射biubiubiu~")
			#松开方向键，坦克停止移动，修改坦克的移动开关
			if event.type == pygame.KEYUP:
				#判断松开的键是上下左右的时候才停止，释放空格键（子弹）是不停止移动的
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					MainGame.my_tank.stop=True


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
		self.direction='U'
		#根据当前图片的方向获取图片
		self.image = self.images[self.direction]
		#根据图片获取区域
		self.rect=self.image.get_rect()
		#设置区域的left和top
		self.rect.left=left
		self.rect.top=top 
		#速度决斗移动的快慢
		self.speed=4
		#坦克移动的开关
		self.stop=True



	#移动
	def move(self):
		# 判断坦克的方向进行移动
		if self.direction=="L" and int(self.rect.left)>0:
			self.rect.left-=self.speed
		elif self.direction=="U" and int(self.rect.top)>0:
			self.rect.top-=self.speed
		elif self.direction=="D" and int(self.rect.top+self.rect.height)<500:
			self.rect.top+=self.speed
		elif self.direction=="R" and int(self.rect.left+self.rect.height)<700:
			self.rect.left+=self.speed
	# 射击
	def shot(self):
		pass

	#展示坦克
	def displayTank(self):
		#获取展示的对象
		self.image=self.images[self.direction]
		#调用blit方法展示
		MainGame.window.blit(self.image,self.rect)

#我方坦克
class MyTank(Tank):
	def __init__(self):
		pass

#敌方坦克
class EnemyTank(Tank):
	def __init__(self,left,top,speed):
		#加载地方坦克的图片
		self.images={
		"U":pygame.image.load("img/U1.jpg"),
		"D":pygame.image.load("img/D1.jpg"),
		"L":pygame.image.load("img/L1.jpg"),
		"R":pygame.image.load("img/R1.jpg")
		}
		#地方坦克的方向为随机
		self.direction= self.randomDirection()
		#根据当前图片的方向获取图片
		self.image = self.images[self.direction]
		#根据图片获取区域
		self.rect=self.image.get_rect()
		#设置区域的left和top
		self.rect.left=left
		self.rect.top=top 
		#速度决斗移动的快慢
		self.speed=2
		#坦克移动的开关
		self.flag=True
		#步数变量
		self.step=60

	#敌方坦克随机移动的方法
	def randMove(self):
		if self.step<=0:
			# 随机修改一个方向
			self.direction=self.randomDirection()
			#让步数复位
			self.step=60
		else:
			self.move()
			#让步数递减
			self.step-=1
	
	def randomDirection(self):
		num=random.randint(1,4)
		if num == 1:
			return "U"
		elif num==2:
			return "D"
		elif num == 3:
			return "L"
		elif num == 4:
			return "R"


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