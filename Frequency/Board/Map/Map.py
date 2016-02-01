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
        if position is None:
            self.SelectedTile = None
            for tile in self.TilesIterator:
                tile.Selected = False


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
        if(game.Events):
            for event in game.Events:
                if event.type == pygame.KEYDOWN:
                    self.MoveUnit(event.key, game)
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

    def MoveUnit(self, movement, game):
        mapSize = game.Settings.GetMaxTiles()
        tile = self.SelectedTile
        newTile = None
        # If the tile has units and the movement is one of the key.events that we want
        if tile is not None:
            if game.Logic.PlayingPlayer.Moves > 0:
                # Update map with new tile based on the key event we received
                # Up
                if(movement == 1):
                    if(tile.Position.Y - 1 >= 0):
                        newTile = self.Tiles[tile.Position.X][tile.Position.Y-1]
                # Up Right
                if(movement == 2):
                    if(tile.Position.Y - 1 >= 0 and tile.Position.X + 1 >= 0 and tile.Position.X + 1 < mapSize.X):
                        newTile = self.Tiles[tile.Position.X+1][tile.Position.Y-1]
                # Right
                if(movement == 3):
                    if(tile.Position.X + 1 >= 0 and tile.Position.X + 1 < mapSize.X):
                        newTile = self.Tiles[tile.Position.X+1][tile.Position.Y]
                # Down Right
                if(movement == 4):
                    if(tile.Position.X + 1 >= 0 and tile.Position.X + 1 < mapSize.X and
                       tile.Position.Y + 1 >= 0 and tile.Position.Y + 1 < mapSize.Y):
                        newTile = self.Tiles[tile.Position.X+1][tile.Position.Y+1]
                # Down
                if(movement == 5):
                    if(tile.Position.Y + 1 >= 0 and tile.Position.Y + 1 < mapSize.Y):
                        newTile = self.Tiles[tile.Position.X][tile.Position.Y+1]
                # Down Left
                if(movement == 6):
                    if(tile.Position.X - 1 >= 0 and tile.Position.Y + 1 >= 0 and tile.Position.Y + 1 < mapSize.Y):
                        newTile = self.Tiles[tile.Position.X-1][tile.Position.Y+1]
                # Left
                if(movement == 7):
                    if(tile.Position.X - 1 >= 0):
                        newTile = self.Tiles[tile.Position.X-1][tile.Position.Y]
                if(movement == 8):
                    if(tile.Position.X -1 >= 0 and tile.Position.Y - 1 >= 0):
                        newTile = self.Tiles[tile.Position.X-1][tile.Position.Y-1]

                if(newTile is not None):
                    newTile.Units = tile.Units
                    newTile.Selected = True
                    self.SelectedTile = newTile
                    game.Logic.PlayingPlayer.Moves -= 1



        if(newTile is not None):
            self.Tiles[tile.Position.X][tile.Position.Y].Units = []
            self.Tiles[tile.Position.X][tile.Position.Y].Selected = False