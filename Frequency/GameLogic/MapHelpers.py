from GameLogic.Map import Tile, Map
from Vector2 import Vector2


def getAroundingTiles(tile: Tile, map: Map):
    loc = tile.Position
    aroundingLocations = [(loc.X-1, loc.Y-1), (loc.X, loc.Y-1), (loc.X+1, loc.Y-1),
                          (loc.X-1, loc.Y),                     (loc.X+1, loc.Y),
                          (loc.X-1, loc.Y+1), (loc.X, loc.Y+1), (loc.X+1, loc.Y+1)]
    # filter locations outside the board
    return [map.GetTile(Vector2(tloc.X, tloc.Y)) for tloc in aroundingLocations if 0 <= tloc.X <= 17 and 0 <= tloc.Y <= 17]
