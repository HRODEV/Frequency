import pygame
from pygame.surface import Surface

from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem
from Vector2 import Vector2


class ExitGame(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/buttons/exitButton.png'), rect=None):
        super().__init__(offset, image, rect)

    def Update(self, game):
        return StartMenuItem.Update(self, game)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)