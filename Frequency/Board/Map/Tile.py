from Helpers.EventHelpers import EventExist
from Board.Units.Soldier import *
from Board.Buildings.Barrack import Barracks

class Tile:

    def __init__(self, position, defaultMoney, enemyMoney, texture, size, units=None, rectangle=None, building=None):
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


    def Update(self, game):
        if self.IsClickedByMouse(game):
            if game.Settings.GetSelectedUnitBuilding() == "Soldier":
                if game.Logic.CanAddUnitBuildingToTile(game):
                    self.Units.append(Soldier(game.Logic.PlayingPlayer, self))
            elif game.Settings.GetSelectedUnitBuilding() == "Barracks":
                 if game.Logic.CanAddUnitBuildingToTile(game):
                    self.Building = Barracks(game.Logic.PlayingPlayer, self)
                    print("place building")

        return Tile(self.Position, self.DefaultMoney, self.EnemyMoney, self.Texture, self.Size, self.Units, self.Rectangle, self.Building)


    def Draw(self, game):
        screen = game.Settings.GetScreen()
        marginX = self.Position.X * self.Size.X + game.Settings.MenuLeftSize.X
        marginY = self.Position.Y * self.Size.Y
        self.Rectangle = screen.blit(self.Texture, (marginX, marginY))
        if len(self.Units) > 0:
            for unit in self.Units:
                unit.Draw(game)
        if self.Building is not None:
            self.Building.Draw(game)


    def IsHoverdByMouse(self):
        return self.Rectangle is not None and self.Rectangle.collidepoint(pygame.mouse.get_pos())


    def IsClickedByMouse(self, game):
        return self.IsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)