import GameLogic.Map
import GameLogic.Unit
from Helpers.EventHelpers import EventExist
from Board.Units.Soldier import *
from Board.Buildings.Barrack import Barracks
from Vector2 import Vector2
from GameLogic.UnitFactory import BuyUnit


class Tile:

    def __init__(self, position, size, logicTile, texture=None, units=None, rectangle=None, building=None, selected=False):
        self.Position = position
        self.Size = size
        self.Texture = texture if texture is not None else self._getTexture(size)
        self.Rectangle = rectangle
        if units is None:
            self.Units = []
        else:
            self.Units = units
        self.Building = building
        self._logicTile = logicTile
        self.Selected = selected

    @property
    def LogicTile(self) -> GameLogic.Map.Tile:
        return self._logicTile

    def Update(self, game):
        if self.IsClickedByMouse(game):
            if game.Settings.GetSelectedUnitBuilding() == "Soldier":
                logicSoldier = game.Logic.BuyUnit(GameLogic.Unit.Soldier, self.LogicTile)
                if logicSoldier is not None:
                    self.Units.append(Soldier(game.Logic.PlayingPlayer, self, logicSoldier))
            elif game.Settings.GetSelectedUnitBuilding() == "Barracks":
                if game.Logic.CanAddUnitBuildingToTile(game, self):
                    self.Building = Barracks(game.Logic.PlayingPlayer, self)
            self.Selected = True

        return type(self)(self.Position, self.Size, self.LogicTile, self.Texture, self.Units, self.Rectangle, self.Building, self.Selected)

    def Draw(self, game):
        screen = game.Settings.GetScreen()
        marginX = self.Position.X * self.Size.X + game.Settings.MenuLeftSize.X
        marginY = self.Position.Y * self.Size.Y
        if self.Selected:
            testTexture = pygame.transform.scale(pygame.image.load('images/tiles/selected.png'), [self.Size.X, self.Size.Y])
        else:
            testTexture = self.Texture
        self.Rectangle = screen.blit(testTexture, (marginX, marginY))
        if len(self.Units) > 0:
            # Fake data
            totalUnitsOnTile = 4
            unitList = []
            unitList.append(self.Units[0])
            unitList.append(self.Units[0])
            unitList.append(self.Units[0])
            unitList.append(self.Units[0])

            i = 0
            if totalUnitsOnTile > 1:
                size = min(self.Size.X // 2, self.Size.Y // 2)
            else:
                size = min(self.Size.X, self.Size.Y)

            for unit in unitList:
                if totalUnitsOnTile > 1:
                    if i == 0:
                        position = Vector2(self.Position.X * self.Size.X, self.Position.Y * self.Size.Y)
                    if i == 1:
                        position = Vector2(self.Position.X * self.Size.X + self.Size.X / 2, self.Position.Y * self.Size.Y)
                    if i == 2:
                        position = Vector2(self.Position.X * self.Size.X, self.Position.Y * self.Size.Y + self.Size.Y / 2)
                    if i == 3:
                        position = Vector2(self.Position.X * self.Size.X + self.Size.X / 2, self.Position.Y * self.Size.Y + self.Size.Y / 2)
                else:
                     position = Vector2(self.Position.X * self.Size.X, self.Position.Y * self.Size.Y)

                unit.Draw(game, self, size, position)
                i += 1
        if self.Building is not None:
            self.Building.Draw(game)

    def IsHoverdByMouse(self):
        return self.Rectangle is not None and self.Rectangle.collidepoint(pygame.mouse.get_pos())

    def IsClickedByMouse(self, game):
        return self.IsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)

    def _getTexture(self, size: Vector2):
        return None


class DesertTile(Tile):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/tiles/DesertSeamless.png'), [size.X, size.Y])


class GoldTile(Tile):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/tiles/GoldSeamless.png'), [size.X, size.Y])


class ForestTile(Tile):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/tiles/ForestSeamless.png'), [size.X, size.Y])


class IceTile(Tile):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/tiles/IceSeamless.png'), [size.X, size.Y])


class SeaTile(Tile):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/tiles/SeaSeamless.png'), [size.X, size.Y])


class SwampTile(Tile):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/tiles/SwampSeamless.png'), [size.X, size.Y])
