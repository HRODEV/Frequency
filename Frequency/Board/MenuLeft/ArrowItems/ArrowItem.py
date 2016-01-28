import pygame
from pygame.surface import Surface

import Vector2
from Helpers.EventHelpers import EventExist

class ArrowItem:
    def __init__(self, offset: Vector2, image: Surface, hover: Surface=None, rect=None):
        self.Offset = offset
        self.Image = image
        self.Hover = hover
        self.Rect = rect

    def Update(self, game):
        return self

    def Draw(self, game):
        # Extra screen-based properties
        menuLeft_centerX = game.Settings.MenuLeftSize.X // 2
        menuLeft_centerY = game.Settings.MenuLeftSize.Y // 2

        x = menuLeft_centerX - self.Image.get_rect().centerx + self.Offset.X
        y = menuLeft_centerY - self.Image.get_rect().centery + self.Offset.Y

        if self.Hover is not None and self.IsHoverdByMouse():
            self.Rect = game.Settings.GetScreen().blit(self.Hover, (x, y))
        else:
            self.Rect = game.Settings.GetScreen().blit(self.Image, (x, y))

    def IsHoverdByMouse(self):
        return self.Rect is not None and self.Rect.collidepoint(pygame.mouse.get_pos())

    def IsClickedByMouse(self, game):
        return self.IsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)

    def GetNewState(self):
        return None