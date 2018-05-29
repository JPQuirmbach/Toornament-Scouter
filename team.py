class Team(object):

    def __init__(self, teamId, name, players):
        self.teamId = teamId
        self.name = name
        self.players = players

    def __str__(self):
        return "teamId: {0}, name: {1}, players: {2}".format(self.teamId, self.name, self.players)
