import pygame
from pygame.surface import Surface

import Vector2
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem


class StartGame(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/buttons/playButton.png'), rect=None):
        super().__init__(offset, image, rect)

    def Update(self, game, events):
        return StartMenuItem.Update(self, game, events)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

