from GameLogic import Player


class Barrack:

    def __init__(self, tile, owner: Player):
        self._tile = tile
        self._owner = owner

    @property
    def Tile(self): return self._tile
    @property
    def Owner(self) -> Player: return self._owner
    @property
    def DefencePoints(self) -> int: return 6


class BaseBarrack(Barrack):

    @property
    def DefencePoints(self) -> int: return 25
