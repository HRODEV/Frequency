import pygame
from pygame.surface import Surface

from Vector2 import Vector2


class GameSettings:

    def __init__(self, resolution: Vector2 = Vector2(1280, 800),
                    screen: Surface = None,
                    tileSize = None,
                    mapSize = None):

        self.Resolution = resolution
        self.TileSize = tileSize
        self.MapSize = mapSize

        self.screen = screen if screen is not None \
            else pygame.display.set_mode([resolution.X, resolution.Y])

        self.SetMaxTiles(Vector2(18, 18))

    def updateResolution(self, newResolution):
        self.Resolution = newResolution

    def GetScreen(self):
        return self.screen

    def SetMaxTiles(self, maxTiles):
        self.MaxTiles = maxTiles

    def GetMaxTiles(self):
        return self.MaxTiles

    def SetMapSize(self, mapSize):
        self.MapSize = mapSize

    def GetMapSize(self):
        return self.MapSize
