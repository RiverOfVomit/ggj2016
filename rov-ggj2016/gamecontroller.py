"""GameController"""

class GameController():
	def __init__(self):
		print "Starting GameController"

	def request_tile(self, sid):
		print "Tile requested (GameController)", sid

	def chose_tile(self, something):
		print str(something), "I am the GameController"