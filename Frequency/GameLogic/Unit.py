from GameLogic import MapHelpers
from GameLogic import Player
from GameLogic.GameLogic import GameLogic


class Unit:
    def __init__(self, tile, owner: Player, logic: GameLogic):
        self._tile = tile
        self._tileFrom = tile
        self._owner = owner
        self._logic = logic
        owner.AddUnit(self)

    @property
    def TileFrom(self):
        return self._tileFrom

    @property
    def Tile(self):
        return self._tile

    @Tile.setter
    def Tile(self, value):
        self._tileFrom = self._tile
        self._tile = value

    @property
    def Owner(self) -> Player:
        return self._owner

    @property
    def AttackPoints(self) -> int:
        return 0

    @property
    def DefencePoints(self) -> int:
        return 0

    def MoveTo(self, tile: Tile):
        # check moves
        if self.Owner.Moves < 1:
            return
        # check turn
        if self.Owner != self._logic.PlayingPlayer:
            raise Exception("player is not on turn")
        # check if you move in the right area
        from GameLogic.Map import SeaTile
        if tile not in MapHelpers.getAroundingTiles(self.Tile, self._logic.Map):
            return
        elif tile.Unit is not None and tile.Unit.Owner != self.Owner:  # fight
            if self.AttackPoints > tile.Unit.DefencePoints:
                tile.Unit.Die()
            else:
                return
        elif tile.Building is not None:
            if tile.Building.Owner == self.Owner:
                return None
            else:
                tile.Building.DefencePoints -= self.AttackPoints
                self.Die()
                if tile.Building.DefencePoints <= 0:
                    tile.Building = None

        # check for actions with the sea
        if type(tile) is SeaTile:
            # check if there is a boat available
            if tile.Unit is not None and type(tile.Unit) is Boat:
                # check if it is possible to place this unit in the boat
                boat = tile.Unit
                if boat.Unit is not None:
                    return
                else:
                    boat.Unit = self
                    self.Tile.Unit = None
                    self.Tile = tile
            else:
                return
        # no sea
        else:
            if tile.Unit is None:
                if self.Tile.Unit == self:
                    self.Tile.Unit = None
                tile.Unit = self
                self.Tile = tile
            elif type(tile.Unit) is UnitGroup:
                unitGroup = tile.Unit
                if unitGroup.CountUnits < 4:
                    if self.Tile.Unit == self:
                        self.Tile.Unit = None
                    self.Tile = tile
                    unitGroup.AddUnit(self)
                else:
                    return
            elif isinstance(tile.Unit, Unit):
                group = UnitGroup(tile, self.Owner, self._logic)
                self.Tile.Unit = None
                self.Tile = tile
                group.AddUnit(self)
                group.AddUnit(tile.Unit)
                tile.Unit = group

        self._logic.PlayingPlayer.Moves -= 1

    def Die(self):
        self.Owner._units = [unit for unit in self.Owner._units if unit != self]
        self.Tile.Unit = None


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
        if type(unit) is UnitGroup or type(unit) is Boat:
            raise Exception("A UnitGroup can only hold normal units, not UnitGroups or boats")
        elif len(self._units) > 3:
            raise Exception("A unitGroup can not hold more than 4 units")
        else:
            self._units.append(unit)

    def RemoveUnit(self, unit: Unit):
        self._units = [_unit for _unit in self._units if _unit != unit]

    def MoveTo(self, tile):
        # check moves
        if self.Owner.Moves < 1:
            return
        # check turn
        if self.Owner != self._logic.PlayingPlayer:
            if self.AttackPoints > tile.Unit.DefencePoints:
                tile.Unit.Die()
            else:
                return
        # check if you move in the right area
        from GameLogic.Map import SeaTile
        if tile not in MapHelpers.getAroundingTiles(self.Tile, self._logic.Map):
            raise Exception("You are not allowed to move this unit more than one tile")
        elif tile.Unit is not None and tile.Unit.Owner != self.Owner:  # fight
            if self.AttackPoints == tile.Unit.DefencePoints:
                tile.Unit.Die()
                self.Die()
            elif self.AttackPoints > tile.Unit.DefencePoints:
                tile.Unit.Die()
            else:
                return
        if tile.Building is not None:
            if tile.Building.Owner == self.Owner:
                return None
            else:
                tile.Building.DefencePoints -= self.AttackPoints
                self.Die()
                if tile.Building.DefencePoints <= 0:
                    tile.Building = None
        # check for actions with the sea
        elif type(tile) is SeaTile:
            # check if there is a boat available
            if tile.Unit is not None and type(tile.Unit) is Boat:
                # check if it is possible to place this unit in the boat
                boat = tile.Unit
                if boat.Unit is not None:
                    return
                else:
                    boat.Unit = self
                    self.Tile.Unit = None
                    self.Tile = tile

        # no sea
        else:
            if tile.Unit is None:
                if self.Tile.Unit == self:
                    self.Tile.Unit = None
                tile.Unit = self
                self.Tile = tile
            elif type(tile.Unit) is not UnitGroup and self.CountUnits < 4:
                self.AddUnit(tile.Unit)
                if self.Tile.Unit == self:
                    self.Tile.Unit = None
                tile.Unit = self
                self.Tile = tile

            elif type(tile.Unit) is UnitGroup:
                return

        self._logic.PlayingPlayer.Moves -= 1

    @property
    def Units(self):
        """
        :return: it returns a copy
        """
        return self._units.copy()

    @property
    def AttackPoints(self):
        return sum([unit.AttackPoints for unit in self._units])

    @property
    def DefencePoints(self):
        return sum([unit.DefencePoints for unit in self._units])

    @property
    def CountUnits(self):
        return len(self._units)

    @property
    def Tile(self):
        return self._tile

    @Tile.setter
    def Tile(self, value):
        self._tileFrom = self._tile
        self._tile = value
        for unit in self._units:
            unit.Tile = value

    def Die(self):
        super().Die()
        for unit in self._units:
            unit.Die()


class Boat(Unit):
    def __init__(self, tile, owner, logic):
        self.Unit = None
        super().__init__(tile, owner, logic)

    @property
    def DefencePoints(self):
        return 6

    def MoveTo(self, tile):
        # check moves
        if self.Owner.Moves < 1:
            return
        # check turn
        if self.Owner != self._logic.PlayingPlayer:
            raise Exception("player is not on turn")
        # check if you move in the right area
        from GameLogic.Map import SeaTile
        if tile not in MapHelpers.getAroundingTiles(self.Tile, self._logic.Map):
            raise Exception("you are not aloud to move this unit more than one tile")
        elif tile.Unit is not None and tile.Unit.Owner != self.Owner:
            return
        # check for actions with the sea
        elif type(tile) is SeaTile:
            if tile.Unit is None:
                self.Tile.Unit = None
                tile.Unit = self
                self.Tile = tile
                self._tile = tile
                if self.Unit is not None:
                    self.Unit.Tile = tile
            else:
                return
        else:
            return

        self._logic.PlayingPlayer.Moves -= 1
