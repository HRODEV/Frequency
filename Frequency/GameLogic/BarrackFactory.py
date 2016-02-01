from GameLogic import MapHelpers
from GameLogic.Barrack import Barrack

def getBarackPrice(tile, character=None):
    from GameLogic.Map import SeaTile, GoldTile
    if type(tile) is SeaTile:
        return
    elif type(tile) is GoldTile:
        return 2000
    else:
        return 500

def BuyBarrack(logic, tile, player):
    price = getBarackPrice(tile)
    if price is None:
        return

    if price > player.Money:
        return
    # check if tile is empty
    if tile.Unit is None and tile.Building is None:
        if next((True for t in MapHelpers.getAroundingTiles(tile, logic.Map) if t.Unit is not None and t.Unit.Owner == player), False):
            tile.Building = Barrack(tile, player)
            player.Money -= price
            player.Moves -= 1
