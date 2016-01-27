import pygame
from pygame.surface import Surface

import Vector2
from Menu.PlayerMenu.PlayerSelection import PlayerSelection
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem


class StartGame(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/buttons/playButton.png'),hover: Surface=pygame.image.load('images/buttons/playButtonHover.png'), rect=None, newState=None):
        super().__init__(offset, image, hover, rect)
        self._newState = newState


    def Update(self, game):
        if self.IsClickedByMouse(game):
            self._newState = PlayerSelection(game.Settings.Resolution)
        nself = super().Update(game)
        return StartGame(nself.Offset, nself.Image, nself.Hover, nself.Rect, self._newState)


    def Draw(self, game):
        super().Draw(game)

    def GetNewState(self):
        return self._newState

