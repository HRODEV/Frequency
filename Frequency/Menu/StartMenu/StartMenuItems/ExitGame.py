import pygame
import sys
from pygame.surface import Surface

from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem
from Vector2 import Vector2


class ExitGame(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=None, hover: Surface=None, rect=None):
        image = image if image is not None else pygame.image.load('images/buttons/exitButton.png').convert_alpha()
        hover = hover if hover is not None else pygame.image.load('images/buttons/exitButtonHover.png').convert_alpha()
        super().__init__(offset, image, hover, rect)

    def Update(self, game):
        return StartMenuItem.Update(self, game)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

    def GetNewState(self):
        pygame.quit()
        sys.exit()
