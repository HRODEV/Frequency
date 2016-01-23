import pygame

import Game
import Vector2
from Board.Map.Map import *


class Board:

    def __init__(self, resolution, map=None):
        self.Map = Map(resolution)


    def Update(self, game: Game):
        return Board(game.Settings.Resolution, self.Map.Update(game))


    def Draw(self, game: Game):
        self.Map.Draw(game)