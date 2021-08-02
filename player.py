import pygame
from entity import entity
import os
import math

def angleToMouse(mpos, x, y):
	angle = math.atan2(mpos[1] - (y), mpos[0] - (x)) * 180 / math.pi;
	if angle < 0:
		angle += 360
	return angle

class Player(entity):
	def __init__(self, x, y):
		self.orgImg = pygame.image.load(os.path.join('images', 'player.png'))
		self.orgImg = pygame.transform.scale(self.orgImg, (100, 100))
		self.angle = None
		self.health = 100
		width, height = 100, 100
		super().__init__(x, y, width, height, self.orgImg)

	def fixImage(self, mpos):
		x, y = self.getPos()
		angle = angleToMouse(mpos, x, y)
		self.angle = -(angle + 90)
		image = self.orgImg
		self.img = pygame.transform.rotate(image, self.angle)
		oldCenter = self.rect.center
		self.rect = self.img.get_rect()
		self.rect.center = oldCenter

	
	def getPos(self):
		return self.rect.centerx, self.rect.centery


class Bullet(entity):

	def __init__(self, playerPos, mpos):
		x, y = playerPos
		self.orgImg = pygame.image.load(os.path.join('images', 'bullet.png'))
		self.bulletSpeed = 8
		width, height = 16, 16
		self.xvel = 0
		self.yvel = 0
		self.getVel(playerPos, mpos)
		super().__init__(x - 16, y - 16, width, height, self.orgImg)


	def isOut(self):
		if (0 > self.x or self.x > 1600):
			return True
		elif (0 > self.y or self.y > 900):
			return True
		return False

	def fixImage(self, playerPos, mpos):
		x, y = playerPos
		angle = angleToMouse(mpos, x, y)
		self.angle = -(angle + 90)
		image = self.orgImg
		self.img = pygame.transform.rotate(image, self.angle)

	def getVel(self, playerPos, mpos):
		angle = angleToMouse(mpos, playerPos[0], playerPos[1])
		angle = 360 - angle
		print(angle)
		angle += 90
		self.xvel = self.bulletSpeed * math.sin(math.radians(angle))
		self.yvel = self.bulletSpeed * math.cos(math.radians(angle))

		

