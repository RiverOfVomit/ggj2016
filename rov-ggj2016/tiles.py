"""Tiles"""

BD_TILE_STATE_OPEN = "open"
BD_TILE_STATE_RESERVED = "reserved"
BD_TILE_STATE_SOLVED = "solved"

class Tile(object):
	def __init__(self, number):

		self.id = number
		self.state = BD_TILE_STATE_OPEN
		self.player = False

	def change_state(self, state):
		if state in self.states:
			self.state = state
		else:
			print "wrong state given"

	def request(self, player):
		if self.state != BD_TILE_STATE_OPEN:
			return False
		else:
			self.state = BD_TILE_STATE_RESERVED
			self.player = player
			return True
