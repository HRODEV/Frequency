import pygame
from Board.Map.Tile import *
from Vector2 import Vector2

class Map:

    def __init__(self, resolution):
        self.Resolution = resolution
        self.Tiles = None
        self.maxTilesX = None
        self.maxTilesY = None

        self.GenerateTiles()


    def GenerateTiles(self):
        tileForProperties = Tile(0, Vector2(0, 0), 100, 150, "images/tiles/Desert.jpg")
        self.maxTilesX = self.Resolution.X // tileForProperties.Width
        self.maxTilesY = self.Resolution.Y // tileForProperties.Height
        tiles = []
        X = 0
        Y = 0

        for Y in range(0, self.maxTilesX):
            for X in range(0, self.maxTilesY):
                tiles.append(Tile(0, Vector2(X, Y), 100, 150, "images/tiles/Desert.jpg"))

        self.Tiles = tiles


    def Update(self):
        return self


    def Draw(self, game):
        for tile in self.Tiles:
            tile.Draw(game)