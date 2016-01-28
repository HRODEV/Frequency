from functools import reduce

from GameLogic import Player
from GameLogic.Map import Tile


class Unit:

    def __init__(self, tile: Tile, owner: Player):
        self._tile = tile
        self._owner = owner

    @property
    def Tile(self) -> Tile: return self._tile
    @property
    def Owner(self) -> Player: return self._owner
    @property
    def AttackPoints(self) -> int: return 0
    @property
    def DefencePoints(self) -> int: return 0


class Soldier(Unit):

    @property
    def AttackPoints(self): return 1
    @property
    def DefencePoints(self): return 1


class Robot(Unit):

    @property
    def AttackPoints(self): return 2
    @property
    def DefencePoints(self): return 2


class Tank(Unit):

    @property
    def AttackPoints(self): return 3
    @property
    def DefencePoints(self): return 3


class UnitGroup(Unit):
    """ a group of max 4 units
    """

    _units = []

    def AddUnit(self, unit: Unit):
        if type(unit) is UnitGroup:
            raise Exception("A UnitGroup can only hold normal units, not UnitGroups")
        elif len(self._units) > 2:
            raise Exception("A unitGroup can not hold more than 4 units")
        else:
            self._units.append(unit)

    def RemoveUnit(self, unit: Unit):
        self._units = [_unit for _unit in self._units if _unit != unit]

    @property
    def Units(self):
        """
        :return: it returns a copy
        """
        return self._units.copy()

    @property
    def AttackPoints(self):
        return reduce((lambda aPoints, unit: aPoints + unit.AttackPoints), self._units)

    @property
    def DefencePoints(self):
        return reduce((lambda aPoints, unit: aPoints + unit.DefencePoints), self._units)
