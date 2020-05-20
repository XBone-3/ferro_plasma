import random
import maintanance as mnt
import cnfg
import pygame
import sys


def main_game_loop(world):
	clock = pygame.time.Clock()
	world.fill(cnfg.BACKGROUND_BLACK)
	deduction = 20
	increment = 20
	player = mnt.PlayerInstancing()
	player.rect.x = 10
	player.rect.y = 10
	destination = mnt.DestinationInstancing()
	destination.rect.x = random.randint(500, 610)
	destination.rect.y = random.randint(300, 620)

	obstacle_y_1 = mnt.ObstacleY()
	obstacle_y_1.rect.x = random.randint(40, 600)
	obstacle_y_1.rect.y = random.randint(40, 600)
	obstacle_y_2 = mnt.ObstacleY()
	obstacle_y_2.rect.x = random.randint(40, 600)
	obstacle_y_2.rect.y = random.randint(40, 600)
	obstacle_y_3 = mnt.ObstacleY()
	obstacle_y_3.rect.x = random.randint(40, 600)
	obstacle_y_3.rect.y = random.randint(40, 600)

	obstacle_x_1 = mnt.ObstacleX()
	obstacle_x_1.rect.x = random.randint(20, 600)
	obstacle_x_1.rect.y = random.randint(100, 600)
	obstacle_x_2 = mnt.ObstacleX()
	obstacle_x_2.rect.x = random.randint(20, 600)
	obstacle_x_2.rect.y = random.randint(100, 600)
	obstacle_x_3 = mnt.ObstacleX()
	obstacle_x_3.rect.x = random.randint(20, 600)
	obstacle_x_3.rect.y = random.randint(100, 600)

	obstacle_list = pygame.sprite.Group()
	player_list = pygame.sprite.Group()
	destination_list = pygame.sprite.Group()

	player_list.add(player)
	obstacle_list.add(obstacle_x_1, obstacle_x_2, obstacle_x_3, obstacle_y_1, obstacle_y_2, obstacle_y_3)
	destination_list.add(destination)
	playing = True

	while playing:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP] or keys[pygame.K_w]:
			player.move_up()
		elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
			player.move_down()
		elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			player.move_right()
		elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
			player.move_left()
		elif keys[pygame.K_q]:
			pygame.quit()
			sys.exit()

		# winner winner chicken dinner

		if player.rect.x in range(destination.rect.x - 10, destination.rect.x + 10):
			if player.rect.y in range(destination.rect.y - 10, destination.rect.y + 10):
				mnt.you_win_screen_interface(world, cnfg.SCREENSIZE)

		# looser looser bugs killer

		if player.rect.x in range(obstacle_x_1.rect.x - deduction, obstacle_x_1.rect.x + increment):
			if player.rect.y in range(obstacle_x_1.rect.y - deduction, obstacle_x_1.rect.y + increment):
				mnt.game_over_screen_interface(world, cnfg.SCREENSIZE)

		if player.rect.x in range(obstacle_x_2.rect.x - deduction, obstacle_x_2.rect.x + increment):
			if player.rect.y in range(obstacle_x_2.rect.y - deduction, obstacle_x_2.rect.y + increment):
				mnt.game_over_screen_interface(world, cnfg.SCREENSIZE)

		if player.rect.x in range(obstacle_x_3.rect.x - deduction, obstacle_x_3.rect.x + increment):
			if player.rect.y in range(obstacle_x_3.rect.y - deduction, obstacle_x_3.rect.y + increment):
				mnt.game_over_screen_interface(world, cnfg.SCREENSIZE)

		if player.rect.x in range(obstacle_y_1.rect.x - deduction, obstacle_y_1.rect.x + increment):
			if player.rect.y in range(obstacle_y_1.rect.y - deduction, obstacle_y_1.rect.y + increment):
				mnt.game_over_screen_interface(world, cnfg.SCREENSIZE)

		if player.rect.x in range(obstacle_y_2.rect.x - deduction, obstacle_y_2.rect.x + increment):
			if player.rect.y in range(obstacle_y_2.rect.y - deduction, obstacle_y_2.rect.y + increment):
				mnt.game_over_screen_interface(world, cnfg.SCREENSIZE)

		if player.rect.x in range(obstacle_y_3.rect.x - deduction, obstacle_y_3.rect.x + increment):
			if player.rect.y in range(obstacle_y_3.rect.y - deduction, obstacle_y_3.rect.y + increment):
				mnt.game_over_screen_interface(world, cnfg.SCREENSIZE)

		world.fill(cnfg.BACKGROUND_BLACK)

		player.update()

		player_list.draw(world)
		obstacle_list.draw(world)
		destination_list.draw(world)

		obstacle_x_1.movement(15)
		obstacle_x_2.movement(15)
		obstacle_x_3.movement(15)
		obstacle_y_1.movement(15)
		obstacle_y_2.movement(15)
		obstacle_y_3.movement(15)

		pygame.display.update()
		clock.tick(cnfg.FRAME_RATE)
