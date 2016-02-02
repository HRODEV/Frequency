import GameLogic.Unit
from GameLogic.Barrack import BaseBarrack
from GameLogic.Character import *


class Tile:
    def __init__(self, _position: Vector2, _basicMoney: int, _enemyMoney: int):
        self._position = _position
        self._basicMoney = _basicMoney
        self._enemyMoney = _enemyMoney
        self._building = None
        self._unit = None

    @property
    def Building(self):
        return self._building

    @Building.setter
    def Building(self, value):
        if self._building is not None:
            raise Exception("there is already a building on this Tile")
        self._building = value

    @property
    def Unit(self) -> GameLogic.Unit.Unit:
        return self._unit

    @Unit.setter
    def Unit(self, value: GameLogic.Unit.Unit):
        self._unit = value

    @property
    def Position(self) -> Vector2:
        return self._position

    @property
    def BasicMoney(self) -> int:
        return self._basicMoney

    @property
    def EnemyMoney(self) -> int:
        return self._enemyMoney

    def GetMoney(self, player):
        return 0


class DesertTile(Tile):

    def __init__(self, _position):
        super().__init__(_position, 50, 100)

    def GetMoney(self, player):
        if type(player.Character) is DesertCharacter:
            return self.BasicMoney
        else:
            return self.EnemyMoney


class ForestTile(Tile):

    def __init__(self, _position):
        super().__init__(_position, 50, 100)

    def GetMoney(self, player):
        if type(player.Character) is ForestCharacter:
            return self.BasicMoney
        else:
            return self.EnemyMoney


class GoldTile(Tile):

    def __init__(self, _position):
        super().__init__(_position, 150, 150)

    def GetMoney(self, player):
        return 150


class IceTile(Tile):

    def __init__(self, _position):
        super().__init__(_position, 50, 100)

    def GetMoney(self, player):
        if type(player.Character) is IceCharacter:
            return self.BasicMoney
        else:
            return self.EnemyMoney


class SeaTile(Tile):

    def __init__(self, _position):
        super().__init__(_position, 0, 0)


class SwampTile(Tile):

    def __init__(self, _position):
        super().__init__(_position, 50, 100)

    def GetMoney(self, player):
        if type(player.Character) is SwampCharacter:
            return self.BasicMoney
        else:
            return self.EnemyMoney


class Map:

    def DetermineTileType(self, X, Y, logic: GameLogic):
        if X < 7 and Y < 7 and X+Y < 10:
            tile = ForestTile(Vector2(X, Y))
        elif Y < 7 and 18 > X > 10 > (17-X) + Y:
            tile = IceTile(Vector2(X, Y))
        elif X < 7 and 18 > Y > 10 > X + (17 - Y):
            tile = DesertTile(Vector2(X, Y))
        elif 10 < X < 18 and Y > 10 > (17 - Y) + (17 - X):
            tile = SwampTile(Vector2(X, Y))
        elif 6 < X < 11 and 6 < Y < 11:
            tile = GoldTile(Vector2(X, Y))
        else:
            tile = SeaTile(Vector2(X, Y))

        if X % 17 == 0 and Y % 17 == 0:
            # (x + y) in (0, 1, 2, 3)
            x = 0 if X == 0 else 1
            y = 0 if Y == 0 else 2
            if logic.TotalPlayers > x + y:
                player = logic.Players[x + y]
                tile.Building = BaseBarrack(tile, player)
        return tile

    def __init__(self, logic):
        self._tiles = [
                [self.DetermineTileType(x, y, logic) for y in range(0, 18)]
                for x in range(0, 18)
            ]
        
    @property
    def TilesIterator(self):
        for row in self._tiles:
            for tile in row:
                yield tile
        
    def GetTile(self, position: Vector2) -> Tile:
        return self._tiles[position.X][position.Y]
    

