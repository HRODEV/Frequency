import pygame
import Game
from Vector2 import Vector2

class MenuLeft:

    def __init__(self, game, size=None, position=None):
        self.Size = Vector2(game.Settings.Resolution.X * 0.17, game.Settings.Resolution.Y)
        self.Position = Vector2(0, 0)


    def Update(self, game: Game):
        return MenuLeft(game, self.Size, self.Position)


    def Draw(self, game : Game):
        pygame.draw.rect(game.Settings.GetScreen(),
                         (255, 0, 0),
                         (self.Position.X, self.Position.Y, self.Size.X, self.Size.Y)
                         )