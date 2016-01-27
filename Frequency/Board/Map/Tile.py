import pygame
from Helpers.EventHelpers import EventExist
from Board.Units.Soldier import *


class Tile:

    def __init__(self, position, defaultMoney, enemyMoney, texture, size, units=None, rectangle=None):
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


    def Update(self, game):
        if self.IsClickedByMouse(game):
            if game.Logic.CanAddUnitToTile(game):
                self.Units.append(Soldier(game.Logic.PlayingPlayer, self))

        return Tile(self.Position, self.DefaultMoney, self.EnemyMoney, self.Texture, self.Size, self.Units, self.Rectangle)


    def Draw(self, game):
        screen = game.Settings.GetScreen()
        marginX = self.Position.X * self.Size.X + game.Settings.MenuLeftSize.X
        marginY = self.Position.Y * self.Size.Y
        self.Rectangle = screen.blit(self.Texture, (marginX, marginY))

        if len(self.Units) > 0:
            for unit in self.Units:
                unit.Draw(game)


    def IsHoverdByMouse(self):
        return self.Rectangle is not None and self.Rectangle.collidepoint(pygame.mouse.get_pos())


    def IsClickedByMouse(self, game):
        return self.IsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)