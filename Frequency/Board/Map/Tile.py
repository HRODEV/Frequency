import pygame

import GameLogic.Map
import GameLogic.Unit
from Board.Buildings.Base import Base
from Board.Buildings.Building import Building
from Helpers.EventHelpers import EventExist
from Board.Unit import Soldier, Robot, Tank, Boat, UnitGroup
from Board.Buildings.Barrack import Barracks
from Vector2 import Vector2


class Tile:

    def __init__(self, position, size, logicTile, texture=None, rectangle=None, selected=False, unit=None):
        self.Position = position
        self.Size = size
        self.Texture = texture if texture is not None else self._getTexture(size)
        self.Rectangle = rectangle

        self._logicTile = logicTile
        self.Selected = selected

        self._unit = unit if unit is not None and unit.LogicUnit == self.LogicTile.Unit \
            else self._getPossibleUnit()
        self._building = self._getPossibleBuilding()

    def _getPossibleBuilding(self) -> Building:
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

    def _getPossibleUnit(self):
        if self._logicTile.Unit is not None:
            import GameLogic.Unit
            logical_unit = self._logicTile.Unit
            if type(logical_unit) is GameLogic.Unit.Soldier:
                return Soldier(logical_unit.Owner, self, self.Size.X, logical_unit)
            elif type(logical_unit) is GameLogic.Unit.Boat:
                return Boat(logical_unit.Owner, self, self.Size.X, logical_unit)
            elif type(logical_unit) is GameLogic.Unit.Robot:
                return Robot(logical_unit.Owner, self, self.Size.X, logical_unit)
            elif type(logical_unit) is GameLogic.Unit.Tank:
                return Tank(logical_unit.Owner, self, self.Size.X, logical_unit)
            elif type(logical_unit) is GameLogic.Unit.UnitGroup:
                return UnitGroup(logical_unit.Owner, self, self.Size.X, logical_unit)
        else:
            return None


    @property
    def LogicTile(self) -> GameLogic.Map.Tile:
        return self._logicTile

    def Update(self, game):
        return type(self)(self.Position, self.Size, self.LogicTile, self.Texture, self.Rectangle,
                          self.Selected, self._unit)

    def Draw(self, game):
        screen = game.Settings.GetScreen()
        marginX = self.Position.X * self.Size.X + game.Settings.MenuLeftSize.X
        marginY = self.Position.Y * self.Size.Y
        self.Rectangle = screen.blit(self.Texture, (marginX, marginY))
        if self.Selected:  # TODO draw a rectangle with pygame
            screen.blit(pygame.transform.scale(pygame.image.load('images/tiles/selected.png').convert_alpha(), [self.Size.X, self.Size.Y]),(marginX, marginY))
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
