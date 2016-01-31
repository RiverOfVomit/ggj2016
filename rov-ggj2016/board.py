"""Board"""
from tiles import *

class Board(object):

	def __init__(self, tile_number):
		self.tile_number = tile_number
		self.tiles = {}
		self.initalize_tiles(self.tile_number)

	def initalize_tiles(self, tile_number):
		for x in range(1, tile_number+1):
			self.tiles[x] = Tile(x)

	def update_tiles(self):
		pass

	def request_tile(self, number, player):
		number = int(number)
		if number in self.tiles:
			return self.tiles[number].request(player)
		else:
			return False

	def get_unsolved_tiles_count(self):
		unsolved_tiles = 0
		print "Tiles type", type(self.tiles)
		for tile in self.tiles:
			if not self.tiles[tile].is_resolved():
				unsolved_tiles += 1
		print "unsolved Tiles:", unsolved_tiles
		return unsolved_tiles


	def get_tile(self,id):
		return self.tiles[id]
