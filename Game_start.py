import cnfg
import maintanance as man
import pygame
import sys


# def start_interface(screen, screen_size):
# 	screen.fill(cnfg.BACKGROUND)
# 	font = pygame.font.Font(cnfg.FONTPATH)
# 	title = font.render('Hard game ever', True, cnfg.FONT_COLOR)


def main():
	pygame.init()
	pygame.display.set_mode(cnfg.SCREENSIZE)
	pygame.display.set_caption('Hard_game_ever 1.0')
	# you = man.PlayerInstancing()
	while True:
		for event in pygame.event.get():
			if (event.type == pygame.QUIT) | (event.type == pygame.K_ESCAPE):
				pygame.quit()
				sys.exit()
		pygame.display.update()
