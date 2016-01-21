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
        maxTilesX = self.Resolution.X // 75
        maxTilesY = self.Resolution.Y // 75
        tiles = []

        for X in range(0, maxTilesX):
            for Y in range(0, maxTilesY):
                TileType = self.DetermineTileType(X, Y)
                tiles.append(TileType(Vector2(X, Y)))

        return tiles


    def DetermineTileType(self, X, Y):
        if X < 7 and Y < 7:
            return ForestTile
        if X > 11 and X < 18 and Y < 7:
            return IceTile
        if X < 7 and Y > 11 and Y < 18:
            return DesertTile
        if X > 11 and X < 18 and Y < 18:
            return SwampTile
        else:
            return SeaTile




    def Update(self, game):
        return Map(self.Resolution, [tile.Update(game) for tile in self.Tiles])


    def Draw(self, game):
        for tile in self.Tiles:
            tile.Draw(game)