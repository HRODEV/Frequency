import pygame

import Game
from Helpers import Colors
from Helpers.EventHelpers import EventExist
from Vector2 import Vector2


class ActionPanel:
    def __init__(self, game: Game, endturnButtonRect=None):
        self.Size = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2, game.Settings.Resolution.Y)
        self.Position = Vector2(0, 0)
        self.EndturnButtonRect = endturnButtonRect
        self.EndTurnButtonImage = pygame.transform.scale(pygame.image.load('images/buttons/endturnButton.png'), [150, 25])

        # TODO netter als je deze verantwoordelijkheid geeft bij het object die dit object beheert
        game.Settings.SetMenuLeftSize(self.Size)

    def Update(self, game: Game) -> 'ActionPanel':
        if self.EndturnButtonIsClickedByMouse(game):
            game.Logic.EndTurn(game)
        return ActionPanel(game, self.EndturnButtonRect)

    def Draw(self, game : Game):
        font = pygame.font.Font(None, 30)
        font.set_bold(True)
        # Draw the background
        pygame.draw.rect(game.Settings.GetScreen(), Colors.WHITE, (self.Position.X, self.Position.Y, self.Size.X, self.Size.Y))

        game.Settings.GetScreen().blit(font.render("Action panel", True, Colors.BLACK), (10,10))

        # Draw end turn button
        self.EndturnButtonRect = game.Settings.GetScreen().blit(self.EndTurnButtonImage, (10, 200))

    def EndturnButtonIsHoverdByMouse(self):
        return self.EndturnButtonRect is not None and self.EndturnButtonRect.collidepoint(pygame.mouse.get_pos())

    def EndturnButtonIsClickedByMouse(self, game):
        return self.EndturnButtonIsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)

class DefaultActionPanel(ActionPanel):

    def Update(self, game: Game):
        nself = super().Update(game)
        DefaultActionPanel(game, nself.EndturnButtonRect)

    def Draw(self, game : Game):
        super().Draw(game)

        font = pygame.font.Font(None, 20)
        game.Settings.GetScreen().blit(font.render("Default", True, Colors.BLACK), (10, 35))

        game.Settings.GetScreen().blit(font.render("Choose an tile or end the turn",
                                                   True, Colors.BLACK), (10, 55))