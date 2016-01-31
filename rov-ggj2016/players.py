import random

BD_PLAYER_NAMES = ['Josefus','Manu','Sheb']

class Players(object):

    def __init__(self):
        self.player = {}
        print "Creating Players bucket. Initial length:", len(self.player)

    def add_new_player(self,sid,player_type):
        self.player[sid] = Player(sid,player_type)
        return self.player[sid]

    def return_player_with_highest_score(self):
        pass

class Player(object):

    def __init__(self, sid, player_type):
    	print "Creating new Player"
        self.sid = sid
        self.name = random.choice(BD_PLAYER_NAMES) + str(random.randint(1, 100))
        self.type = player_type
        self.tileid = None
        self.score = 0

    def add_score(self, score):
        self.score += score
        print "SCORE ADDED:", self.name, "HAS NOW", self.score, "POINTS"


# TESTING

# players = Players()
# print players.player

# players.add_new_player("sid_00", "null")
# players.add_new_player("sid_01", "eins")
# players.add_new_player("sid_02", "zwei")
# print players.player

# for player in players.player:
#     print players.player[player].score