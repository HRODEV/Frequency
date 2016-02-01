import pygame
from pygame.surface import Surface

from Vector2 import Vector2


class GameSettings:


    def __init__(self, resolution: Vector2 = Vector2(1280, 800),
                 screen: Surface = None,
                 tileSize = None,
                 newPlayers = 0,
                 mapSize = None,
                 menuLeftSize = None,
                 fullscreen = False):

        self._resolution = resolution
        self.TileSize = tileSize
        self.newPlayer = newPlayers
        self.MapSize = mapSize
        self.MenuLeftSize = menuLeftSize
        self.Fullscreen = fullscreen
        self.Font = pygame.font.SysFont("Arial", 72)

        self.screen = screen if screen is not None \
            else pygame.display.set_mode([resolution.X, resolution.Y])

        self.SetMaxTiles(Vector2(18, 18))

    @property
    def Resolution(self) -> Vector2:
        return self._resolution

    def SetResolution(self, newResolution: Vector2, fullscreen=False):
        self._resolution = newResolution

        if fullscreen is True:
            if self.Fullscreen is True:
                self.screen = pygame.display.set_mode(newResolution.Position)
                self.Fullscreen = False
            else:
                self.screen = pygame.display.set_mode(newResolution.Position, pygame.FULLSCREEN)
                self.Fullscreen = True
        else:
            self.screen = pygame.display.set_mode(newResolution.Position)



    def GetScreen(self) -> Surface:
        return self.screen

    def SetMaxTiles(self, maxTiles):
        self.MaxTiles = maxTiles

    def GetMaxTiles(self):
        return self.MaxTiles

    def SetMapSize(self, mapSize):
        self.MapSize = mapSize

    def GetMapSize(self):
        return self.MapSize

    def getFont(self):
        return self.Font

    def setFont(self, newFont):
        self.Font = newFont

    def SetMenuLeftSize(self, menuSize):
            self.MenuLeftSize = menuSize

    def GetMenuLeftSize(self):
        return self.MenuLeftSize
