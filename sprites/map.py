import pygame as pg
import os
from settings import *
from sprites.wall import Wall
from sprites.player import Player
from sprites.npc import NPC

class Map():
	def __init__(self, game, map_name):
		self.game = game
		self.npcs = set()
		
		game_folder = os.path.dirname('..')
		image_folder = os.path.join(game_folder, 'images', 'maps')
		with open(os.path.join(image_folder, map_name)) as f:
			map = f.readlines()
		for y, tiles in enumerate(map):
			for x, tile in enumerate(tiles):
				if tile == '1':
					Wall(game, x, y)
				elif tile == 'P':
					self.game.p1 = Player(self.game, x*tile_size, y*tile_size)
					self.game.p1.rect.x += (tile_size - self.game.p1.rect.width) / 2
				elif tile == 'N':
					self.npcs.add(NPC(self.game, x*tile_size, y*tile_size))

		self.tilewidth = len(map[0].strip())
		self.tileheight = len(map)
		self.width = self.tilewidth * tile_size
		self.height = self.tileheight * tile_size

class Camera():
	def __init__(self, width, height):
		self.camera = pg.Rect(0, 0, width, height)
		self.width = width
		self.height = height

	def apply(self, entity):
		return entity.rect.move(self.camera.topleft)

	def update(self, target):
		x = -target.rect.x + screen_width // 2
		y = -target.rect.y + screen_height // 2

		x = min(0, x)
		y = min(0, y)
		x = max(x, -(self.width - screen_width))
		y = max(y, -(self.height - screen_height))

		# print('MAP', self.width, self.height)
		# print('CAMERA', self.camera.bottom)

		self.camera = pg.Rect(x, y, self.width, self.height)