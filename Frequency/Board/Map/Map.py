import pygame

from Board.Map.DesertTile import DesertTile
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
                tiles.append(DesertTile(Vector2(X, Y)))

        return tiles


    def Update(self, game):
        return Map(self.Resolution, [tile.Update(game) for tile in self.Tiles])


    def Draw(self, game):
        for tile in self.Tiles:
            tile.Draw(game)