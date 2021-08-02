import pygame

class healthBar(object):
	def __init__(self):
		self.playerHealth = pygame.Rect(50, 800, 300, 50)
		self.playerHealthRed = pygame.Rect(350, 800, 100, 50)
		self.lastPlayerHealth = 100

	def drawPlayerBar(self, win, playerHealth):
		if self.lastPlayerHealth != playerHealth:
			self.playerHealthRed.update(50, 800, 300, 50)
			self.lastPlayerHealth = playerHealth
		else:
			self.playerHealthRed.update(((playerHealth * 3) + 50), 800, (300 - (playerHealth * 3)), 50)
		pygame.draw.rect(win, (0, 255, 0), self.playerHealth)
		pygame.draw.rect(win, (255, 0, 0), self.playerHealthRed)

class enemyHealthBar(object):
	def __init__(self, health):
		self.lastHealth = health
		self.currHealth = health
		self.healthBar = pygame.Rect(0, 0, 50, 10)
		self.healthBarRed = pygame.Rect(0, 0, 0, 10)
		self.healthBarLeft = 0
		self.hits = health / 5

	def drawHealthBar(self, win, centerx, top, enemyHealth):
		currHealth = enemyHealth
		self.healthBar.center = (centerx, top + 20)
		self.healthBar.left = centerx - 25
		self.healthBarRed.center = (centerx, top + 20)
		self.healthBarRed.right = centerx + 25
		if self.lastHealth != currHealth:
			change = (1 / (self.hits + 1)) * 50
			self.healthBarRed.width += change + 1
			self.healthBar.width -= change
		self.lastHealth = currHealth
		pygame.draw.rect(win, (0, 255, 0), self.healthBar)
		pygame.draw.rect(win, (255, 0, 0), self.healthBarRed)
