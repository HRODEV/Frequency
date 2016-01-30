import GameLogic.Map
import GameLogic.Unit
from Board.Buildings.Base import Base
from Board.Buildings.Building import Building
from Helpers.EventHelpers import EventExist
from Board.Units.Soldier import *
from Board.Buildings.Barrack import Barracks
from Vector2 import Vector2


class Tile:

    def __init__(self, position, size, logicTile, texture=None, units=None, rectangle=None, selected=False):
        self.Position = position
        self.Size = size
        self.Texture = texture if texture is not None else self._getTexture(size)
        self.Rectangle = rectangle
        if units is None:
            self.Units = []
        else:
            self.Units = units
        self._logicTile = logicTile
        self.Selected = selected

        self._building = self._getPosibleBuilding()

    def _getPosibleBuilding(self) -> Building:
        if self._logicTile.Building is not None:
            # check type of building
            from GameLogic.Barrack import BaseBarrack, Barrack
            if type(self._logicTile.Building) is BaseBarrack:
                return Base(self._logicTile.Building.Owner, self)
            elif type(self._logicTile.Building) is Barrack:
                return Barracks(self._logicTile.Building.Owner, self)
            else:
                raise Exception("this type is not supported for a building")
        else:
            return None



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

        return type(self)(self.Position, self.Size, self.LogicTile, self.Texture, self.Units, self.Rectangle, self.Selected)

    def Draw(self, game):
        screen = game.Settings.GetScreen()
        marginX = self.Position.X * self.Size.X + game.Settings.MenuLeftSize.X
        marginY = self.Position.Y * self.Size.Y
        if self.Selected:
            testTexture = pygame.transform.scale(pygame.image.load('images/tiles/selected.png').convert_alpha(), [self.Size.X, self.Size.Y])
        else:
            testTexture = self.Texture
        self.Rectangle = screen.blit(testTexture, (marginX, marginY))
        if len(self.Units) > 0:
            # Fake data
            totalUnitsOnTile = 4
            unitList = [self.Units[0], self.Units[0], self.Units[0], self.Units[0]]

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
        if self._building is not None:
            self._building.Draw(game)

    def IsHoverdByMouse(self):
        return self.Rectangle is not None and self.Rectangle.collidepoint(pygame.mouse.get_pos())

    def IsClickedByMouse(self, game):
        return self.IsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)

    def _getTexture(self, size: Vector2):
        return None


class DesertTile(Tile):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/tiles/DesertSeamless.png').convert_alpha(), [size.X, size.Y])


class GoldTile(Tile):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/tiles/GoldSeamless.png').convert_alpha(), [size.X, size.Y])


class ForestTile(Tile):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/tiles/ForestSeamless.png').convert_alpha(), [size.X, size.Y])


class IceTile(Tile):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/tiles/IceSeamless.png').convert_alpha(), [size.X, size.Y])


class SeaTile(Tile):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/tiles/SeaSeamless.png').convert_alpha(), [size.X, size.Y])


class SwampTile(Tile):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/tiles/SwampSeamless.png').convert_alpha(), [size.X, size.Y])
