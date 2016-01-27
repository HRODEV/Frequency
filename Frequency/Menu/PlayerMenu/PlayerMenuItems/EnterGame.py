import pygame
from pygame.surface import Surface

import Vector2
import Game
from Board.Board import Board
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem


class EnterGame(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/buttons/playButton.png'), rect=None, newState=None):
        super().__init__(offset, image, rect)
        self._newState = newState

    def Update(self, game: Game):
        if self.IsClickedByMouse(game):
            self.CreatePlayers(game)
            self._newState = Board(game)
        return StartMenuItem.Update(self, game)

    def CreatePlayers(self, game: Game):
        for i in range(game.Settings.GetTotalPlayers()):
            game.Logic.AddNewPlayer("Player%i" %i)
            print("test")

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

    def GetNewState(self):
        return self._newState

