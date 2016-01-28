import pygame
from pygame.surface import Surface

import Vector2
from Board.MenuLeft.ArrowItems.ArrowItem import ArrowItem


class ArrowLeft(ArrowItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/arrows/ArrowDarkLeft.png'), hover: Surface=pygame.image.load('images/arrows/ArrowLightLeft.png'), rect=None, newState=None):
        super().__init__(offset, image, hover, rect)
        self._newState = newState

    def Update(self, game):
        if self.IsClickedByMouse(game):
            print("Left")
        return ArrowItem.Update(self, game)

    def Draw(self, game):
        ArrowItem.Draw(self, game)

    def GetNewState(self):
        return self._newState

