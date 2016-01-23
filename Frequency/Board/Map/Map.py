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
        maxLength = min(self.Resolution.X // maxTiles.X, self.Resolution.Y // maxTiles.Y)
        maxTileSize = Vector2(maxLength, maxLength)
        tiles = []

        for X in range(0, maxTiles.X):
            row = []
            for Y in range(0, maxTiles.Y):
                TileType = self.DetermineTileType(X, Y)
                row.append(TileType(Vector2(X, Y), maxTileSize))
            tiles.append(row)

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
        nList = []
        for row in self.Tiles:
            nRow = []
            for tile in row:
                newTile = tile.Update(game)
                nRow.append(newTile)
            nList.append(nRow)
        return Map(self.Resolution, nList)


    def Draw(self, game):
        for row in self.Tiles:
            for tile in row:
                tile.Draw(game)