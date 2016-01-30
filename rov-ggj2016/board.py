"""Board"""
from tiles import *

class Board(object):
	def __init__(self):
		self.config = (3,5)
		self.tiles = {}

	def initalize_tiles(self, config):
		"""Creates all tiles and puts them into a dictionary"""
		print "x:", config[0], "y:", config[1]

		# Create tile objects according to config
		for x in range(config[0]):
			for y in range(config[1]):
				self.tiles[x,y] = Tile((x,y))
				# TEST
				print self.tiles[(x,y)].id

		print "BOARD:", len(self.tiles), "created"


	def update_tiles(self):
		pass



#TESTS
#tc = Board()
#tc.initalize_tiles(tc.config)
