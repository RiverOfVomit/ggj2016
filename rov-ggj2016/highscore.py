"""HighScore"""

class HighScore():
    def __init__(self):
        self.name = "Highscore class"
        self.score = {}


    def add_player(self, player_name):
        self.score[player_name] = 0


    def update_score(self, player_name, points):
        self.score[player_name] += points


    def delete_player(self, player_name):
        del self.score[player_name]


    def reset_highscore(self):
        self.score = {}

### TESTING
# high = HighScore()

# high.add_player("Sheb")
# high.add_player("Manu")
# high.add_player("Josef")

# high.update_score("Manu", 1)
# high.update_score("Manu", 1)
# high.update_score("Sheb", 1)
# print high.score

# high.delete_player("Sheb")
# print high.score

# high.reset_highscore()
# print high.score