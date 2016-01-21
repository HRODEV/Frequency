import pygame
from pygame.surface import Surface

from Vector2 import Vector2


class GameSettings:

    def __init__(self, resolution: Vector2 = Vector2(700, 700), screen: Surface = None):
        self.Resolution = resolution

        self.screen = screen if screen is not None \
            else pygame.display.set_mode([resolution.X,resolution.Y])

    def updateResolution(self, newResolution):
        self.Resolution = newResolution

    def GetScreen(self):
        return self.screen


