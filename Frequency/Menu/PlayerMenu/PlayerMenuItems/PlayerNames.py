from functools import reduce

import pygame

import Game
from Menu.HeadMenu import HeadMenu
from Menu.PlayerMenu.PlayerMenuItems.EnterGame import EnterGame
from Vector2 import Vector2


class PlayerNames(HeadMenu):

    def __init__(self, resolution:Vector2, background=None, logo=None, startMenuItems=None):
        super().__init__(resolution, background, logo)

        self.StartMenuItems = startMenuItems if startMenuItems is not None \
            else [EnterGame(Vector2(0, 0))]

    def Update(self, game: Game):
        newStartMenuItems = [smi.Update(game) for smi in self.StartMenuItems]

        newstate = reduce(lambda state, smi: smi.GetNewState() if smi.IsClickedByMouse(game) else state, newStartMenuItems, None)

        return newstate if newstate is not None \
            else PlayerNames(game, self.Background, self.Logo, newStartMenuItems)

    def Draw(self, game: Game):
        super().Draw(game)

        for menuItem in self.StartMenuItems:
            menuItem.Draw(game)
