"""GameController"""

from board import Board
from players import *

BD_TILE_NUMBER = 9

class GameController():

    def __init__(self):
        #print "Starting GameController"

        self.players = Players()
        self.board = Board(BD_TILE_NUMBER)

    def request_tile(self, number, sid):
        print "Tile", number ,"requested (GameController) by player", self.players.player[sid].name
        reserved = self.board.request_tile(number, self.get_player(sid))
        #success = self.board.tile[number].request(self.get_player(sid))
        if reserved:
            print "Tile succesfully reserved"
        else:
            print "Tile could not be reserved"
        return reserved

    def choose_tile(self, something):
        print str(something), "I am the GameController"

    def check_board_size(self):
        pass

    def add_player(self,sid):
        new_player = self.players.add_new_player(sid)
        print "New Player created: ", new_player.name

    def get_player(self,sid):
        return self.players.player[sid]
