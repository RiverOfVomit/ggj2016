"""GameController"""
from board import Board

class GameController():
	
	def __init__(self):
		print "Starting GameController"

		################
		## INIT BOARD ##
		################

		self.board = Board()
		print "GAMECONTROLLER: Board detected with following config:", self.board.config

	def request_tile(self, sid):
		print "Tile requested (GameController)", sid

	def choose_tile(self, something):
		print str(something), "I am the GameController"

	def check_board_size(self):
		pass
