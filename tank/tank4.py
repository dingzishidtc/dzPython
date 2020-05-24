import pygame

SCREEN_WIDTH=700
SCREEN_HEIGHT=500
BG_COLOR=pygame.Color(0,0,0) #三个0是黑色
class MainGame():
	window=None
	def __init__(self):
		pass

	#开始游戏
	def startGame(self):
		#加载主窗口
		#初始化窗口
		pygame.display.init()
		#设置窗口大小及显示
		MainGame.window = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
		#设置窗口标题
		pygame.display.set_caption('坦克大战僵尸')
		#使窗口保持显示状态，不加下面的会一闪而过
		while True:
			#给窗口设置填充色
			MainGame.window.fill(BG_COLOR)
			#获取时间
			self.getEvent()
			pygame.display.update()


	# 结束游戏
	def endGame(self):
		print("谢谢使用")
		exit()

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
					print("zuo")
				elif event.key == pygame.K_RIGHT:
					print("you")
				elif event.key == pygame.K_UP:
					print("shang")
				elif event.key == pygame.K_DOWN:
					print("xia")


class Tank():
	def __init__(self):
		pass

	#移动
	def move(self):
		pass
	# 射击
	def shot(self):
		pass

	#展示坦克
	def displayTank(self):
		pass

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