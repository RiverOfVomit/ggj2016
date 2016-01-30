"""GameController"""

from board import Board
from players import *
from pprint import pprint

BD_TILE_NUMBER = 9
BD_MAX_PLAYERS = 3

class GameController():

    def __init__(self):
        #print "Starting GameController"

        self.players = Players()
        self.board = Board(BD_TILE_NUMBER)

    def request_tile(self, number, sid):
        print "Tile", number ,"requested (GameController) by player", self.players.player[sid].name
        result = self.board.request_tile(number, self.get_player(sid))
        #success = self.board.tile[number].request(self.get_player(sid))
        if result:
            print "Tile succesfully reserved", result.id
        else:
            print "Tile could not be reserved"
        return result

    def choose_tile(self, something):
        print str(something), "I am the GameController"

    def check_board_size(self):
        pass

    def add_player(self,sid):
        if (sid not in self.players.player) and (BD_MAX_PLAYERS > len(self.players.player)):
            player_type = len(self.players.player) + 1
            new_player = self.players.add_new_player(sid, player_type)
            print "New Player created: ", new_player.name, new_player.type
        else:
            print "no new player was created"

    def get_player(self,sid):
        return self.players.player[sid]
