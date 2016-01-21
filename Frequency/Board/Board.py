import pygame

import Game
from Board.Map.Map import *


class Board:

    def __init__(self, resolution, map=None):
        self.Map = Map(resolution)


    def Update(self, game: Game):
        return Board(game.Settings.Resolution, self.Map.Update())


    def Draw(self, game: Game):
        self.Map.Draw(game)

