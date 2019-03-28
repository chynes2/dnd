import pygame as pg
import os
from settings import BLACK, WHITE, screen_width, screen_height

class NPC(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.speed = 0
		self.load_image()
		self.rect.x = x
		self.rect.y = y
		self.passable = False

	def load_image(self):
		img_name = 'npc_1.png'
		game_folder = os.path.dirname('..')
		image_folder = os.path.join(game_folder, 'images')
		self.image = pg.image.load(os.path.join(image_folder, img_name)).convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

	def update(self):
		pass
