"""Tiles"""

BD_TILE_STATE_OPEN = "open"
BD_TILE_STATE_RESERVED = "reserved"
BD_TILE_STATE_SOLVED = "solved"

class Tile(object):
	
    def __init__(self, number):
        self.id = number
        self.state = BD_TILE_STATE_OPEN
        self.player = False

    def request(self, player):
        if self.state != BD_TILE_STATE_OPEN:
            return False
        else:
            self.state = BD_TILE_STATE_RESERVED
            self.player = player
            return self
