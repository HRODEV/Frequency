from GameLogic import MapHelpers
from GameLogic.Barrack import Barrack


def getBarackPrice(tile, character=None):
    from GameLogic.Map import SeaTile, GoldTile, ForestTile, DesertTile, IceTile, SwampTile
    from GameLogic.Character import ForestCharacter, DesertCharacter, IceCharacter, SwampCharacter
    if type(tile) is SeaTile:
        return
    elif type(tile) is GoldTile:
        return 2000
    else:
        if (type(tile) is ForestTile and type(character) is ForestCharacter) \
                or (type(tile) is DesertTile and type(character) is DesertCharacter) \
                or (type(tile) is IceTile and type(character) is IceCharacter) \
                or (type(tile) is SwampTile and type(character) is SwampCharacter):
            return 500
        return 1500

def BuyBarrack(logic, tile, player):
    price = getBarackPrice(tile, player.Character)
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
            return tile.Building
