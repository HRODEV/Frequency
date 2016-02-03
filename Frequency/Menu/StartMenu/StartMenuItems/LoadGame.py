import pygame
from pygame.surface import Surface

from Menu.LoadGameMenu.LoadGameMenu import LoadGameMenu
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem
from Vector2 import Vector2


class LoadGame(StartMenuItem):
    def __init__(self, offset: Vector2, image: Surface = None, hover: Surface = None, rect=None, newState=None):
        image = image if image is not None else pygame.image.load('images/buttons/loadButton.png').convert_alpha()
        hover = hover if hover is not None else pygame.image.load('images/buttons/loadButtonHover.png').convert_alpha()
        super().__init__(offset, image, hover, rect)
        self._newState = newState

    def Update(self, game):
        if self.IsClickedByMouse(game):
            self._newState = LoadGameMenu(game.Settings.Resolution)
        nself = super().Update(game)
        return LoadGame(nself.Offset, nself.Image, nself.Hover, nself.Rect, self._newState)

    def Draw(self, game):
        super().Draw(game)

    def GetNewState(self):
        return self._newState
