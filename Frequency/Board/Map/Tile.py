import pygame
from Helpers.EventHelpers import EventExist


class Tile:

    def __init__(self, position, defaultMoney, enemyMoney, texture, size, units=None, rectangle=None):
        self.Position = position
        self.DefaultMoney = defaultMoney
        self.EnemyMoney = enemyMoney
        self.Size = size
        self.Texture = texture
        self.Units = units
        self.Rectangle = rectangle

    def Update(self, game):
        if self.IsClickedByMouse(game):
            print(self.Position.X, self.Position.Y)

        return Tile(self.Position, self.DefaultMoney, self.EnemyMoney, self.Size, self.Texture, self.Units, self.Rectangle)


    def Draw(self, game):
        screen = game.Settings.GetScreen()
        marginX = self.Position.X * self.Size.X
        marginY = self.Position.Y * self.Size.Y

        self.Rectangle = screen.blit(self.Texture, (marginX, marginY))


    def IsHoverdByMouse(self):
        return self.Rectangle is not None and self.Rectangle.collidepoint(pygame.mouse.get_pos())


    def IsClickedByMouse(self, game):
        return self.IsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)
