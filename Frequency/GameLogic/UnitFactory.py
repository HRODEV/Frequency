from GameLogic.Character import *
from GameLogic.Unit import *


def getUnitPrice(unitType, character):
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


def SellUnit(gameLogic, unitType, tile, player: Player):
    price = getUnitPrice(unitType, player.Character)
    if player.Money >= price:
        player.Money -= price
        unit = unitType(tile, player)
        return unit


