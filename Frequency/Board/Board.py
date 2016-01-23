import pygame

import Game
from Board.Map.Map import *


class Board:

    def __init__(self, resolution, map=None):
        self.Map = map if map is not None else Map(resolution)


    def Update(self, game: Game):
        return Board(game.Settings.Resolution, self.Map.Update(game))


    def Draw(self, game: Game):
        self.Map.Draw(game)