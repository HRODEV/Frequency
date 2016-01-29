import pygame

import Game
from Board.Map.Tile import Tile
from Helpers import Colors
from Helpers.EventHelpers import EventExist
from Vector2 import Vector2

from Board.MenuLeft.ArrowItems.ArrowItem import ArrowButtonUp
from Board.MenuLeft.ArrowItems.ArrowItem import ArrowButtonUpRight
from Board.MenuLeft.ArrowItems.ArrowItem import ArrowButtonRight
from Board.MenuLeft.ArrowItems.ArrowItem import ArrowButtonDownRight
from Board.MenuLeft.ArrowItems.ArrowItem import ArrowButtonDown
from Board.MenuLeft.ArrowItems.ArrowItem import ArrowButtonDownLeft
from Board.MenuLeft.ArrowItems.ArrowItem import ArrowButtonLeft
from Board.MenuLeft.ArrowItems.ArrowItem import ArrowButtonUpLeft


class ActionPanel:
    def __init__(self, game: Game, tile: Tile=None, endturnButtonRect=None, arrowButtons=None):
        self.Size = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2, game.Settings.Resolution.Y)
        self.Position = Vector2(0, 0)
        self.Tile = tile
        self.EndturnButtonRect = endturnButtonRect

        self.ArrowBtnUp = None
        self.ArrowBtnUpRight = None
        self.ArrowBtnRight = None
        self.ArrowBtnDownRight = None
        self.ArrowBtnDown = None
        self.ArrowBtnDownLeft = None
        self.ArrowBtnLeft = None
        self.ArrowBtnUpLeft = None

        self.Map = None
        self.EndTurnButtonImage = pygame.transform.scale(pygame.image.load('images/buttons/endturnButton.png').convert_alpha(), [150, 25])
        # TODO netter als je deze verantwoordelijkheid geeft bij het object die dit object beheert
        game.Settings.SetMenuLeftSize(self.Size)

    def Update(self, game: Game) -> 'ActionPanel':
        # End turn
        if self.EndturnButtonIsClickedByMouse(game):
            game.Logic.EndTurn(game)

        # Movement
        if self.ArrowBtnUp.IsClickedByMouse(game):
           self.Map.MoveUnit(1, game)
        elif self.ArrowBtnUpRight.IsClickedByMouse(game):
            self.Map.MoveUnit(2, game)
        elif self.ArrowBtnRight.IsClickedByMouse(game):
            self.Map.MoveUnit(3, game)
        elif self.ArrowBtnDownRight.IsClickedByMouse(game):
            self.Map.MoveUnit(4, game)
        elif self.ArrowBtnDown.IsClickedByMouse(game):
            self.Map.MoveUnit(5, game)
        elif self.ArrowBtnDownLeft.IsClickedByMouse(game):
            self.Map.MoveUnit(6, game)
        elif self.ArrowBtnLeft.IsClickedByMouse(game):
            self.Map.MoveUnit(7, game)
        elif self.ArrowBtnUpLeft.IsClickedByMouse(game):
            self.Map.MoveUnit(8, game)

        return ActionPanel(game, self.Tile, self.EndturnButtonRect)

    def Draw(self, game: Game):
        font = pygame.font.Font(None, 30)
        font.set_bold(True)
        # Draw the background
        pygame.draw.rect(game.Settings.GetScreen(), Colors.WHITE, (self.Position.X, self.Position.Y, self.Size.X, self.Size.Y))

        game.Settings.GetScreen().blit(font.render("Action panel", True, Colors.BLACK), (10,10))

        # Draw end turn button
        self.EndturnButtonRect = game.Settings.GetScreen().blit(self.EndTurnButtonImage, (10, game.Settings.Resolution.Y-50))

    def IsHoverdByMouse(btn):
        return btn is not None and self.Rect.collidepoint(pygame.mouse.get_pos())

    def IsClickedByMouse(btn, game):
        return btn.IsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)

    def EndturnButtonIsHoverdByMouse(self):
        return self.EndturnButtonRect is not None and self.EndturnButtonRect.collidepoint(pygame.mouse.get_pos())

    def EndturnButtonIsClickedByMouse(self, game):
        return self.EndturnButtonIsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)

class DefaultActionPanel(ActionPanel):

    def Update(self, game: Game):
        nself = super().Update(game)
        DefaultActionPanel(game, self.Tile, nself.EndturnButtonRect)

    def Draw(self, game : Game):
        super().Draw(game)

        font = pygame.font.Font(None, 20)
        game.Settings.GetScreen().blit(font.render("Default", True, Colors.BLACK), (10, 35))

        game.Settings.GetScreen().blit(font.render("Choose an tile or end the turn",
                                                   True, Colors.BLACK), (10, 55))


class UnitActionPanel(ActionPanel):

    def Update(self, game: Game, map):
        self.Map = map
        nself = super().Update(game)
        UnitActionPanel(game, self.Tile, nself.EndturnButtonRect)

    def Draw(self, game : Game):
        super().Draw(game)

        font = pygame.font.Font(None, 20)
        game.Settings.GetScreen().blit(font.render("Unit actions", True, Colors.BLACK), (10, 35))

        game.Settings.GetScreen().blit(font.render("Choose you actions with the unit",
                                                   True, Colors.BLACK), (10, 55))

        # Draw the Arrow Buttons
        self.ArrowBtnUp = ArrowButtonUp(Vector2(0, -40))
        self.ArrowBtnUp.Draw(game)
        self.ArrowBtnUpRight = ArrowButtonUpRight(Vector2(40, -40))
        self.ArrowBtnUpRight.Draw(game)
        self.ArrowBtnRight = ArrowButtonRight(Vector2(40,0))
        self.ArrowBtnRight.Draw(game)
        self.ArrowBtnDownRight = ArrowButtonDownRight(Vector2(40, 40))
        self.ArrowBtnDownRight.Draw(game)
        self.ArrowBtnDown = ArrowButtonDown(Vector2(0, 40))
        self.ArrowBtnDown.Draw(game)
        self.ArrowBtnDownLeft = ArrowButtonDownLeft(Vector2(-40, 40))
        self.ArrowBtnDownLeft.Draw(game)
        self.ArrowBtnLeft = ArrowButtonLeft(Vector2(-40, 0))
        self.ArrowBtnLeft.Draw(game)
        self.ArrowBtnUpLeft = ArrowButtonUpLeft(Vector2(-40, -40))
        self.ArrowBtnUpLeft.Draw(game)

class BarrakActionPanel(ActionPanel):

    def Update(self, game: Game):
        nself = super().Update(game)
        BarrakActionPanel(game, self.Tile, nself.EndturnButtonRect)

    def Draw(self, game : Game):
        super().Draw(game)

        font = pygame.font.Font(None, 20)
        game.Settings.GetScreen().blit(font.render("Barrak actions", True, Colors.BLACK), (10, 35))

        game.Settings.GetScreen().blit(font.render("Choose you actions with the Barrak",
                                                   True, Colors.BLACK), (10, 55))

class InfoActionTile(ActionPanel):

    def Update(self, game: Game):
        nself = super().Update(game)
        InfoActionTile(game, self.Tile, nself.EndturnButtonRect)

    def Draw(self, game : Game):
        super().Draw(game)

        font = pygame.font.Font(None, 20)
        game.Settings.GetScreen().blit(font.render("Tile Info", True, Colors.BLACK), (10, 35))

        game.Settings.GetScreen().blit(font.render("Here you can find info about the tile",
                                                   True, Colors.BLACK), (10, 55))