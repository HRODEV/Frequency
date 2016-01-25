import pygame
from pygame.surface import Surface

from Settings import GameSettings
from Board.Board import Board
import Vector2
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem


class ThreePlayers(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/buttons/3pButton.png'), rect=None, newState = None):
        super().__init__(offset, image, rect)
        self.NewState = newState

    def Update(self, game):
        if self.IsClickedByMouse(game):
            self.NewState = Board(game)
            GameSettings.UpdatePlayers(game.Settings, 3)


        return StartMenuItem.Update(self, game)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

    def GetNewState(self):
        return self.NewState