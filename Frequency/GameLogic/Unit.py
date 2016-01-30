from functools import reduce

from GameLogic import MapHelpers
from GameLogic import Player
from GameLogic.GameLogic import GameLogic


class Unit:

    def __init__(self, tile, owner: Player, logic: GameLogic):
        self._tile = tile
        self._owner = owner
        self._logic = logic
        owner.AddUnit(self)

    @property
    def Tile(self): return self._tile
    @Tile.setter
    def Tile(self, value):
        self._tile = value
    @property
    def Owner(self) -> Player: return self._owner
    @property
    def AttackPoints(self) -> int: return 0
    @property
    def DefencePoints(self) -> int: return 0

    def MoveTo(self, tile: Tile):
        # check turn
        if not self.Owner.IsOnTurn:
            raise Exception("player is not on turn")
        # check if you move in the right area
        from GameLogic.Map import SeaTile
        if tile not in MapHelpers.getAroundingTiles(self.Tile, self._logic.Map):
            raise Exception("you are not aloud to move this unit more than one tile")
        elif tile.Unit is not None and tile.Unit.Owner != self.Owner:
            raise Exception("You need to fight to go to this tile")
        # check for actions with the sea
        elif type(tile) is SeaTile:
            # check if there is a boat available
            if tile.Unit is not None and type(tile.Unit) is Boat:
                # check if it is possible to place this unit in the boat
                boat = tile.Unit
                if boat.Unit is not None:
                    raise Exception("there is already a unit or group on the boat")
                else:
                    boat.Unit = self
                    self.Tile.Unit = None
                    self._tile = tile
        #no sea
        else:
            if tile.Unit is None:
                self.Tile.Unit = None
                tile.Unit = self
                self._tile = tile
            elif type(tile.Unit) is UnitGroup:
                unitGroup = tile.Unit
                if unitGroup.CountUnits < 4:
                    self.Tile.Unit = None
                    self._tile = tile
                    unitGroup.AddUnit(self)
                else:
                    raise Exception("this unit group is full")

        self._logic.PlayingPlayer.Moves -= 1


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
    def __init__(self, tile, owner: Player, logic: GameLogic):
        super().__init__(tile, owner, logic)
        self._units = []

    def AddUnit(self, unit: Unit):
        print(self)
        if type(unit) is UnitGroup or type(unit) is Boat:
            raise Exception("A UnitGroup can only hold normal units, not UnitGroups or boats")
        elif len(self._units) > 3:
            raise Exception("A unitGroup can not hold more than 4 units")
        else:
            self._units.append(unit)

    def RemoveUnit(self, unit: Unit):
        self._units = [_unit for _unit in self._units if _unit != unit]

    def MoveTo(self, tile: 'Tile'):
        # check turn
        if not self.Owner.IsOnTurn:
            raise Exception("player is not on turn")
        # check if you move in the right area
        from GameLogic.Map import SeaTile
        if tile not in MapHelpers.getAroundingTiles(self.Tile, self._logic.Map):
            raise Exception("you are not aloud to move this unit more than one tile")
        elif tile.Unit is not None and tile.Unit.Owner != self.Owner:
            raise Exception("You need to fight to go to this tile")
        # check for actions with the sea
        elif type(tile) is SeaTile:
            # check if there is a boat available
            if tile.Unit is not None and type(tile.Unit) is Boat:
                # check if it is possible to place this unit in the boat
                boat = tile.Unit
                if boat.Unit is not None:
                    raise Exception("there is already a unit or group on the boat")
                else:
                    boat.Unit = self
                    self.Tile.Unit = None
                    self._tile = tile
                    for unit in self.Units:
                        unit._tile = tile
        #no sea
        else:
            if tile.Unit is None:
                self.Tile.Unit = None
                tile.Unit = self
                self._tile = tile
                for unit in self.Units:
                    unit._tile = tile
            elif type(tile.Unit) is UnitGroup:
                # TODO dealing with two UnitGroups
                raise NotImplemented()

        self._logic.PlayingPlayer.Moves -= 1


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

    @property
    def CountUnits(self):
        return len(self._units)

    @property
    def Tile(self):
        return self._tile

    @Tile.setter
    def Tile(self, value):
        self._tile = value
        for unit in self._units:
            unit.Tile = value


class Boat(Unit):

    def __init__(self, tile, owner, logic):
        self.Unit = None
        super().__init__(tile, owner, logic)

    @property
    def DefencePoints(self):
        return 6

    def MoveTo(self, tile: 'Tile'):
        # check turn
        if not self.Owner.IsOnTurn:
            raise Exception("player is not on turn")
        # check if you move in the right area
        from GameLogic.Map import SeaTile
        if tile not in MapHelpers.getAroundingTiles(self.Tile, self._logic.Map):
            raise Exception("you are not aloud to move this unit more than one tile")
        elif tile.Unit is not None and tile.Unit.Owner != self.Owner:
            raise Exception("You need to fight to go to this tile")
        # check for actions with the sea
        elif type(tile) is SeaTile:
            if tile.Unit is None:
                self.Tile.Unit = None
                tile.Unit = self
                self.Unit.Tile = tile
                self._tile = tile

        self._logic.PlayingPlayer.Moves -= 1


