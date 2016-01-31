"""Board"""
from tiles import *

class Board(object):

	def __init__(self, tile_number):
		self.tile_number = tile_number
		self.tiles = {}
		self.initalize_tiles(self.tile_number)

	def initalize_tiles(self, tile_number):
		for x in range(0, tile_number):
			self.tiles[x] = Tile(x)

	def update_tiles(self):
		pass

	def request_tile(self, number, player):
		number = int(number)
		if number in self.tiles:
			return self.tiles[number].request(player)
		else:
			return False
			
	def get_tile(self,id):
		return self.tiles[id]
