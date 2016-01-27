import pygame
from pygame.surface import Surface

import Vector2
import Game
from Board.Board import Board
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem


class EnterGame(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/buttons/playButton.png'), hover: Surface=pygame.image.load('images/buttons/playButtonHover.png'), rect=None, newState=None):
        super().__init__(offset, image, hover, rect)
        self._newState = newState

    def Update(self, game: Game):
        if self.IsClickedByMouse(game):
            self._newState = Board(game)
            game.Logic.StartGame()
        return super().Update(game)

    def CreatePlayers(self, game: Game):
        # TODO change the names of the already existing players in the gamelogic
        pass

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

    def GetNewState(self):
        return self._newState

