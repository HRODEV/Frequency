import pygame
from pygame.surface import Surface

import Vector2
from Helpers.EventHelpers import EventExist

class ArrowItem:
    def __init__(self, offset: Vector2, image: Surface, hover: Surface=None, rect=None):
        self.Offset = offset
        self.Image = image if image is not None else self._getTexture()
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

    def _getTexture(self, size: Vector2):
        return None

class ArrowButtonUp(ArrowItem):

    def _getTexture():
        return pygame.image.load('images/arrows/ArrowDarkUp.png')

    def _getHoverTexture():
        return pygame.image.load('images/arrows/ArrowLightUp.png')


class ArrowButtonUpRight(ArrowItem):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/arrows/ArrowDarkUpRight.png'), [size.X, size.Y])


class ArrowButtonRight(ArrowItem):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/arrows/ArrowDarkRight.png'), [size.X, size.Y])


class ArrowButtonDownRight(ArrowItem):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/arrows/ArrowDarkDownRight.png'), [size.X, size.Y])


class ArrowButtonDown(ArrowItem):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/arrows/ArrowDarkDown.png'), [size.X, size.Y])


class ArrowButtonDownLeft(ArrowItem):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/arrows/ArrowDarkDownLeft.png'), [size.X, size.Y])


class ArrowButtonLeft(ArrowItem):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/arrows/ArrowDarkLeft.png'), [size.X, size.Y])


class ArrowButtonUpLeft(ArrowItem):

    def _getTexture(self, size: Vector2):
        return pygame.transform.scale(pygame.image.load('images/arrows/ArrowDarkUpLeft.png'), [size.X, size.Y])