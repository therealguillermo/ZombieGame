import pygame
import math

class entity(object):
	def __init__(self, x, y, width, height, img):
		self.x = x
		self.y = y
		self.width = width
		self.height = height 
		self.img = img
		self.rect = self.img.get_rect()
		self.rect.topleft = (self.x, self.y)
		self.centerx = self.rect.centerx
		self.centery = self.rect.centery

	def move(self, x, y):
		self.x += x
		self.y += y
		self.rect.topleft = (self.x, self.y)
		self.centerx = self.rect.centerx
		self.centery = self.rect.centery


	def draw(self, win):
		win.blit(self.img, (self.x, self.y))
