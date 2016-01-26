import pygame
from pygame.surface import Surface

import Vector2
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem
from Menu.PlayerMenu.PlayerMenuItems.PlayerNames import PlayerNames


class ThreePlayers(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/buttons/3pButton.png'), rect=None, newState = None):
        super().__init__(offset, image, rect)
        self.NewState = newState

    def Update(self, game):
        if self.IsClickedByMouse(game):
            self.NewState = PlayerNames(game)
            game.Settings.UpdatePlayers(3)


        return StartMenuItem.Update(self, game)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

    def GetNewState(self):
        return self.NewState