import pygame
import random
from enemies import fastZombie
from enemies import zombie
from enemies import bigZombie
from healthBars import healthBar
random.seed(5)

def cf():
	return random.randrange(2)

def cf3():
	return random.randrange(3)

class Game(object):
	def __init__(self):
		self.bullets = []
		self.enemies = []
		self.shooting = False
		self.tick = 0
		self.FPS = 60
		self.clock = pygame.time.Clock()
		self.playerHitBoxSize = 15
		self.playerHealth = 100
		self.healthBar = healthBar()

	def updateEnemyCount(self):
		if self.tick % 100 == 0:
			self.enemies.append(self.createNewEnemy())

	def checkCollide(self, playerPos):
		counter = 0
		x, y = playerPos
		for enemy in self.enemies:
			bulletCount = 0
			for bullet in self.bullets:
				if ((enemy.centerx + enemy.hitBoxSize > bullet.centerx) and (enemy.centerx - enemy.hitBoxSize < bullet.centerx)) and ((enemy.centery + enemy.hitBoxSize > bullet.centery) and (enemy.centery - enemy.hitBoxSize < bullet.centery)):
					if enemy.health > 0:
						enemy.health -= 5
					else:
						self.enemies.pop(counter)
					self.bullets.pop(bulletCount)
				bulletCount += 1 
			if ((enemy.centerx + self.playerHitBoxSize > x) and (enemy.centerx - self.playerHitBoxSize < x)) and ((enemy.centery + self.playerHitBoxSize > y) and (enemy.centery - self.playerHitBoxSize < y)): 
				self.enemies.pop(counter)
				self.playerHealth -= enemy.dmg
			counter += 1


	def createNewEnemy(self):
		spawnx = 0
		spawny = 0
		if cf():
			if cf():
				spawnx = random.randrange(-200, -20)
			else:
				spawnx = random.randrange(1620, 1800)
			spawny = random.randrange(-200, 1100)
		else:
			if cf():
				spawny = random.randrange(-200, -20)
			else:
				spawny = random.randrange(920, 1100)
			spawnx = random.randrange(-200, 1800)

		c = cf3()
		if c == 0:
			return fastZombie(spawnx, spawny)
		elif c == 1:
			return bigZombie(spawnx, spawny)
		else:
			return zombie(spawnx, spawny)

