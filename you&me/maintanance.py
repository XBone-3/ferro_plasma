import cnfg
import pygame
import sys
import level_zero


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
			game_over_screen_interface(pygame.display.set_mode(cnfg.SCREENSIZE), cnfg.SCREENSIZE)

	def move_down(self):
		if 0 <= self.rect.y <= 600:
			# self.move_y += 1
			self.rect.y = self.rect.y + 5
		else:
			game_over_screen_interface(pygame.display.set_mode(cnfg.SCREENSIZE), cnfg.SCREENSIZE)

	def move_left(self):
		if 0 <= self.rect.x <= 600:
			# self.move_x -= 1
			self.rect.x = self.rect.x - 5
		else:
			game_over_screen_interface(pygame.display.set_mode(cnfg.SCREENSIZE), cnfg.SCREENSIZE)

	def move_right(self):
		if 0 <= self.rect.x <= 600:
			# self.move_x += 1
			self.rect.x = self.rect.x + 5
		else:
			game_over_screen_interface(pygame.display.set_mode(cnfg.SCREENSIZE), cnfg.SCREENSIZE)


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

	def movement(self, speed):
		if 0 < self.rect.x <= 640:
			self.rect.x = self.rect.x - speed
		elif self.rect.x <= 0:
			self.rect.x = self.rect.x + speed
			while self.rect.x < 640:
				self.rect.x = self.rect.x + speed
			self.rect.x = self.rect.x - speed


class ObstacleY(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.obstacle_y_path = cnfg.OBSTACLE_IMAGE_Y_PATH
		self.image = pygame.image.load(self.obstacle_y_path)
		self.rect = self.image.get_rect()

	def movement(self, speed):
		if 0 < self.rect.y < 640:
			self.rect.y = self.rect.y - speed
		elif self.rect.y < 0:
			self.rect.y = self.rect.y + speed
			while self.rect.y < 640:
				self.rect.y = self.rect.y + speed
			self.rect.y = self.rect.y - speed


class ObstacleP(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.obstacle_p_path = cnfg.OBSTACLE_IMAGE_P_PATH
		self.image = pygame.image.load(self.obstacle_p_path)
		self.rect = self.image.get_rect()

	def movement(self, speed):
		pass


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


def game_over_screen_interface(world, screen_size):
	world.fill(cnfg.BACKGROUND_START_SCREEN)
	title_font = pygame.font.Font(cnfg.TITLE_FONT_PATH, screen_size[0] // 10)
	content_font = pygame.font.Font(cnfg.CONTENT_FONT_PATH, screen_size[0] // 20)
	end_title = title_font.render('Game Over', True, cnfg.TITLE_FONT_COLOR)
	re_spawn = content_font.render('press "s" to start again', True, (20, 20, 20))
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
				level_zero.main_game_loop(world)
			elif key[pygame.K_q]:
				pygame.quit()
				sys.exit()
		pygame.display.update()


def you_win_screen_interface(world, screen_size):
	world.fill(cnfg.BACKGROUND_START_SCREEN)
	title_font = pygame.font.Font(cnfg.TITLE_FONT_PATH, screen_size[0] // 10)
	content_font = pygame.font.Font(cnfg.CONTENT_FONT_PATH, screen_size[0] // 20)
	end_title = title_font.render('You win', True, cnfg.TITLE_FONT_COLOR)
	re_spawn = content_font.render('press "s" to play next level', True, (20, 20, 20))
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
				level_zero.main_game_loop(world)
			elif key[pygame.K_n]:
				pass
			elif key[pygame.K_q]:
				pygame.quit()
				sys.exit()
		pygame.display.update()
