"""GameController"""

from board import Board
from players import *

class GameController():

	def __init__(self):
		print "Starting GameController"

		################
		## INIT BOARD ##
		################
		self.players = Players()
		self.board = Board()
		print "GAMECONTROLLER: Board detected with following config:", self.board.config

	def request_tile(self, data, sid):
		print "Tile requested (GameController)", sid

	def choose_tile(self, something):
		print str(something), "I am the GameController"

	def check_board_size(self):
		pass

	def add_player(self,sid):
		new_player = self.players.add_new_player(sid)
		print "New Player created: ", new_player.name
