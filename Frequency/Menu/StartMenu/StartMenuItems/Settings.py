import pygame
from pygame.surface import Surface

import Vector2
from Menu.SettingsMenu.SettingsMenu import SettingsMenu
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem


class Settings(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/buttons/settingsButton.png'), hover: Surface=pygame.image.load('images/buttons/settingsButtonHover.png'), rect=None, newState=None):
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

