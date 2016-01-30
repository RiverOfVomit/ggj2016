import random

player_names = ['Josefus','Manu','Sheb']

class Players(object):

    def __init__(self):
    	print "Creating Players bucket"
        self.players = {}

    def add_new_player(self,sid):
        self.players[sid] = Player(sid)
        return self.players[sid]

class Player(object):

    def __init__(self, sid):
    	print "Creating new Player"
        self.sid = sid
        self.name = random.choice(player_names) + ' ' +  str(random.randint(1, 100))
