import pygame
from pygame.surface import Surface

from Settings import GameSettings
from Board.Board import Board
import Vector2
from GameLogic.GameLogic import GameLogic
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem


class TwoPlayers(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/buttons/2pButton.png'), rect=None, newState = None, gameLogic = None):
        super().__init__(offset, image, rect)
        self.NewState = newState
        self.GameLogic = gameLogic if gameLogic is not None else GameLogic()

    def Update(self, game):
        if self.IsClickedByMouse(game):
            self.NewState = Board(game)
            GameSettings.UpdatePlayers(game.Settings, 2)


        return StartMenuItem.Update(self, game)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

    def GetNewState(self):
        return self.NewState