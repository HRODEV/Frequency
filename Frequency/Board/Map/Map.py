import pygame

from Board.Map.ForestTile import ForestTile
from Board.Map.IceTile import IceTile
from Board.Map.DesertTile import DesertTile
from Board.Map.SwampTile import SwampTile
from Board.Map.GoldTile import GoldTile
from Board.Map.SeaTile import SeaTile
from Vector2 import Vector2


class Map:

    def __init__(self, game, tiles=None):
        self.Resolution = game.Settings.Resolution
        self.Tiles = tiles if tiles is not None else self.GenerateTiles(game)


    def GenerateTiles(self, game):
        maxTiles = Vector2(18, 18)
        maxLength = min(self.Resolution.X // maxTiles.X, self.Resolution.Y // maxTiles.Y)
        maxTileSize = Vector2(maxLength, maxLength)
        tiles = []
        game.Settings.SetMapSize(Vector2(maxTiles.X * maxLength, maxTiles.X * maxLength))


        for X in range(0, maxTiles.X):
            row = []
            for Y in range(0, maxTiles.Y):
                TileType = self.DetermineTileType(game.Logic.Map.GetTile(Vector2(X, Y)))
                row.append(TileType(Vector2(X, Y), maxTileSize))
            tiles.append(row)

        return tiles


    def DetermineTileType(self, logicTile):
        import GameLogic.Map
        if type(logicTile) is GameLogic.Map.DesertTile:
            return DesertTile
        elif type(logicTile) is GameLogic.Map.ForestTile:
            return ForestTile
        elif type(logicTile) is GameLogic.Map.GoldTile:
            return GoldTile
        elif type(logicTile) is GameLogic.Map.IceTile:
            return IceTile
        elif type(logicTile) is GameLogic.Map.SeaTile:
            return SeaTile
        elif type(logicTile) is GameLogic.Map.SwampTile:
            return SwampTile
        else:
            raise Exception("%s type is not sported" % str(type(logicTile)))


    def Update(self, game):
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            self.MoveUnit(self.Tiles[0][17])
        nList = []
        for row in self.Tiles:
            nRow = []
            for tile in row:
                newTile = tile.Update(game)
                nRow.append(newTile)
            nList.append(nRow)
        return Map(game, nList)

    def Draw(self, game):
        for row in self.Tiles:
            for tile in row:
                tile.Draw(game)
