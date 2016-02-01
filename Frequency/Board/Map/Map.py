import pygame
from functools import reduce

from Board.Buildings.Base import Base
from Board.Map.Tile import *
from Vector2 import Vector2


class Map:

    def __init__(self, game, tiles=None, selectedTile=None):
        self.Resolution = game.Settings.Resolution
        self.Tiles = tiles if tiles is not None else self.GenerateTiles(game)
        self.SelectedTile = selectedTile


    def GenerateTiles(self, game):
        maxTiles = Vector2(18, 18)
        maxLength = min(self.Resolution.X // maxTiles.X, self.Resolution.Y // maxTiles.Y)
        maxTileSize = Vector2(maxLength, maxLength)
        tiles = []
        game.Settings.SetMapSize(Vector2(maxTiles.X * maxLength, maxTiles.X * maxLength))

        for X in range(0, maxTiles.X):
            row = []
            for Y in range(0, maxTiles.Y):
                logicTile = game.Logic.Map.GetTile(Vector2(X, Y))
                TileType = self.DetermineTileType(logicTile)
                row.append(TileType(Vector2(X, Y), maxTileSize, logicTile))
            tiles.append(row)

        return tiles

    @property
    def ActiveTile(self):
        return self.SelectedTile

    def SetActiveTile(self, position: Vector2):
        for tile in self.TilesIterator:
                tile.Selected = False
        if position is None:
            self.SelectedTile = None
        else:
            self.SelectedTile = self.Tiles[position.X][position.Y]
            self.SelectedTile.Selected = True


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

    @property
    def TilesIterator(self):
        for row in self.Tiles:
            for tile in row:
                yield tile

    def Update(self, game, onSelectedTileChanged):

        isClicked = next((True for tile in self.TilesIterator if tile.IsClickedByMouse(game)), False)
        nList = []
        for row in self.Tiles:
            nRow = []
            for tile in row:
                newTile = tile.Update(game)
                if isClicked:
                    if newTile.IsClickedByMouse(game):
                        newTile.Selected = True
                        self.SelectedTile = newTile
                        onSelectedTileChanged(newTile.LogicTile)
                    else:
                        newTile.Selected = False
                elif tile == self.SelectedTile:
                    self.SelectedTile = newTile
                nRow.append(newTile)
            nList.append(nRow)

        return Map(game, nList, self.SelectedTile)

    def Draw(self, game):
        for row in self.Tiles:
            for tile in row:
                tile.Draw(game)
