import pygame as pg
from settings import *

class Wall(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.game = game
		self.groups = self.game.all_sprites, self.game.walls
		pg.sprite.Sprite.__init__(self, self.groups)
		self.width = tile_size
		self.height = tile_size
		self.image = pg.Surface((tile_size, tile_size))
		self.image.fill(BLACK)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x * tile_size
		self.rect.y = y * tile_size
		self.passable = False

	def update(self):
		pass