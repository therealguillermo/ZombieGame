import pygame
from pygame import *
import random
from game import Game
from player import Player
from player import Bullet


win = pygame.display.set_mode((1600,900 ))

game = Game()
player = Player(800, 450)

running = True
#main game loop#
while running:
	game.tick += 1
	win.fill((255, 255, 255))
	game.clock.tick(game.FPS)
	for event in pygame.event.get():        
		if event.type == pygame.QUIT:
			running = False
	if game.playerHealth <= 0:
		running = False


	click = pygame.mouse.get_pressed()
	mpos = pygame.mouse.get_pos()
	keys = pygame.key.get_pressed()

	if keys[K_w]:
		player.move(0, -2)
	if keys[K_a]:
		player.move(-2, 0)
	if keys[K_s]:
		player.move(0, 2)
	if keys[K_d]:
		player.move(2, 0)

	player.fixImage(mpos)
	player.draw(win)


	if click[0] and not game.shooting:
		b = Bullet(player.getPos(), mpos)
		b.fixImage(player.getPos(), mpos)
		game.bullets.append(b)
		game.shooting = True
	else: 
		if game.tick % 10 == 0: 
			game.shooting = False


	for bullet in game.bullets:
		bullet.move(bullet.xvel, bullet.yvel)
		if bullet.isOut():
			for match in game.bullets:
				count = 0
				if match == bullet:
					game.bullets.pop(count)
				else:
					count+=1
		else:	
			bullet.draw(win)


	game.updateEnemyCount()
	game.checkCollide(player.getPos())
	print(player.getPos())
	for enemy in game.enemies:
		enemy.fixImage(player.getPos())
		enemy.updateVel(player.getPos())
		enemy.move(enemy.xvel, enemy.yvel)
		enemy.draw(win)


	game.healthBar.drawPlayerBar(win, game.playerHealth)
	for enemy in game.enemies:
		enemy.healthBar.drawHealthBar(win, enemy.centerx, enemy.rect.top, enemy.health)












	pygame.display.update()        

#########################


pygame.quit()