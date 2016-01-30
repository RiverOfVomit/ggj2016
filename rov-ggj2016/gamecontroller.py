"""GameController"""

from board import Board
from players import *
from collections import deque

BD_TILE_NUMBER = 9
BD_OPEN_PLAYERS = deque([1,2,3])

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

    def remove_player(self,sid):
        #print "player len before pop", len(self.players.player)
        if (sid in self.players.player):
            removed_player = self.players.player.pop(sid, None)
            BD_OPEN_PLAYERS.append(removed_player.type) # open up player slot
            print removed_player.name, 'left the game'
        #print "player len after pop", len(self.players.player)

    def add_player(self,sid):
        if (sid not in self.players.player) and (len(BD_OPEN_PLAYERS) > 0):
            player_type = BD_OPEN_PLAYERS.popleft()
            new_player = self.players.add_new_player(sid, player_type)
            print "New Player created: ", new_player.name, new_player.type
            return new_player
        else:
            print "NO new player was created"
            return False

    def rp(self):
        print "here delete now!"

    def get_player(self,sid):
        return self.players.player[sid]
