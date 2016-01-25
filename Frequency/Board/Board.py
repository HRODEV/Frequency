import pygame

import Game
from Board.Map.Map import *
from Board.MenuLeft.MenuLeft import *
from Board.MenuRight.MenuRight import *


class Board:

    def __init__(self, game, menuleft=None, menuright=None, map=None):
        self.Map = map if map is not None else Map(game)
        self.MenuLeft = menuleft if menuleft is not None else MenuLeft(game)
        self.MenuRight = menuright if menuright is not None else MenuRight(game)


    def Update(self, game: Game):
        return Board(game, self.MenuLeft.Update(game), self.MenuLeft.Update(game), self.Map.Update(game))


    def Draw(self, game: Game):
        self.MenuLeft.Draw(game)
        self.MenuRight.Draw(game)
        self.Map.Draw(game)
