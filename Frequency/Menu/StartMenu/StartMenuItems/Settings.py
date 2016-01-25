import pygame
from pygame.surface import Surface

import Vector2
from Board.Board import Board
from Menu.PlayerMenu.PlayerMenuItems.PlayerSelection import PlayerSelection
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem


class Settings(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/buttons/settingsButton.png'), rect=None, newState=None):
        super().__init__(offset, image, rect)
        self._newState = newState

    def Update(self, game):
        if self.IsClickedByMouse(game):
            self._newState = SettingsMenu(game.Settings.Resolution)
        return StartMenuItem.Update(self, game)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

    def GetNewState(self):
        return self._newState

