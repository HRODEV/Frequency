from GameLogic.Character import *
from GameLogic.MapHelpers import getAroundingTiles
import Game

def getUnitPrice(unitType, character):
    from GameLogic.Unit import Soldier, Robot, Tank, Boat
    if unitType is Soldier:
        if type(character) is IceCharacter:
            return 120
        else:
            return 150
    elif unitType is Robot:
        if type(character) is ForestCharacter:
            return 240
        else:
            return 300
    elif unitType is Tank:
        if type(character) is DesertCharacter:
            return 600
        else:
            return 750
    elif unitType is Boat:
        if type(character) is SwampCharacter:
            return 800
        else:
            return 1000
    else:
        raise Exception("This is not a valid unit type")


def BuyUnit(gameLogic, unitType, tile, player):
    price = getUnitPrice(unitType, player.Character)
    if player.Money < price:
        return None
    # check if there is a building
    if next((False for tile in getAroundingTiles(tile, gameLogic.Map) if
             tile.Building is not None and
             tile.Building.Owner == player), True):  # check if it is his own building
        return None

    from GameLogic.Map import SeaTile
    import GameLogic.Unit
    if type(tile) is not SeaTile:
        if unitType is GameLogic.Unit.Boat:
            return
        elif tile.Unit is None:
            player.Money -= price
            unit = unitType(tile, player, gameLogic)
            tile.Unit = unit
            return unit
        elif type(tile.Unit) is GameLogic.Unit.UnitGroup:
            if tile.Unit.CountUnits > 3:
                return None
            else:
                player.Money -= price
                unit = unitType(tile, player, gameLogic)
                tile.Unit.AddUnit(unit)
                return unit
        elif isinstance(tile.Unit, GameLogic.Unit.Unit):
            existingUnit = tile.Unit
            group = GameLogic.Unit.UnitGroup(tile, player, gameLogic)
            group.AddUnit(existingUnit)
            player.Money -= price
            unit = unitType(tile, player, gameLogic)
            group.AddUnit(unit)
            tile.Unit = group
            return unit
    elif unitType is GameLogic.Unit.Boat:
        if tile.Unit is None:
            player.Money -= price
            unit = unitType(tile, player, gameLogic)
            tile.Unit = unit
            return unit