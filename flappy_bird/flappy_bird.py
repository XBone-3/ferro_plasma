import pygame
import random
import neat
import os

pygame.font.init()

bird_imgs = [pygame.transform.scale2x(pygame.image.load('imgs\\bird1.png')),
            pygame.transform.scale2x(pygame.image.load('imgs\\bird2.png')),
            pygame.transform.scale2x(pygame.image.load('imgs\\bird3.png'))]

pipe_img = pygame.transform.scale2x(pygame.image.load('imgs\\pipe.png'))

bg_img = pygame.transform.scale(pygame.image.load("imgs\\bg.png"), (600, 900))

base_img = pygame.transform.scale2x(pygame.image.load("imgs\\base.png"))

stat_font = pygame.font.SysFont('comicsans', 50)
GEN = 0

class Bird():
	IMGS = bird_imgs
	MAX_ROTATION = 25
	ROT_VEL = 20
	ANNIMATION_TIME = 5

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.img = self.IMGS[0]
		self.height = self.y
		self.tilt = 0
		self.img_count = 0
		self.tick_count = 0
		self.vel = 0

	def jump(self):
		self.vel = -10.5
		self.tick_count = 0
		self.height = self.y

	def move(self):
		self.tick_count += 1

		disp = self.vel * self.tick_count + 1.5 * self.tick_count ** 2

		if disp >= 16:
			disp = 16
		if disp < 0:
			disp -= 2
		self.y = self.y + disp
		if disp < 0 or self.y < self.height + 50:
			if self.tilt < self.MAX_ROTATION:
				self.tilt = self.MAX_ROTATION
		else:
			if self.tilt > -90:
				self.tilt -= self.ROT_VEL

	def draw(self, win):
		self.img_count += 1
		if self.img_count < self.ANNIMATION_TIME:
			self.img = self.IMGS[0]
		elif self.img_count < self.ANNIMATION_TIME * 2:
			self.img = self.IMGS[1]
		elif self.img_count < self.ANNIMATION_TIME * 3:
			self.img = self.IMGS[2]
		elif self.img_count < self.ANNIMATION_TIME * 4:
			self.img = self.IMGS[1]
		elif self.img_count < self.ANNIMATION_TIME * 4 + 1:
			self.img = self.IMGS[0]
			self.img_count = 0
		elif self.tilt <= -80:
			self.img = self.IMGS[1]
			self.img_count = self.ANNIMATION_TIME * 2
		rotated_image = pygame.transform.rotate(self.img, self.tilt)
		rotated_image_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, int(self.y))).center)
		win.blit(rotated_image, rotated_image_rect.topleft)

	def get_mask(self):
		return pygame.mask.from_surface(self.img)

class Pipe():
	GAP = 200
	VELOCITY = 5
	def __init__(self, x):
		self.x = x
		self.height = 0
		self.top = 0
		self.bottom = 0
		self.pipe_top = pygame.transform.flip(pipe_img, False, True)
		self.pipe_bottom = pipe_img
		self.passed = False
		self.set_height()

	def set_height(self):
		self.height = random.randint(45, 450)
		self.top = self.height - self.pipe_top.get_height()
		self.bottom = self.height + self.GAP

	def move(self):
		self.x -= self.VELOCITY

	def draw(self, win):
		win.blit(self.pipe_top, (self.x, self.top))
		win.blit(self.pipe_bottom, (self.x, self.bottom))

	def collide(self, bird):
		bird_mask = bird.get_mask()
		top_mask = pygame.mask.from_surface(self.pipe_top)
		bottom_mask = pygame.mask.from_surface(self.pipe_bottom)
		top_offset = (self.x - bird.x, self.top - round(bird.y))
		bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))
		t_point = bird_mask.overlap(top_mask, top_offset)
		b_point = bird_mask.overlap(bottom_mask, bottom_offset)
		if t_point or b_point:
			return True
		return False

class Base():
	VEL = 5
	WIDTH = base_img.get_width()
	IMG = base_img

	def __init__(self, y):
		self.y = y
		self.x1 = 0
		self.x2 = self.WIDTH

	def move(self):
		self.x1 -= self.VEL
		self.x2 -= self.VEL
		if self.x1 + self.WIDTH < 0:
			self.x1 = self.x2 + self.WIDTH
		if self.x2 + self.WIDTH < 0:
			self.x2 = self.x1 + self.WIDTH

	def draw(self, win):
		win.blit(self.IMG, (self.x1, self.y))
		win.blit(self.IMG, (self.x2, self.y))


def draw_window(win, birds, pipes, base, score, gen):
	win.blit(bg_img, (0,0))
	for pipe in pipes:
		pipe.draw(win)
	text = stat_font.render('score:' + str(score), 1, (225, 225, 225))
	win.blit(text, (600 - 10 - text.get_width(), 10))
	text = stat_font.render('gen:' + str(gen), 1, (225,225,225))
	win.blit(text, (10, 10))
	for bird in birds:
		bird.draw(win)
	base.draw(win)
	pygame.display.update()

def game_loop(genomes, config):
	global GEN
	nets = []
	ge = []
	birds = []
	GEN += 1
	for _, g in genomes:
		net = neat.nn.FeedForwardNetwork.create(g, config)
		nets.append(net)
		birds.append(Bird(175, 350))
		g.fitness = 0
		ge.append(g)
	pipes = [Pipe(600)]
	base = Base(730)
	score = 0
	win = pygame.display.set_mode((600, 800))
	pygame.display.set_caption('flappy bird AI')
	gameover = False
	clock = pygame.time.Clock()
	while not gameover:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				break
		pipe_ind = 0
		rem = []
		add_pipe = False
		if len(birds) > 0:
			if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].pipe_top.get_width():
				pipe_ind = 1
		else:
			gameover = True
			break
		for x, bird in enumerate(birds):
			ge[x].fitness += 0.1
			bird.move()
			output = nets[x].activate(
				(bird.y, abs(bird.y - pipes[pipe_ind].top), abs(bird.y - pipes[pipe_ind].bottom)))
			if output[0] > 0.5:
				bird.jump()
		for pipe in pipes:
			for x, bird in enumerate(birds):
				if pipe.collide(bird):
					ge[x].fitness -= 2
					birds.pop(x)
					nets.pop(x)
					ge.pop(x)
				if not pipe.passed and (pipe.x < bird.x):
					pipe.passed = True
					add_pipe = True
			if pipe.x + pipe.pipe_top.get_width() < 0:
				rem.append(pipe)
			pipe.move()
		if add_pipe:
			score += 1
			for g in ge:
				g.fitness += 5
			pipes.append(Pipe(600))
		for r in rem:
			pipes.remove(r)

		for x, bird in enumerate(birds):
			if bird.y + bird.img.get_height() > 730 or bird.y < 0:
				birds.pop(x)
				nets.pop(x)
				ge.pop(x)
		base.move()
		draw_window(win, birds, pipes, base, score, GEN)
def run(config_path):
	config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
	p = neat.Population(config)
	p.add_reporter(neat.StdOutReporter(True))
	stats = neat.StatisticsReporter()
	p.add_reporter(stats)
	winner = p.run(game_loop, 50)
if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-neat-feedforward.txt')
    run(config_path)