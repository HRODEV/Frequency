import pygame

from Board.Map.ForestTile import ForestTile
from Board.Map.IceTile import IceTile
from Board.Map.DesertTile import DesertTile
from Board.Map.SwampTile import SwampTile
from Board.Map.GoldTile import GoldTile
from Board.Map.SeaTile import SeaTile
from Board.Map.Tile import *
from Vector2 import Vector2


class Map:

    def __init__(self, resolution, tiles=None):
        self.Resolution = resolution
        self.Tiles = tiles if tiles is not None else self.GenerateTiles()


    def GenerateTiles(self):
        maxTiles = Vector2(18, 18)
        maxTileSize = Vector2(self.Resolution.X // maxTiles.X, self.Resolution.Y // maxTiles.Y)
        tiles = []

        for X in range(0, maxTiles.X):
            for Y in range(0, maxTiles.Y):
                TileType = self.DetermineTileType(X, Y)
                tiles.append(TileType(Vector2(X, Y), Vector2(maxTileSize.X, maxTileSize.Y)))

        return tiles


    def DetermineTileType(self, X, Y):
        if X < 7 and Y < 7:
            return ForestTile
        if X > 10 and X < 18 and Y < 7:
            return IceTile
        if X < 7 and Y >10 and Y < 18:
            return DesertTile
        if X > 10 and X < 18 and Y > 10:
            return SwampTile
        if X > 6 and X < 11 and Y > 6 and Y < 11:
            return GoldTile
        else:
            return SeaTile




    def Update(self, game):
        return Map(self.Resolution, [tile.Update(game) for tile in self.Tiles])


    def Draw(self, game):
        for tile in self.Tiles:
            tile.Draw(game)