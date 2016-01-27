from Board.Map.SeaTile import SeaTile
from GameLogic.Player import Player


class GameLogic:

    def __init__(self, players, playingPlayer=None):
        self.Players = players
        self.PlayingPlayer = playingPlayer if playingPlayer is not None else self.Players[0]

    def GetTotalPlayers(self):
        return len(self.Players)

    def Update(self, game):
        return GameLogic(self.Players, self.PlayingPlayer)

    def AddNewPlayer(self, Name):
        if not self.Players:
            characterIndex = 0
            player = Player(Name, characterIndex)
            self.PlayingPlayer = player
            self.Players.append(player)
        else:
            characterIndex = self.Players[-1].Character + 1
            self.Players.append(Player(Name, characterIndex, 0, 0))

    def EndTurn(self, game):
        self.PlayingPlayer.Moves = 0
        newPlayingPlayer = self.Players[(self.PlayingPlayer.Character.Id + 1) % self.GetTotalPlayers()]
        newPlayingPlayer.Moves = 4
        self.PlayingPlayer = newPlayingPlayer

    def CanAddUnitBuildingToTile(self, game, tile):
        # TODO rest of implementation
        if type(tile) is not SeaTile:
            if self.PlayingPlayer.Moves != 0:
                self.PlayingPlayer.Moves -= 1
                return True
        return False


