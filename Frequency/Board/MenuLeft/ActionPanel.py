import pygame

import Game
from GameLogic.Map import Tile
from Board.MenuLeft.ArrowItem import *
from Helpers import Colors
from Helpers.EventHelpers import EventExist
from Vector2 import Vector2


class ActionPanel:
    def __init__(self, game: Game, tile: Tile = None, endturnButtonRect=None):
        self.Size = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2,
                            game.Settings.Resolution.Y)
        self.Position = Vector2(0, 0)
        self.Tile = tile
        self.EndturnButtonRect = endturnButtonRect

        self.Map = None
        self.EndTurnButtonImage = pygame.transform.scale(
            pygame.image.load('images/buttons/endturnButton.png').convert_alpha(), [150, 25])
        # TODO netter als je deze verantwoordelijkheid geeft bij het object die dit object beheert
        game.Settings.SetMenuLeftSize(self.Size)

    def Update(self, game: Game) -> 'ActionPanel':
        # End turn
        if self.EndturnButtonIsClickedByMouse(game):
            game.Logic.EndTurn(game)

        return ActionPanel(game, self.Tile, self.EndturnButtonRect)

    def Draw(self, game: Game):
        font = pygame.font.Font(None, 30)
        font.set_bold(True)
        # Draw the background
        pygame.draw.rect(game.Settings.GetScreen(), Colors.WHITE,
                         (self.Position.X, self.Position.Y, self.Size.X, self.Size.Y))

        game.Settings.GetScreen().blit(font.render("Action panel", True, Colors.BLACK), (10, 10))

        # Draw end turn button
        self.EndturnButtonRect = game.Settings.GetScreen().blit(self.EndTurnButtonImage,
                                                                (10, game.Settings.Resolution.Y - 50))

    def EndturnButtonIsHoverdByMouse(self):
        return self.EndturnButtonRect is not None and self.EndturnButtonRect.collidepoint(pygame.mouse.get_pos())

    def EndturnButtonIsClickedByMouse(self, game):
        return self.EndturnButtonIsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)


class DefaultActionPanel(ActionPanel):
    def Update(self, game: Game):
        nself = super().Update(game)
        return DefaultActionPanel(game, self.Tile, nself.EndturnButtonRect)

    def Draw(self, game: Game):
        super().Draw(game)

        font = pygame.font.Font(None, 20)
        game.Settings.GetScreen().blit(font.render("Default", True, Colors.BLACK), (10, 35))

        game.Settings.GetScreen().blit(font.render("Choose an tile or end the turn",
                                                   True, Colors.BLACK), (10, 55))


class UnitActionPanel(ActionPanel):
    def __init__(self, game: Game, tile: Tile = None, endturnButtonRect=None, buttons=None):
        super().__init__(game, tile, endturnButtonRect)
        self.Buttons = buttons if buttons is not None \
            else [ArrowButtonUp(Vector2(0, -40)), ArrowButtonUpRight(Vector2(40, -40)),
                  ArrowButtonRight(Vector2(40, 0)),
                  ArrowButtonDownRight(Vector2(40, 40)), ArrowButtonDown(Vector2(0, 40)),
                  ArrowButtonDownLeft(Vector2(-40, 40)), ArrowButtonLeft(Vector2(-40, 0)),
                  ArrowButtonUpLeft(Vector2(-40, -40))]

    def Update(self, game: Game):
        self.Map = map
        nself = super().Update(game)
        return UnitActionPanel(game, self.Tile, nself.EndturnButtonRect, self.Buttons)

    def Draw(self, game: Game):
        super().Draw(game)

        font = pygame.font.Font(None, 20)
        game.Settings.GetScreen().blit(font.render("Unit actions", True, Colors.BLACK), (10, 35))

        game.Settings.GetScreen().blit(font.render("Choose you actions with the unit",
                                                   True, Colors.BLACK), (10, 55))

        # Draw the Arrow Buttons
        for arrowButton in self.Buttons:
            arrowButton.Draw(game)


class BarrackActionPanel(ActionPanel):

    def __init__(self, game: Game, tile: Tile = None, endturnButtonRect=None, buttons=None):
        super().__init__(game, tile, endturnButtonRect)
        if buttons is not None:
            self.Buttons = buttons
        else:
            import GameLogic.MapHelpers
            self.Buttons = []
            for pos in GameLogic.MapHelpers.getAroundingTiles(tile, game.Logic.Map):
                if pos.Position.X == tile.Position.X+1 and pos.Position.Y == tile.Position.Y:
                    self.Buttons.append(ArrowButtonRight(Vector2(40, 0)))
                elif pos.Position.X == tile.Position.X+1 and pos.Position.Y == tile.Position.Y+1:
                    self.Buttons.append(ArrowButtonDownRight(Vector2(40, 40)))
                elif pos.Position.X == tile.Position.X and pos.Position.Y == tile.Position.Y+1:
                    self.Buttons.append(ArrowButtonDown(Vector2(0, 40)))
                elif pos.Position.X == tile.Position.X-1 and pos.Position.Y == tile.Position.Y+1:
                    self.Buttons.append(ArrowButtonDownLeft(Vector2(-40, 40)))
                elif pos.Position.X == tile.Position.X-1 and pos.Position.Y == tile.Position.Y:
                    self.Buttons.append(ArrowButtonLeft(Vector2(-40, 0)))
                elif pos.Position.X == tile.Position.X-1 and pos.Position.Y == tile.Position.Y-1:
                    self.Buttons.append(ArrowButtonUpLeft(Vector2(-40, -40)))
                elif pos.Position.X == tile.Position.X and pos.Position.Y == tile.Position.Y-1:
                    self.Buttons.append(ArrowButtonUp(Vector2(0, -40)))
                elif pos.Position.X == tile.Position.X+1 and pos.Position.Y == tile.Position.Y-1:
                    self.Buttons.append(ArrowButtonUpRight(Vector2(40, -40)))

    def Update(self, game: Game):
        nself = super().Update(game)
        return BarrackActionPanel(game, self.Tile, nself.EndturnButtonRect)

    def Draw(self, game: Game):
        super().Draw(game)

        font = pygame.font.Font(None, 20)
        game.Settings.GetScreen().blit(font.render("Barrak actions", True, Colors.BLACK), (10, 35))

        game.Settings.GetScreen().blit(font.render("Choose you actions with the Barrak",
                                                   True, Colors.BLACK), (10, 55))

        # Draw the Arrow Buttons
        for arrowButton in self.Buttons:
            arrowButton.Draw(game)


class InfoActionTile(ActionPanel):
    def Update(self, game: Game):
        nself = super().Update(game)
        return InfoActionTile(game, self.Tile, nself.EndturnButtonRect)

    def Draw(self, game: Game):
        super().Draw(game)

        font = pygame.font.Font(None, 20)
        game.Settings.GetScreen().blit(font.render("Tile Info", True, Colors.BLACK), (10, 35))

        game.Settings.GetScreen().blit(font.render("Here you can find info about the tile",
                                                   True, Colors.BLACK), (10, 55))
