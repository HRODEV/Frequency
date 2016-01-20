import pygame
from pygame.surface import Surface

import Vector2


class StartMenuItem:
    def __init__(self, offset: Vector2, image: Surface, rect):
        self.Image = image
        self.Offset = offset
        self.Rect = rect

    def Update(self, game, events):
        return self

    def Draw(self, game):
        # Extra screen-based properties
        screen_centerX = game.Settings.Resolution.X // 2
        screen_centerY = game.Settings.Resolution.Y // 2

        x = screen_centerX - self.Image.get_rect().centerx + self.Offset.X
        y = screen_centerY + 20 + self.Offset.Y

        self.Rect = game.Settings.GetScreen().blit(self.Image, (x, y))


    def IsHoverdByMouse(self):
        return self.Rect is not None and self.Rect.collidepoint(pygame.mouse.get_pos())

    '''def IsClickedByMouse(self):
        return self.IsHoverdByMouse() and #check events'''

