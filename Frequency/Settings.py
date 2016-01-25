import pygame
from pygame.surface import Surface

from Vector2 import Vector2


class GameSettings:

    def __init__(self, resolution: Vector2 = Vector2(1280, 800), screen: Surface = None, tileSize = None, newPlayers = 0):
        self.Resolution = resolution
        self.tileSize = tileSize

        self.screen = screen if screen is not None \
            else pygame.display.set_mode([resolution.X,resolution.Y])

        self.SetMaxTiles(Vector2(18, 18))
        self.Players = newPlayers

    def updateResolution(self, newResolution):
        self.Resolution = newResolution

    def GetScreen(self):
        return self.screen

    def SetMaxTiles(self, maxTiles):
        self.maxTiles = maxTiles

    def GetMaxTiles(self):
        return self.maxTiles

    def UpdatePlayers(self, newPlayers):
        self.Players = newPlayers