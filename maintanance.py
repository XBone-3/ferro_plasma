import random
import Game_start
import cnfg
import pygame
import sys
import random


class PlayerInstancing(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image_path = cnfg.player_IMAGE_PATH
		self.image = pygame.image.load(cnfg.player_IMAGE_PATH)
		self.rect = self.image.get_rect()

	def move_up(self):
		if 0 <= self.rect.y <= 600:
			# self.move_y -= 1
			self.rect.y = self.rect.y - 5
		else:
			pygame.quit()
			sys.exit()

	def move_down(self):
		if 0 <= self.rect.y <= 600:
			# self.move_y += 1
			self.rect.y = self.rect.y + 5
		else:
			pygame.quit()
			sys.exit()

	def move_left(self):
		if 0 <= self.rect.x <= 600:
			# self.move_x -= 1
			self.rect.x = self.rect.x - 5
		else:
			pygame.quit()
			sys.exit()

	def move_right(self):
		if 0 <= self.rect.x <= 600:
			# self.move_x += 1
			self.rect.x = self.rect.x + 5
		else:
			pygame.quit()
			sys.exit()


class DestinationInstancing(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(cnfg.DESTINATION_IMAGE_PATH)
		self.rect = self.image.get_rect()


class ObstacleX(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.obstacle_x_path = cnfg.OBSTACLE_IMAGE_X_PATH
		self.image = pygame.image.load(self.obstacle_x_path)
		self.rect = self.image.get_rect()

	def movement(self):
		if 0 < self.rect.x < 640:
			self.rect.x = self.rect.x - 15
		elif self.rect.x < 0:
			self.rect.x = self.rect.x + 15
			while self.rect.x < 640:
				self.rect.x = self.rect.x + 15
			self.rect.x = self.rect.x - 15


class ObstacleY(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.obstacle_y_path = cnfg.OBSTACLE_IMAGE_Y_PATH
		self.image = pygame.image.load(self.obstacle_y_path)
		self.rect = self.image.get_rect()

	def movement(self):
		if 0 < self.rect.y < 640:
			self.rect.y = self.rect.y - 15
		elif self.rect.y < 0:
			self.rect.y = self.rect.y + 15
			while self.rect.y < 640:
				self.rect.y = self.rect.y + 15
			self.rect.y = self.rect.y - 15


class ObstacleP(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.obstacle_p_path = cnfg.OBSTACLE_IMAGE_P_PATH
		self.image = pygame.image.load(self.obstacle_p_path)
		self.rect = self.image.get_rect()


class ObstacleR(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.obstacle_r_path = cnfg.OBSTACLE_IMAGE_R_PATH
		self.image = pygame.image.load(self.obstacle_r_path)
		self.rect = self.image.get_rect()


class ObstacleF(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.obstacle_f_path = cnfg.OBSTACLE_IMAGE_F_PATH
		self.image = pygame.image.load(self.obstacle_f_path)
		self.rect = self.image.get_rect()


def start_screen_interface(world, screen_size):
	world.fill(cnfg.BACKGROUND_START_SCREEN)
	title_font = pygame.font.Font(cnfg.TITLE_FONT_PATH, screen_size[0] // 10)
	content_font = pygame.font.Font(cnfg.CONTENT_FONT_PATH, screen_size[0] // 20)
	title = title_font.render('Hard game ever', True, cnfg.TITLE_FONT_COLOR)
	content = content_font.render('my version', True, cnfg.CONTENT_FONT_COLOR)
	instruction = content_font.render('press "s" to start', True, (20, 20, 20))
	title_rect = title.get_rect()
	title_rect.midtop = (screen_size[0] / 2, screen_size[1] / 3)
	content_rect = content.get_rect()
	content_rect.midtop = (screen_size[0] / 2, screen_size[1] / 2)
	instruction_rect = instruction.get_rect()
	instruction_rect.midtop = (screen_size[0] / 2, screen_size[1] - 80)
	world.blit(title, title_rect)
	world.blit(content, content_rect)
	world.blit(instruction, instruction_rect)
	while True:
		key = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if key[pygame.K_s]:
				return
		pygame.display.update()


def game_loop(world):
	clock = pygame.time.Clock()
	world.fill(cnfg.BACKGROUND_BLACK)
	player = PlayerInstancing()
	player.rect.x = 10
	player.rect.y = 10
	destination = DestinationInstancing()
	destination.rect.x = random.randint(30, 610)
	destination.rect.y = random.randint(530, 620)
	# after uncommenting obstacle_p and obstacle_f add them to obstacle_list
	'''obstacle_p = mnt.ObstacleP()
	obstacle_p.rect.x = random.randint(20, 600)
	obstacle_p.rect.y = random.randint(20, 600)'''
	obstacle_y_1 = ObstacleY()
	obstacle_y_1.rect.x = random.randint(20, 600)
	obstacle_y_1.rect.y = random.randint(20, 600)
	obstacle_y_2 = ObstacleY()
	obstacle_y_2.rect.x = random.randint(20, 600)
	obstacle_y_2.rect.y = random.randint(20, 600)
	obstacle_y_3 = ObstacleY()
	obstacle_y_3.rect.x = random.randint(20, 600)
	obstacle_y_3.rect.y = random.randint(20, 600)
	'''obstacle_f = mnt.ObstacleF()
	obstacle_f.rect.x = random.randint(20, 600)
	obstacle_f.rect.y = random.randint(20, 600)'''
	obstacle_x_1 = ObstacleX()
	obstacle_x_1.rect.x = random.randint(20, 600)
	obstacle_x_1.rect.y = random.randint(100, 600)
	obstacle_x_2 = ObstacleX()
	obstacle_x_2.rect.x = random.randint(20, 600)
	obstacle_x_2.rect.y = random.randint(100, 600)
	obstacle_x_3 = ObstacleX()
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

		if player.rect.x in range(destination.rect.x - 10, destination.rect.x + 10):
			if player.rect.y in range(destination.rect.y - 10, destination.rect.y + 10):
				you_win_screen_interface(world, cnfg.SCREENSIZE)

		if player.rect.x in range(obstacle_x_1.rect.x - 10, obstacle_x_1.rect.x + 10):
			if player.rect.y in range(obstacle_x_1.rect.y - 10, obstacle_x_1.rect.y + 10):
				game_over_screen_interface(world, cnfg.SCREENSIZE)

		if player.rect.x in range(obstacle_x_2.rect.x - 10, obstacle_x_2.rect.x + 10):
			if player.rect.y in range(obstacle_x_2.rect.y - 10, obstacle_x_2.rect.y + 10):
				game_over_screen_interface(world, cnfg.SCREENSIZE)

		if player.rect.x in range(obstacle_x_3.rect.x - 10, obstacle_x_3.rect.x + 10):
			if player.rect.y in range(obstacle_x_3.rect.y - 10, obstacle_x_3.rect.y + 10):
				game_over_screen_interface(world, cnfg.SCREENSIZE)

		if player.rect.x in range(obstacle_y_1.rect.x - 10, obstacle_y_1.rect.x + 10):
			if player.rect.y in range(obstacle_y_1.rect.y - 10, obstacle_y_1.rect.y + 10):
				game_over_screen_interface(world, cnfg.SCREENSIZE)

		if player.rect.x in range(obstacle_y_2.rect.x - 10, obstacle_y_2.rect.x + 10):
			if player.rect.y in range(obstacle_y_2.rect.y - 10, obstacle_y_2.rect.y + 10):
				game_over_screen_interface(world, cnfg.SCREENSIZE)

		if player.rect.x in range(obstacle_y_3.rect.x - 10, obstacle_y_3.rect.x + 10):
			if player.rect.y in range(obstacle_y_3.rect.y - 10, obstacle_y_3.rect.y + 10):
				game_over_screen_interface(world, cnfg.SCREENSIZE)

		world.fill(cnfg.BACKGROUND_BLACK)

		player.update()

		player_list.draw(world)
		obstacle_list.draw(world)
		destination_list.draw(world)

		obstacle_x_1.movement()
		obstacle_x_1.movement()
		obstacle_x_2.movement()
		obstacle_y_2.movement()
		obstacle_y_3.movement()
		obstacle_y_3.movement()

		pygame.display.update()
		clock.tick(cnfg.FRAME_RATE)


def game_over_screen_interface(world, screen_size):
	world.fill(cnfg.BACKGROUND_START_SCREEN)
	title_font = pygame.font.Font(cnfg.TITLE_FONT_PATH, screen_size[0] // 10)
	content_font = pygame.font.Font(cnfg.CONTENT_FONT_PATH, screen_size[0] // 20)
	end_title = title_font.render('Game Over', True, cnfg.TITLE_FONT_COLOR)
	re_spawn = content_font.render('press "s" to play again', True, (20, 20, 20))
	quit_instruction = content_font.render('press "q" to quit', True, (20, 20, 20))
	title_rect = end_title.get_rect()
	title_rect.midtop = (screen_size[0] // 2, screen_size[1] // 3)
	content_rect = re_spawn.get_rect()
	content_rect.midtop = (screen_size[0] // 2, screen_size[1] - 120)
	instruction_rect = quit_instruction.get_rect()
	instruction_rect.midtop = (screen_size[0] // 2, screen_size[1] - 80)
	world.blit(end_title, title_rect)
	world.blit(re_spawn, content_rect)
	world.blit(quit_instruction, instruction_rect)
	while True:
		key = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif key[pygame.K_s]:
				game_loop(world)
			elif key[pygame.K_q]:
				pygame.quit()
				sys.exit()
		pygame.display.update()


def you_win_screen_interface(world, screen_size):
	world.fill(cnfg.BACKGROUND_START_SCREEN)
	title_font = pygame.font.Font(cnfg.TITLE_FONT_PATH, screen_size[0] // 10)
	content_font = pygame.font.Font(cnfg.CONTENT_FONT_PATH, screen_size[0] // 20)
	end_title = title_font.render('You win', True, cnfg.TITLE_FONT_COLOR)
	re_spawn = content_font.render('press "s" to play again', True, (20, 20, 20))
	quit_instruction = content_font.render('press "q" to quit', True, (20, 20, 20))
	title_rect = end_title.get_rect()
	title_rect.midtop = (screen_size[0] // 2, screen_size[1] // 3)
	content_rect = re_spawn.get_rect()
	content_rect.midtop = (screen_size[0] // 2, screen_size[1] - 120)
	instruction_rect = quit_instruction.get_rect()
	instruction_rect.midtop = (screen_size[0] // 2, screen_size[1] - 80)
	world.blit(end_title, title_rect)
	world.blit(re_spawn, content_rect)
	world.blit(quit_instruction, instruction_rect)
	while True:
		key = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif key[pygame.K_s]:
				game_loop(world)
			elif key[pygame.K_q]:
				pygame.quit()
				sys.exit()
		pygame.display.update()
