import random

BD_PLAYER_NAMES = ['Josefus','Manu','Sheb']

class Players(object):

    def __init__(self):
        self.player = {}
        print "Creating Players bucket. Initial length:", len(self.player)

    def add_new_player(self,sid,player_type):
        self.player[sid] = Player(sid,player_type)
        return self.player[sid]

class Player(object):

    def __init__(self, sid, player_type):
    	print "Creating new Player"
        self.sid = sid
        self.name = random.choice(BD_PLAYER_NAMES) + str(random.randint(1, 100))
        self.type = player_type
        self.tileid = None
