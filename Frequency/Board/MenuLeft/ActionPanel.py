import pygame

import Game
from GameLogic.Map import Tile
from Board.MenuLeft.ArrowItem import *
from Board.MenuLeft.BuyUnitItems import *
from GameLogic.Unit import Soldier
from Helpers import Colors
from Helpers.EventHelpers import EventExist
from Vector2 import Vector2


class ActionPanel:
    def __init__(self, game: Game, tile: Tile = None, endturnButtonRect=None, newSelection=None):
        self.Size = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2,
                            game.Settings.Resolution.Y)
        self.Position = Vector2(0, 0)
        self.Tile = tile
        self.EndturnButtonRect = endturnButtonRect
        self.NewSelection = newSelection

        self.Map = None
        self.EndTurnButtonImage = pygame.transform.scale(
            pygame.image.load('images/buttons/endturnButton.png').convert_alpha(), [150, 25])
        # TODO netter als je deze verantwoordelijkheid geeft bij het object die dit object beheert
        game.Settings.SetMenuLeftSize(self.Size)

    def Update(self, game: Game) -> 'ActionPanel':
        # End turn
        if self.EndturnButtonIsClickedByMouse(game):
            game.Logic.EndTurn(game)
            return DefaultActionPanel(game)

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
    def __init__(self, game: Game, tile: Tile = None, endturnButtonRect=None, buttons=None, newSelection=None):
        super().__init__(game, tile, endturnButtonRect, newSelection)
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

        if type(nself) is DefaultActionPanel:
            return nself

        clickedButton = next((btn for btn in self.Buttons if btn.IsClickedByMouse(game)), None)
        if clickedButton is not None:
            self.Tile.Unit.MoveTo(game.Logic.Map.GetTile(clickedButton.GetDestinationPosition(self.Tile.Position)))
            return UnitActionPanel(game, self.Tile, nself.EndturnButtonRect, self.Buttons,
                                   clickedButton.GetDestinationPosition(self.Tile.Position))

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

    def __init__(self, game: Game, tile: Tile = None, endturnButtonRect=None, buttons=None, buyUnits=None):
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

        if buyUnits is not None:
            self.BuyUnits = buyUnits
        else:
            self.BuyUnits = []
            self.BuyUnits.append(SoldierButton(Vector2(0, 100)))
            self.BuyUnits.append(RobotButton(Vector2(1, 100)))
            self.BuyUnits.append(TankButton(Vector2(2, 100)))
            self.BuyUnits.append(BoatButton(Vector2(3, 100)))

    def Update(self, game: Game):
        nself = super().Update(game)

        if type(nself) is DefaultActionPanel:
            return nself

        clickedButton = next((btn for btn in self.Buttons if btn.IsClickedByMouse(game)), None)
        if clickedButton is not None:
            game.Logic.BuyUnit(
                Soldier,
                game.Logic.Map.GetTile(clickedButton.GetDestinationPosition(self.Tile.Position))
            )

        return BarrackActionPanel(game, self.Tile, nself.EndturnButtonRect, self.Buttons, self.BuyUnits)

    def Draw(self, game: Game):
        super().Draw(game)

        font = pygame.font.Font(None, 20)
        game.Settings.GetScreen().blit(font.render("Barrack actions", True, Colors.BLACK), (10, 35))

        game.Settings.GetScreen().blit(font.render("Choose you actions with the Barrack",
                                                   True, Colors.BLACK), (10, 55))

        # Draw the Arrow Buttons
        for arrowButton in self.Buttons:
            arrowButton.Draw(game)

        # Draw the Buy Unit Buttons
        for unitBuyButton in self.BuyUnits:
            unitBuyButton.Draw(game)


class InfoActionTile(ActionPanel):
    def Update(self, game: Game):
        nself = super().Update(game)

        if type(nself) is DefaultActionPanel:
            return nself

        return InfoActionTile(game, self.Tile, nself.EndturnButtonRect)

    def Draw(self, game: Game):
        super().Draw(game)

        font = pygame.font.Font(None, 20)
        game.Settings.GetScreen().blit(font.render("Tile Info", True, Colors.BLACK), (10, 35))

        game.Settings.GetScreen().blit(font.render("Here you can find info about the tile",
                                                   True, Colors.BLACK), (10, 55))
