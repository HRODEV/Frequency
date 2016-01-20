import pygame
from pygame.surface import Surface

import Vector2
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem


class Rules(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface = pygame.image.load('images/buttons/rulesButton.png')):
        super().__init__(offset, image)

    def Update(self):
        return StartMenuItem.Update(self)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

