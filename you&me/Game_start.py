import cnfg
import level_zero
import pygame
import sys


def start_screen_interface():
	pygame.init()
	world = pygame.display.set_mode(cnfg.SCREENSIZE)
	pygame.display.set_caption('Hard_game_ever 1.0')
	world.fill(cnfg.BACKGROUND_START_SCREEN)
	title_font = pygame.font.Font(cnfg.TITLE_FONT_PATH, cnfg.SCREENSIZE[0] // 10)
	content_font = pygame.font.Font(cnfg.CONTENT_FONT_PATH, cnfg.SCREENSIZE[0] // 20)
	title = title_font.render('You and Me', True, cnfg.TITLE_FONT_COLOR)
	content = content_font.render('my version', True, cnfg.CONTENT_FONT_COLOR)
	instruction = content_font.render('''press "s" to start''', True, (20, 20, 20))
	instruction_1 = content_font.render('''press "q" to quit once started''', True, (20, 20, 20))
	title_rect = title.get_rect()
	title_rect.midtop = (cnfg.SCREENSIZE[0] // 2, cnfg.SCREENSIZE[1] // 3)
	content_rect = content.get_rect()
	content_rect.midtop = (cnfg.SCREENSIZE[0] // 2, cnfg.SCREENSIZE[1] // 2)
	instruction_rect = instruction.get_rect()
	instruction_rect.midtop = (cnfg.SCREENSIZE[0] // 2, cnfg.SCREENSIZE[1] - 100)
	instruction_1_rect = instruction_1.get_rect()
	instruction_1_rect.midtop = (cnfg.SCREENSIZE[0] // 2, cnfg.SCREENSIZE[1] - 60)
	world.blit(title, title_rect)
	world.blit(content, content_rect)
	world.blit(instruction, instruction_rect)
	world.blit(instruction_1, instruction_1_rect)
	while True:
		key = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if key[pygame.K_s]:
				level_zero.main_game_loop(world)
		pygame.display.update()


if __name__ == '__main__':
	start_screen_interface()
