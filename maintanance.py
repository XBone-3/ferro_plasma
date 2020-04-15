import cnfg
import random
import pygame


class PlayerInstancing:
	def __init__(self):
		self.direction = 0
		self.image = pygame.image.load(cnfg.player_IMAGE_PATH)
		self.speed = [(self.direction + 1) * 3]

	def move_up(self):
		pass

	def move_down(self):
		pass

	def move_left(self):
		pass

	def move_right(self):
		pass


class ObstaclesInstancing:
	def __init__(self):
		pass

	def obstacle_y(self, speed):
		pass

	def obstacle_x(self, speed):
		pass

	def obstacle_r(self, speed):
		pass

	def obstacle_p(self, speed):
		pass


class DestinationInstancing:
	def __init__(self):
		self.image = pygame.image.load(cnfg.DESTINATION_IMAGE_PATH)

	def destination_position(self):
		pass

	def destination_movement(self):
		pass
