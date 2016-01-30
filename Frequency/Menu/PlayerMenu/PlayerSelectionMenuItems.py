import pygame
from pygame.surface import Surface

import Vector2
from GameLogic.GameLogic import GameLogic
from GameLogic.Player import Player
from Menu.PlayerMenu.PlayerNamesMenu import PlayerNamesMenu
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem


def emptyPlayerGeneratorN(n: int):
    return [Player("Player%i" % i, i) for i in range(0, n)]

class NPlayersMenuItem(StartMenuItem):
    def __init__(self, offset: Vector2, image: Surface, hover: Surface, rect=None, newState=None):
        super().__init__(offset, image, hover, rect)
        self._newState = newState

    def Update(self, game):
        if self.IsClickedByMouse(game):
            game.Logic = self._getLogic()
            self._newState = PlayerNamesMenu(game.Settings.Resolution)

        nself = super().Update(game)
        return type(self)(nself.Offset, nself.Image, nself.Hover, nself.Rect, self._newState)

    def _getLogic(self) -> GameLogic:
        return None

    def GetNewState(self):
        return self._newState


class FourPlayers(NPlayersMenuItem):

    def __init__(self, offset: Vector2, image: Surface = None, hover: Surface = None, rect=None, newState=None):
        image = image if image is not None else pygame.image.load('images/buttons/4pButton.png').convert_alpha()
        hover = hover if hover is not None else pygame.image.load('images/buttons/4pButtonHover.png').convert_alpha()
        super().__init__(offset, image, hover, rect, newState)

    def _getLogic(self):
        return GameLogic(emptyPlayerGeneratorN(4))


class ThreePlayers(NPlayersMenuItem):

    def __init__(self, offset: Vector2, image: Surface=None, hover: Surface=None, rect=None, newState=None):
        image = image if image is not None else pygame.image.load('images/buttons/3pButton.png').convert_alpha()
        hover = hover if hover is not None else pygame.image.load('images/buttons/3pButtonHover.png').convert_alpha()
        super().__init__(offset, image, hover, rect, newState)

    def _getLogic(self):
        return GameLogic(emptyPlayerGeneratorN(3))


class TwoPlayers(NPlayersMenuItem):

    def __init__(self, offset: Vector2, image: Surface=None, hover: Surface=None, rect=None, newState=None):
        image = image if image is not None else pygame.image.load('images/buttons/2pButton.png').convert_alpha()
        hover = hover if hover is not None else pygame.image.load('images/buttons/2pButtonHover.png').convert_alpha()
        super().__init__(offset, image, hover, rect, newState)

    def _getLogic(self):
        return GameLogic(emptyPlayerGeneratorN(2))
