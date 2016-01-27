import pygame
from pygame.surface import Surface

from GameLogic.GameLogic import GameLogic
from Menu.PlayerMenu.PlayerMenuItems.PlayerNames import PlayerNames
import Vector2
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem


class TwoPlayers(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/buttons/2pButton.png'), hover: Surface=pygame.image.load('images/buttons/2pButtonHover.png'), rect=None, newState=None):
        super().__init__(offset, image, hover, rect)
        self.NewState = newState

    def Update(self, game):
        if self.IsClickedByMouse(game):
            game.Logic = GameLogic()
            self.NewState = PlayerNames(game.Settings.Resolution)
            game.Settings.UpdatePlayers(2)

        return StartMenuItem.Update(self, game)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

    def GetNewState(self):
        return self.NewState