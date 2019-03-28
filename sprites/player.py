import pygame as pg
import os
from settings import BLACK, WHITE, screen_width, screen_height

class Player(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.speed = 10
		self.load_image()
		self.rect.x = x
		self.rect.y = y
		self.passable = True

	def load_image(self):
		img_name = 'wizard_small.png'
		game_folder = os.path.dirname('..')
		image_folder = os.path.join(game_folder, 'images')
		self.image = pg.image.load(os.path.join(image_folder, img_name)).convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

	def update(self):
		self.move()

	def move(self):
		self.speed_x, self.speed_y = 0, 0
		
		keystate = pg.key.get_pressed()
		if keystate[pg.K_LEFT]:
			self.speed_x += -self.speed
		if keystate[pg.K_RIGHT]:
			self.speed_x += self.speed
		if keystate[pg.K_UP]:
			self.speed_y += -self.speed
		if keystate[pg.K_DOWN]:
			self.speed_y += self.speed
		if self.speed_x != 0 and self.speed_y != 0:
			self.speed_x *= 0.7071
			self.speed_y *= 0.7071

		## move horizontal
		self.future_self = self.image.get_rect()
		self.future_self.x = self.rect.x + self.speed_x
		self.future_self.y = self.rect.y
		if self.future_self.right > self.game.map.width:
			self.speed_x = 0
		if self.future_self.left < 0:
			self.speed_x = 0
		for wall in self.game.walls:
			if not wall.passable:
				if self.future_self.colliderect(wall.rect):
					self.speed_x = 0
		for sprite in self.game.all_sprites:
			if not sprite.passable:
				if self.future_self.colliderect(sprite.rect):
					self.speed_x = 0

		## move vertical
		self.future_self = self.image.get_rect()
		self.future_self.x = self.rect.x
		self.future_self.y = self.rect.y + self.speed_y
		if self.future_self.bottom > self.game.map.height:
			self.speed_y = 0
		if self.future_self.top < 0:
			self.speed_y = 0
		for wall in self.game.walls:
			if not wall.passable:
				if self.future_self.colliderect(wall.rect):
					self.speed_y = 0
		for sprite in self.game.all_sprites:
			if not sprite.passable:
				if self.future_self.colliderect(sprite.rect):
					self.speed_y = 0

		self.rect.x += self.speed_x
		self.rect.y += self.speed_y
