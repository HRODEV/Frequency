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
        maxTiles = Vector2(self.Resolution.X // 35, self.Resolution.Y // 35)
        tiles = []

        for X in range(0, maxTiles.X):
            for Y in range(0, maxTiles.Y):
                TileType = self.DetermineTileType(X, Y)
                tiles.append(TileType(Vector2(X, Y), Vector2(50, 50)))

        return tiles


    def DetermineTileType(self, X, Y):
        if X < 7 and Y < 7:
            return ForestTile
        if X > 12 and X < 20 and Y < 7:
            return IceTile
        if X < 7 and Y >12 and Y < 20:
            return DesertTile
        if X > 12 and X < 20 and Y > 12:
            return SwampTile
        if X > 7 and X < 12 and Y > 7 and Y < 12:
            return GoldTile
        else:
            return SeaTile




    def Update(self, game):
        return Map(self.Resolution, [tile.Update(game) for tile in self.Tiles])


    def Draw(self, game):
        for tile in self.Tiles:
            tile.Draw(game)