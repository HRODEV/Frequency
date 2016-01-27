import GameLogic.Map
from Helpers.EventHelpers import EventExist
from Board.Units.Soldier import *
from Board.Buildings.Barrack import Barracks
from Vector2 import Vector2


class Tile:

    def __init__(self, position, defaultMoney, enemyMoney, texture, size, units, rectangle, building, logicTile):
        self.Position = position
        self.DefaultMoney = defaultMoney
        self.EnemyMoney = enemyMoney
        self.Size = size
        self.Texture = texture
        self.Rectangle = rectangle
        if units is None:
            self.Units = []
        else:
            self.Units = units
        self.Building = building
        self._logicTile = logicTile

    @property
    def LogicTile(self) -> GameLogic.Map.Tile:
        return self._logicTile

    def Update(self, game):
        if self.IsClickedByMouse(game):
            if game.Settings.GetSelectedUnitBuilding() == "Soldier":
                if game.Logic.CanAddUnitBuildingToTile(game, self):
                    self.Units.append(Soldier(game.Logic.PlayingPlayer, self))
                    game.Logic.PlayingPlayer.Money -= 100
            elif game.Settings.GetSelectedUnitBuilding() == "Barracks":
                 if game.Logic.CanAddUnitBuildingToTile(game, self):
                    self.Building = Barracks(game.Logic.PlayingPlayer, self)

        return type(self)(self.Position, self.Size, self.LogicTile, self.Texture, self.Units, self.Rectangle, self.Building)

    def Draw(self, game):
        screen = game.Settings.GetScreen()
        marginX = self.Position.X * self.Size.X + game.Settings.MenuLeftSize.X
        marginY = self.Position.Y * self.Size.Y
        self.Rectangle = screen.blit(self.Texture, (marginX, marginY))
        if len(self.Units) > 0:
            for unit in self.Units:
                unit.Draw(game, self)
        if self.Building is not None:
            self.Building.Draw(game)

    def IsHoverdByMouse(self):
        return self.Rectangle is not None and self.Rectangle.collidepoint(pygame.mouse.get_pos())

    def IsClickedByMouse(self, game):
        return self.IsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)


class DesertTile(Tile):

    def __init__(self, position: Vector2, size: Vector2, logicTile, texture=None, units=None, rectangle=None, building=None):
        texture = texture if texture is not None else pygame.transform.scale(pygame.image.load('images/tiles/DesertSeamless.png'), [size.X, size.Y])
        super().__init__(position, 50, 100, texture, size, units, rectangle, building, logicTile)


class GoldTile(Tile):

    def __init__(self, position: Vector2, size: Vector2, logicTile, texture=None, units=None, rectangle=None, building=None):
        texture = texture if texture is not None else pygame.transform.scale(pygame.image.load('images/tiles/GoldSeamless.png'), [size.X, size.Y])
        super().__init__(position, 50, 100, texture, size, units, rectangle, building, logicTile)


class ForestTile(Tile):

    def __init__(self, position: Vector2, size: Vector2, logicTile, texture=None, units=None, rectangle=None, building=None):
        texture = texture if texture is not None else pygame.transform.scale(pygame.image.load('images/tiles/ForestSeamless.png'), [size.X, size.Y])
        super().__init__(position, 50, 100, texture, size, units, rectangle, building, logicTile)


class IceTile(Tile):

    def __init__(self, position: Vector2, size: Vector2, logicTile, texture=None, units=None, rectangle=None, building=None):
        texture = texture if texture is not None else pygame.transform.scale(pygame.image.load('images/tiles/IceSeamless.png'), [size.X, size.Y])
        super().__init__(position, 50, 100, texture, size, units, rectangle, building, logicTile)



class SeaTile(Tile):
    def __init__(self, position: Vector2, size: Vector2, logicTile, texture=None, units=None, rectangle=None, building=None):
        texture = texture if texture is not None else pygame.transform.scale(pygame.image.load('images/tiles/SeaSeamless.png'), [size.X, size.Y])
        super().__init__(position, 50, 100, texture, size, units, rectangle, building, logicTile)


class SwampTile(Tile):
    def __init__(self, position: Vector2, size: Vector2, logicTile, texture=None, units=None, rectangle=None, building=None):
        texture = texture if texture is not None else pygame.transform.scale(pygame.image.load('images/tiles/SwampSeamless.png'), [size.X, size.Y])
        super().__init__(position, 50, 100, texture, size, units, rectangle, building, logicTile)
