import pygame
from pygame.surface import Surface

import Vector2
from Menu.SettingsMenu.SettingsMenu import SettingsMenu
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem


class Settings(StartMenuItem):
    def __init__(self, offset: Vector2, image: Surface = None, hover: Surface = None, rect=None, newState=None):
        image = image if image is not None else pygame.image.load('images/buttons/settingsButton.png').convert_alpha()
        hover = hover if hover is not None else pygame.image.load(
            'images/buttons/settingsButtonHover.png').convert_alpha()
        super().__init__(offset, image, hover, rect)
        self._newState = newState

    def Update(self, game):
        if self.IsClickedByMouse(game):
            self._newState = SettingsMenu(game.Settings.Resolution)
        return StartMenuItem.Update(self, game)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

    def GetNewState(self):
        return self._newState
