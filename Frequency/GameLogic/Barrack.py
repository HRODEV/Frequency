from GameLogic import Player


class Barrack:

    def __init__(self, tile, owner: Player):
        self._tile = tile
        self._owner = owner
        self._defencePoints = 6

    @property
    def Tile(self): return self._tile

    @property
    def Owner(self) -> Player: return self._owner

    @property
    def DefencePoints(self) -> int: return self._defencePoints

    @DefencePoints.setter
    def DefencePoints(self, value: int):
        self._defencePoints = value


class BaseBarrack(Barrack):

    def __init__(self, tile, owner: Player):
        super().__init__(tile, owner)
        self._defencePoints = 25
