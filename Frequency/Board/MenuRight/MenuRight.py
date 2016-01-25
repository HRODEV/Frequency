import pygame
import Game
from Vector2 import Vector2

class MenuRight:

    def __init__(self, game, size=None, position=None):
        self.Options = ["Buy units", "Your money", "Lands", "Turn income", "Next turn income", "Remaining moves"]
        self.Size = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2, game.Settings.Resolution.Y)
        self.Position = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2 + game.Settings.GetMapSize().X, 0)
        game.Settings.SetMenuLeftSize(self.Size)
        self.Screen = game.Settings.GetScreen()


    def Update(self, game: Game):
        return MenuRight(game, self.Size, self.Position)

    def Draw(self, game : Game):

        self.Font = game.Settings.getFont()

        for rightMenuItem in self.Options:
            self.Screen.blit(self.Font.render('Hallo', True, (255, 255, 255)), (0, 0))

        pygame.draw.rect(self.Screen,
                         (0, 0, 255),
                         (self.Position.X, self.Position.Y, self.Size.X, self.Size.Y))