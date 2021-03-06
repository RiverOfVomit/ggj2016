"""GameController"""

from board import Board
from players import *
from collections import deque

BD_TILE_NUMBER = 9
BD_OPEN_PLAYERS = [1,2,3]

class GameController():

    def __init__(self):
        print "(Re)Starting GameController"
        self.player_slots = deque(BD_OPEN_PLAYERS)
        self.players = Players()
        self.board = Board(BD_TILE_NUMBER)

    def reset_game_state(self):
        self.__init__()

    def request_tile(self, number, sid):
        self.board.sanitycheck_players(self.players)
        player = self.get_player(sid)
        print "Tile", number ,"requested by", player.name
        tile = self.board.request_tile(number, player)
        #success = self.board.tile[number].request(self.get_player(sid))
        if tile:
            player.tileid = tile.id
            print "Tile succesfully reserved", tile.id, player.tileid
        else:
            print "Tile could not be reserved"
        return tile

    def choose_tile(self, something):
        print str(something), "I am the GameController"

    def check_board_size(self):
        pass

    def remove_player(self,sid):
        #print "player len before pop", len(self.players.player)
        if (sid in self.players.player):
            removed_player = self.players.player.pop(sid, None)
            self.player_slots.append(removed_player.type) # open up player slot
            self.board.sanitycheck_players(self.players)
            print removed_player.name, 'left the game'
        #print "player len after pop", len(self.players.player)

    def resolve_tile(self,sid):
        player = self.get_player(sid)
        self.board.sanitycheck_players(self.players)
        if player.tileid:
            print "Tile", player.tileid ,"resolved by", player.name
            tile = self.board.get_tile(player.tileid)
            self.players.player[sid].add_score(1)
            tile.resolve(player)
            return tile
        else:
            print "Player", player.name, "has no tileid to resolve!"
            return False

    def add_player(self,sid):
        self.board.sanitycheck_players(self.players)
        if (sid not in self.players.player) and (len(self.player_slots) > 0):
            player_type = self.player_slots.popleft()
            new_player = self.players.add_new_player(sid, player_type)
            print "New Player created: ", new_player.name, new_player.type
            return new_player
        else:
            print "NO new player was created", len(self.player_slots)
            return False

    def check_if_game_won(self):
        self.board.sanitycheck_players(self.players)
        unsolved_tiles = self.board.get_unsolved_tiles_count()
        if unsolved_tiles == 0:
            # get player with highest score
            return True

    def rp(self):
        print "here delete now!"

    def get_player(self,sid):
        return self.players.player[sid]
