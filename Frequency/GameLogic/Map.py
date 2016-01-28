import GameLogic.Unit
from GameLogic.Barrack import BaseBarrack
from Vector2 import Vector2


class Tile:
    def __init__(self, _position: Vector2, _basicMoney: int, _enemyMoney: int):
        self._position = _position
        self._basicMoney = _basicMoney
        self._enemyMoney = _enemyMoney
        self._building = None
        self._unit = None

    @property
    def Building(self): # TODO make buildings
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
        if self._unit is None:
            self._unit = value
        else:
            raise Exception("there is already a unit on the tile")

    @property
    def Position(self) -> Vector2:
        return self._position

    @property
    def BasicMoney(self) -> int:
        return self._basicMoney

    @property
    def EnemyMoney(self) -> int:
        return self._enemyMoney


class DesertTile(Tile):

    def __init__(self, _position):
        super().__init__(_position, 50, 100)


class ForestTile(Tile):

    def __init__(self, _position):
        super().__init__(_position, 50, 100)


class GoldTile(Tile):

    def __init__(self, _position):
        super().__init__(_position, 150, 150)


class IceTile(Tile):

    def __init__(self, _position):
        super().__init__(_position, 50, 100)


class SeaTile(Tile):

    def __init__(self, _position):
        super().__init__(_position, 50, 100)


class SwampTile(Tile):

    def __init__(self, _position):
        super().__init__(_position, 50, 100)


class Map:

    def DetermineTileType(self, X, Y, logic: GameLogic):
        if X < 7 and Y < 7:
            tile = ForestTile(Vector2(X, Y))
        elif 10 < X < 18 and Y < 7:
            tile = IceTile(Vector2(X, Y))
        elif X < 7 and 10 < Y < 18:
            tile = DesertTile(Vector2(X, Y))
        elif 10 < X < 18 and Y > 10:
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
    

