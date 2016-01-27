import pygame
import Game
from Vector2 import Vector2
from Helpers.EventHelpers import EventExist


class MenuLeft:

    def __init__(self, game, size=None, position=None, endturnButtonRect=None):
        self.Size = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2, game.Settings.Resolution.Y)
        self.Position = Vector2(0, 0)
        self.EndturnButtonRect = endturnButtonRect

        game.Settings.SetMenuLeftSize(self.Size)

    def Update(self, game: Game):
        if self.EndturnButtonIsClickedByMouse(game):
            game.Logic.EndTurn(game)
        return MenuLeft(game, self.Size, self.Position)

    def Draw(self, game : Game):
        # Draw the background
        pygame.draw.rect(game.Settings.GetScreen(),(255, 255, 255), (self.Position.X, self.Position.Y, self.Size.X, self.Size.Y))

        # Draw end turn button
        endTurnButton = pygame.transform.scale(pygame.image.load('images/buttons/endturnButton.png'), [150, 25])
        self.EndturnButtonRect = game.Settings.GetScreen().blit(endTurnButton, (10, 100))


    def EndturnButtonIsHoverdByMouse(self):
        return self.EndturnButtonRect is not None and self.EndturnButtonRect.collidepoint(pygame.mouse.get_pos())

    def EndturnButtonIsClickedByMouse(self, game):
        return self.EndturnButtonIsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)