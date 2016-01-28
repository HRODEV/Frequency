import GameLogic.Unit
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
        if self._building is None:
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

    def DetermineTileType(self, X, Y):
        if X < 7 and Y < 7:
            return ForestTile(Vector2(X, Y))
        if 10 < X < 18 and Y < 7:
            return IceTile(Vector2(X, Y))
        if X < 7 and 10 < Y < 18:
            return DesertTile(Vector2(X, Y))
        if 10 < X < 18 and Y > 10:
            return SwampTile(Vector2(X, Y))
        if 6 < X < 11 and 6 < Y < 11:
            return GoldTile(Vector2(X, Y))
        else:
            return SeaTile(Vector2(X, Y))

    def __init__(self):
        self._tiles = [
                [self.DetermineTileType(x, y) for y in range(0, 18)] 
                for x in range(0, 18)
            ]
        
    @property
    def TilesIterator(self):
        for row in self._tiles:
            for tile in row:
                yield tile
        
    def GetTile(self, position: Vector2) -> Tile:
        return self._tiles[position.X][position.Y]
    

