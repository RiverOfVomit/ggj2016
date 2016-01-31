"""Tiles"""

BD_TILE_STATE_OPEN = "open"
BD_TILE_STATE_RESERVED = "reserved"
BD_TILE_STATE_SOLVED = "solved"

class Tile(object):

    def __init__(self, number):
        self.id = number
        self.state = BD_TILE_STATE_OPEN
        self.playersid = None

    def request(self, player):
        if self.state != BD_TILE_STATE_OPEN:
            return False
        else:
            self.state = BD_TILE_STATE_RESERVED
            self.playersid = player.sid
            return self

    def resolve(self, player):
        if self.state == BD_TILE_STATE_RESERVED and self.playersid == player.sid:
            self.state = BD_TILE_STATE_SOLVED
            player.tileid = None
            return self
        else:
            return False;
