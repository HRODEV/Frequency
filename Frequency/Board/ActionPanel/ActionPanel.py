import pygame

import Game
from GameLogic.Map import Tile
from Board.ActionPanel.ArrowItem import *
from Board.ActionPanel.BuyUnitItems import *
from GameLogic.Unit import Soldier
from GameLogic.UnitFactory import getUnitPrice
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


class SimpleTextButton:

    def __init__(self, text, position):
        self._text = text
        self._position = position
        self.clicked = False
        self.rect = None

    def Draw(self, screen):
        font = pygame.font.Font(None, 20)
        textColor = Colors.RED if self.clicked else Colors.BLACK

        if self.IsHoverdByMouse():
            self.rect = screen.blit(font.render(self._text, True, textColor, Colors.DIMGREY), self._position)
        else:
            self.rect = screen.blit(font.render(self._text, True, textColor), self._position)

    def IsHoverdByMouse(self):
        return self.rect is not None and self.rect.collidepoint(pygame.mouse.get_pos())

    def IsClickedByMouse(self, game):
        return self.IsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)


class UnitActionPanel(ActionPanel):
    def __init__(self, game: Game, tile: Tile = None, endturnButtonRect=None, buttons=None, newSelection=None,
                 _barackButton=None, _moveButton=None, _moveUnitFromBoatButton=None):
        super().__init__(game, tile, endturnButtonRect, newSelection)
        self._barrackButton = _barackButton if _barackButton is not None else SimpleTextButton("Buy Barrack", (10, 100))
        if _moveButton is not None:
            self._moveButton = _moveButton
        else:
            self._moveButton = SimpleTextButton("Move Unit", (10, 130))
            self._moveButton.clicked = True
        self._moveUnitFromBoatButton = _moveUnitFromBoatButton if _moveUnitFromBoatButton is not None \
            else SimpleTextButton("move Unit to land", (10, 160))
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

        if self._barrackButton.IsClickedByMouse(game) or self._moveButton.IsClickedByMouse(game) \
                or self._moveUnitFromBoatButton.IsClickedByMouse(game):

            if self._moveButton.IsClickedByMouse(game):
                self._moveButton.clicked = True
                self._barrackButton.clicked = False
                self._moveUnitFromBoatButton.clicked = False
            elif self._barrackButton.IsClickedByMouse(game):
                self._barrackButton.clicked = True
                self._moveButton.clicked = False
                self._moveUnitFromBoatButton.clicked = False
            else:
                self._moveUnitFromBoatButton.clicked = True
                self._barrackButton.clicked = False
                self._moveButton.clicked = False

        clickedButton = next((btn for btn in self.Buttons if btn.IsClickedByMouse(game)), None)
        if self._moveButton.clicked:
            if clickedButton is not None:
                self.Tile.Unit.MoveTo(game.Logic.Map.GetTile(clickedButton.GetDestinationPosition(self.Tile.Position)))
                return UnitActionPanel(game, self.Tile, nself.EndturnButtonRect, None,
                                       clickedButton.GetDestinationPosition(self.Tile.Position))

        elif self._barrackButton.clicked:
            if clickedButton is not None:
                game.Logic.BuyBarrack(game.Logic.Map.GetTile(clickedButton.GetDestinationPosition(self.Tile.Position)))
                return BarrackActionPanel(game, game.Logic.Map.GetTile(clickedButton.GetDestinationPosition(self.Tile.Position)))
        else:
            if clickedButton is not None:
                self.Tile.Unit.Unit.MoveTo(game.Logic.Map.GetTile(clickedButton.GetDestinationPosition(self.Tile.Position)))
                self.Tile.Unit.Unit = None
                return UnitActionPanel(game, self.Tile, nself.EndturnButtonRect, None,
                                       clickedButton.GetDestinationPosition(self.Tile.Position))


        return UnitActionPanel(game, self.Tile, nself.EndturnButtonRect, self.Buttons, None, self._barrackButton,
                               self._moveButton, self._moveUnitFromBoatButton)

    def Draw(self, game: Game):
        super().Draw(game)

        screen = game.Settings.GetScreen()
        font = pygame.font.Font(None, 20)
        game.Settings.GetScreen().blit(font.render("Unit actions", True, Colors.BLACK), (10, 35))

        screen.blit(font.render("Choose you actions with the unit",
                                                   True, Colors.BLACK), (10, 55))

        screen.blit(font.render("defense points: %i" % self.Tile.Unit.DefencePoints, True, Colors.BLACK), (10, 190))
        screen.blit(font.render("attack points: %i" % self.Tile.Unit.AttackPoints, True, Colors.BLACK), (10, 210))

        # choose between buy a barrack or move the unit
        self._barrackButton.Draw(screen)
        self._moveButton.Draw(screen)
        if type(self.Tile.Unit) is Boat:
            self._moveUnitFromBoatButton.Draw(screen)

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
            self.BuyUnits.append(SoldierButton(Vector2(0, 100), game.Logic.PlayingPlayer.Character.Id))
            self.BuyUnits.append(RobotButton(Vector2(1, 100), game.Logic.PlayingPlayer.Character.Id))
            self.BuyUnits.append(TankButton(Vector2(2, 100), game.Logic.PlayingPlayer.Character.Id))
            self.BuyUnits.append(BoatButton(Vector2(3, 100), game.Logic.PlayingPlayer.Character.Id))

    def Update(self, game: Game):
        nself = super().Update(game)

        if type(nself) is DefaultActionPanel:
            return nself

        clickedArrowButton = next((btn for btn in self.Buttons if btn.IsClickedByMouse(game)), None)
        clickedUnitButton = next((btn for btn in self.BuyUnits if btn.IsClickedByMouse(game)), None)

        if clickedUnitButton is not None:
            for btn in self.BuyUnits:
                btn.clicked = False
            clickedUnitButton.clicked = True

        clickedUnitButton = next((btn for btn in self.BuyUnits if btn.clicked), None)
        if clickedUnitButton is not None and clickedArrowButton is not None:

            game.Logic.BuyUnit(
                clickedUnitButton.GetUnitType(),
                game.Logic.Map.GetTile(clickedArrowButton.GetDestinationPosition(self.Tile.Position))
            )

        return BarrackActionPanel(game, self.Tile, nself.EndturnButtonRect, self.Buttons, self.BuyUnits)

    def Draw(self, game: Game):
        super().Draw(game)

        screen = game.Settings.GetScreen()

        font = pygame.font.Font(None, 20)
        screen.blit(font.render("Barrack actions", True, Colors.BLACK), (10, 35))

        screen.blit(font.render("Choose you actions with the Barrack",
                                                   True, Colors.BLACK), (10, 55))

        # Draw the Arrow Buttons
        for arrowButton in self.Buttons:
            arrowButton.Draw(game)

        # Draw the Buy Unit Buttons
        for unitBuyButton in self.BuyUnits:
            unitBuyButton.Draw(game)

        # Draw the price of the units
        #Soldier
        screen.blit(font.render('ƒ '+str(getUnitPrice(Soldier, self.Tile.Building.Owner.Character)),
                                                   True, Colors.BLACK), (15, 150))
        #Robot
        screen.blit(font.render('ƒ '+str(getUnitPrice(Robot, self.Tile.Building.Owner.Character)),
                                                   True, Colors.BLACK), (73, 150))
        #Tank
        screen.blit(font.render('ƒ '+str(getUnitPrice(Tank, self.Tile.Building.Owner.Character)),
                                                   True, Colors.BLACK), (131, 150))
        #Boat
        screen.blit(font.render('ƒ '+str(getUnitPrice(Boat, self.Tile.Building.Owner.Character)),
                                                   True, Colors.BLACK), (189, 150))


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
