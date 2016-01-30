import random

BD_PLAYER_NAMES = ['Josefus','Manu','Sheb']

class Players(object):

    def __init__(self):
    	print "Creating Players bucket"
        self.player = {}

    def add_new_player(self,sid):
        self.player[sid] = Player(sid)
        return self.player[sid]

class Player(object):

    def __init__(self, sid):
    	print "Creating new Player"
        self.sid = sid
        self.name = random.choice(BD_PLAYER_NAMES) + ' ' +  str(random.randint(1, 100))
