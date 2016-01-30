"""Tiles"""

class Tile(object):
	def __init__(self, coordinate):
		self.states = ["open", "reserved", "solved"]
		self.id = coordinate
		self.state = "open"
		self.player = ""

	def change_state(self, state):
		if state in self.states:
			self.state = state
		else:
			print "wrong state given"

	def set_player(self, player_name):
		self.player = player_name
