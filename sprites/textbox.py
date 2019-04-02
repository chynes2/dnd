import pygame as pg
import os
from settings import BLACK, WHITE, screen_width, screen_height

class TextBox(pg.sprite.Sprite):
	def __init__(self, game, x, y, speaker, message):
		self.groups = game.all_sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.passable = True
		self.speaker = speaker
		self.message = message
		self.image = pg.font.Font(None, 24).render(message, True, BLACK)
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = self.speaker.rect.topright

	def update(self):
		keystate = pg.key.get_pressed()
		if keystate[pg.K_SPACE]:
			self.game.all_sprites.remove(self)