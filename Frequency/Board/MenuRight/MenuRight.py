import pygame
import Game
from Vector2 import Vector2

class MenuRight:

    def __init__(self, game, size=None, position=None):
        self.Size = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2, game.Settings.Resolution.Y)
        self.Position = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2 + game.Settings.GetMapSize().X, 0)
        game.Settings.SetMenuLeftSize(self.Size)


    def Update(self, game: Game):
        return MenuRight(game, self.Size, self.Position)


    def Draw(self, game : Game):
        pygame.draw.rect(game.Settings.GetScreen(),
                         (0, 0, 255),
                         (self.Position.X, self.Position.Y, self.Size.X, self.Size.Y))