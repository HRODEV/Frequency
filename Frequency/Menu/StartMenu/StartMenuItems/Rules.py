import pygame
from pygame.surface import Surface

import Vector2
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem


class Rules(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/buttons/rulesButton.png'), rect=None):
        super().__init__(offset, image, rect)

    def Update(self, game):
        return StartMenuItem.Update(self, game)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

