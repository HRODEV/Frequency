import pygame
from pygame.surface import Surface

import Vector2
import Game
from Board.Board import Board
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem


class EnterGame(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=None, hover: Surface=None, rect=None, newState=None):
        image = image if image is not None else pygame.image.load('images/buttons/playButton.png').convert_alpha()
        hover = hover if hover is not None else pygame.image.load('images/buttons/playButtonHover.png').convert_alpha()
        super().__init__(offset, image, hover, rect)
        self._newState = newState

    def Update(self, game: Game):
        if self.IsClickedByMouse(game):
            self._newState = Board(game)
            game.Logic.StartGame()
        return super().Update(game)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

    def GetNewState(self):
        return self._newState

