import pygame as pg
from sprites.textbox import TextBox
import os
from settings import BLACK, WHITE, screen_width, screen_height

class NPC(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.speed = 10
		self.load_image()
		self.rect.x = x
		self.rect.y = y
		self.detection_radius = 50
		self.passable = False
		self.triggered = False

	def load_image(self):
		img_name = 'npc_1.png'
		game_folder = os.path.dirname('..')
		image_folder = os.path.join(game_folder, 'images')
		self.image = pg.image.load(os.path.join(image_folder, img_name)).convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

	def update(self):
		## check for player
		inflated = self.rect.inflate(self.detection_radius*2, self.detection_radius*2)
		if inflated.colliderect(self.game.p1.rect):
			if not self.triggered:
				self.triggered = True
				message = 'Have you heard about my amazing girlfriend Disha?!'
				TextBox(self.game, self.rect.topright[0], self.rect.topright[1], self, message)