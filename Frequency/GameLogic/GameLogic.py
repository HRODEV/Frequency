from GameLogic.Player import Player


class GameLogic():

    def __init__(self, players=None, playingPlayer=None):
        if players is None:
            self.Players = []
        else:
            self.Players = players
        self.PlayingPlayer = playingPlayer if playingPlayer is not None else []


    def Update(self, game):
        return GameLogic(self.Players, self.PlayingPlayer)


    def AddNewPlayer(self, Name):
        if not self.Players:
            characterIndex = 0
            player = Player(Name, characterIndex, 0, 4)
            self.PlayingPlayer = player
            self.Players.append(player)
        else:
            characterIndex = self.Players[-1].Character +1
            self.Players.append(Player(Name, characterIndex, 0, 0))

    def EndTurn(self, game):
        self.PlayingPlayer.Moves = 0
        newPlayingPlayer = self.Players[(self.PlayingPlayer.Character + 1) % game.Settings.GetTotalPlayers()]
        newPlayingPlayer.Moves = 4
        self.PlayingPlayer = newPlayingPlayer

    def CanAddUnitBuildingToTile(self, game):
          if self.PlayingPlayer.Moves != 0:
            self.PlayingPlayer.Moves -= 1
            return True


