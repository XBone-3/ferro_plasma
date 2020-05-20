import random
import maintanance as mnt
import cnfg
import pygame
import sys
import level_one


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
	# after uncommenting obstacle_p and obstacle_f add them to obstacle_list
	'''obstacle_p = mnt.ObstacleP()
	obstacle_p.rect.x = random.randint(20, 600)
	obstacle_p.rect.y = random.randint(20, 600)'''
	# obstacle_y_1 = mnt.ObstacleY()
	# obstacle_y_1.rect.x = random.randint(40, 600)
	# obstacle_y_1.rect.y = random.randint(40, 600)
	# obstacle_y_2 = mnt.ObstacleY()
	# obstacle_y_2.rect.x = random.randint(40, 600)
	# obstacle_y_2.rect.y = random.randint(40, 600)
	# obstacle_y_3 = mnt.ObstacleY()
	# obstacle_y_3.rect.x = random.randint(40, 600)
	# obstacle_y_3.rect.y = random.randint(40, 600)
	'''obstacle_f = mnt.ObstacleF()
	obstacle_f.rect.x = random.randint(20, 600)
	obstacle_f.rect.y = random.randint(20, 600)'''
	# obstacle_x_1 = mnt.ObstacleX()
	# obstacle_x_1.rect.x = random.randint(20, 600)
	# obstacle_x_1.rect.y = random.randint(100, 600)
	# obstacle_x_2 = mnt.ObstacleX()
	# obstacle_x_2.rect.x = random.randint(20, 600)
	# obstacle_x_2.rect.y = random.randint(100, 600)
	# obstacle_x_3 = mnt.ObstacleX()
	# obstacle_x_3.rect.x = random.randint(20, 600)
	# obstacle_x_3.rect.y = random.randint(100, 600)

	obstacle_p_1 = mnt.ObstacleP()
	obstacle_p_1.rect.x = random.randint(cnfg.SCREENSIZE[0] // 4, cnfg.SCREENSIZE[0] // 2)
	obstacle_p_1.rect.y = random.randint(cnfg.SCREENSIZE[0] // 4, cnfg.SCREENSIZE[0] // 2)

	obstacle_list = pygame.sprite.Group()
	player_list = pygame.sprite.Group()
	destination_list = pygame.sprite.Group()

	player_list.add(player)
	obstacle_list.add(obstacle_p_1)
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
				level_one.main_game_loop(world)

		# looser looser bugs killer

		# if player.rect.x in range(obstacle_x_1.rect.x - deduction, obstacle_x_1.rect.x + increment):
		# 	if player.rect.y in range(obstacle_x_1.rect.y - deduction, obstacle_x_1.rect.y + increment):
		# 		mnt.game_over_screen_interface(world, cnfg.SCREENSIZE)
		#
		# if player.rect.x in range(obstacle_x_2.rect.x - deduction, obstacle_x_2.rect.x + increment):
		# 	if player.rect.y in range(obstacle_x_2.rect.y - deduction, obstacle_x_2.rect.y + increment):
		# 		mnt.game_over_screen_interface(world, cnfg.SCREENSIZE)
		#
		# if player.rect.x in range(obstacle_x_3.rect.x - deduction, obstacle_x_3.rect.x + increment):
		# 	if player.rect.y in range(obstacle_x_3.rect.y - deduction, obstacle_x_3.rect.y + increment):
		# 		mnt.game_over_screen_interface(world, cnfg.SCREENSIZE)
		#
		# if player.rect.x in range(obstacle_y_1.rect.x - deduction, obstacle_y_1.rect.x + increment):
		# 	if player.rect.y in range(obstacle_y_1.rect.y - deduction, obstacle_y_1.rect.y + increment):
		# 		mnt.game_over_screen_interface(world, cnfg.SCREENSIZE)
		#
		# if player.rect.x in range(obstacle_y_2.rect.x - deduction, obstacle_y_2.rect.x + increment):
		# 	if player.rect.y in range(obstacle_y_2.rect.y - deduction, obstacle_y_2.rect.y + increment):
		# 		mnt.game_over_screen_interface(world, cnfg.SCREENSIZE)
		#
		# if player.rect.x in range(obstacle_y_3.rect.x - deduction, obstacle_y_3.rect.x + increment):
		# 	if player.rect.y in range(obstacle_y_3.rect.y - deduction, obstacle_y_3.rect.y + increment):
		# 		mnt.game_over_screen_interface(world, cnfg.SCREENSIZE)

		world.fill(cnfg.BACKGROUND_BLACK)

		player.update()

		player_list.draw(world)
		obstacle_list.draw(world)
		destination_list.draw(world)

		# obstacle_x_1.movement(20)
		# obstacle_x_2.movement(20)
		# obstacle_x_3.movement(20)
		# obstacle_y_1.movement(20)
		# obstacle_y_2.movement(20)
		# obstacle_y_3.movement(20)

		pygame.display.update()
		clock.tick(cnfg.FRAME_RATE)
