from GameLogic.Player import Player


class GameLogic:

    def __init__(self, players=None):
        if players is None:
            self.Players = []
        else:
            self.Players = players


    def addNewPlayer(self, Name):
        if not self.Players:
            characterIndex = 0
        else:
            characterIndex = self.Players[-1].Character +1

        self.Players.append(Player(Name, characterIndex, 0))