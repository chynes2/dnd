# https://www.youtube.com/watch?v=3zV2ewk-IGU
# http://kidscancode.org/lessons/

import pygame as pg
import os
from settings import *
from sprites.player import Player
from sprites.wall import Wall
from sprites.map import Map, Camera

class Game():
	def __init__(self):
		self.running = True
		self.game_display = pg.display.set_mode((screen_width, screen_height))
		self.game_clock = pg.time.Clock()
		
		pg.init()
		pg.mixer.init()
		pg.display.set_caption(game_title)
		
	def new(self):
		self.all_sprites = pg.sprite.Group()
		self.walls = pg.sprite.Group()
		self.load_environment()
		self.camera = Camera(self.map.width, self.map.height)

	def load_environment(self):
		self.map = Map(self, 'magic_yale/01.txt')
		
	def run(self):
		self.playing = True
		while self.playing:
			self.game_clock.tick(fps)
			self.events()
			self.update()
			self.draw()

	def update(self):
		self.all_sprites.update()
		self.camera.update(self.p1)
		#print('ALL-SPRITES---->', [s for s in self.all_sprites if s not in self.walls])

	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.running = False
			print(event)

	def draw(self):
		self.game_display.fill(WHITE)
		self.draw_grid()
		for sprite in self.all_sprites:
			self.game_display.blit(sprite.image, self.camera.apply(sprite))
		pg.display.flip()


	def show_start_screen(self):
		pass

	def show_game_over(self):
		pass

	def draw_grid(self):
		for x in range(0, screen_width, tile_size):
			pg.draw.line(self.game_display, BLACK, (x, 0), (x, screen_height))
		for y in range(0, screen_height, tile_size):
			pg.draw.line(self.game_display, BLACK, (0, y), (screen_width, y))

game = Game()
game.show_start_screen()
while game.running:
	game.new()
	game.run()
	game.show_game_over()

pg.quit()