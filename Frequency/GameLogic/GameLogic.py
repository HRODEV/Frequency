from GameLogic import UnitFactory
from GameLogic.Player import Player


class GameLogic:

    def __init__(self, players, _turn=0):
        self.Players = players
        self._turn = _turn
        from GameLogic.Map import Map
        self._map = Map(self)

    @property
    def Map(self) -> 'Map':
        return self._map

    @property
    def Turns(self) -> int:
        return self._turn

    @property
    def Round(self) -> int:
        return self._turn / self.TotalPlayers

    @property
    def TotalPlayers(self) -> int:
        return len(self.Players)

    @property
    def PlayingPlayer(self) -> Player:
        return self.Players[self._turn % self.TotalPlayers]

    _gamestarted = False
    def StartGame(self):
        if self._gamestarted:
            raise Exception("game already started")
        else:
            self._gamestarted = True
            self.PlayingPlayer.Moves = 4

    def AddNewPlayer(self, Name) -> Player:
        if not self._gamestarted:
            characterIndex = self.Players[-1].Character + 1
            player = Player(Name, characterIndex, 0, 0)
            self.Players.append(player)
            return player
        else:
            raise Exception("game already started")

    def EndTurn(self, game):
        self.PlayingPlayer.Moves = 0
        self._turn += 1
        self.PlayingPlayer.Moves = 4
        self.PlayingPlayer.Money += self.GetIncome()

    def CanAddUnitToTile(self, game, tile):
        # TODO rest of implementation
        from GameLogic.Map import SeaTile
        if type(tile) is not SeaTile:
            if self.PlayingPlayer.Moves != 0 and self.PlayingPlayer.Money >= 100:
                self.PlayingPlayer.Moves -= 1
                return True
        return False

    def GetIncome(self, player: Player=None):
        player = player if player is not None else self.PlayingPlayer

        tilesWithUnit = list(set([unit.Tile for unit in player.Units]))

        return sum([tile.GetMoney(player) for tile in tilesWithUnit])

    def BuyUnit(self, unitType, tile):
        if self.PlayingPlayer.Moves > 0:
            unit = UnitFactory.BuyUnit(self, unitType, tile, self.PlayingPlayer)

            if unit is not None:
                self.PlayingPlayer.Moves -= 1

            return unit
