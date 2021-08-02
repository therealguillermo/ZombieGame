import pygame
import os
import math
from entity import entity
from healthBars import enemyHealthBar

class enemy(entity):
	def __init__(self, x, y, width, height, img, health):
		super().__init__(x, y, width, height, img)
		self.xvel = 0
		self.yvel = 0
		self.health = health
		self.healthBar = enemyHealthBar(health)
	
	def angleToPlayer(self, playerPos, x, y):
		angle = math.atan2(playerPos[1] - (y), playerPos[0] - (x)) * 180 / math.pi;
		if angle < 0:
			angle += 360
		return angle
	
	def fixImage(self, playerPos):
		angle = self.angleToPlayer(playerPos, self.centerx, self.centery)
		self.angle = -(angle + 90)
		image = self.orgImg
		self.img = pygame.transform.rotate(image, self.angle)
		oldCenter = self.rect.center
		self.rect = self.img.get_rect()
		self.rect.center = oldCenter

	#BUG - angleToMouse needs center of image, corner is currently being used
	def updateVel(self, playerPos):
		angle = self.angleToPlayer(playerPos, self.centerx, self.centery)
		angle = 360 - angle
		angle += 90
		self.xvel = self.speed * math.sin(math.radians(angle))
		self.yvel = self.speed * math.cos(math.radians(angle))

class fastZombie(enemy):
	def __init__(self, x, y):
		self.orgImg = pygame.image.load(os.path.join('images', 'fastZombie.png'))
		width, height = 64, 64
		self.orgImg = pygame.transform.scale(self.orgImg, (width, height))
		super().__init__(x, y, width, height, self.orgImg, 10)
		self.speed = 3
		self.hitBoxSize = 12
		self.dmg = 5


class zombie(enemy):
	def __init__(self, x, y):
		self.orgImg = pygame.image.load(os.path.join('images', 'zombie.png'))
		width, height = 120, 120
		self.orgImg = pygame.transform.scale(self.orgImg, (width, height))
		super().__init__(x, y, width, height, self.orgImg, 20)
		self.speed = 2
		self.hitBoxSize = 15
		self.dmg = 10


class bigZombie(enemy):
	def __init__(self, x, y):
		self.orgImg = pygame.image.load(os.path.join('images', 'bigZombie.png'))
		width, height = 120, 120
		self.orgImg = pygame.transform.scale(self.orgImg, (width, height))
		super().__init__(x, y, width, height, self.orgImg, 40)
		self.speed = 1
		self.hitBoxSize = 40
		self.dmg = 30