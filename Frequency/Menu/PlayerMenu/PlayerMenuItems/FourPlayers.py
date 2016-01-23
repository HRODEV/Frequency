import pygame
from pygame.surface import Surface

from Board.Board import Board
import Vector2
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem


class FourPlayers(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/buttons/4pButton.png'), rect=None, newState = None):
        super().__init__(offset, image, rect)
        self.NewState = newState

    def Update(self, game):
        if self.IsClickedByMouse(game):
            self.NewState = Board(game.Settings.Resolution)

        return StartMenuItem.Update(self, game)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

    def GetNewState(self):
        return self.NewState
