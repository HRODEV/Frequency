import pygame
from pygame.surface import Surface

from Helpers.EventHelpers import EventExist
from Vector2 import Vector2


class ArrowItem:
    def __init__(self, offset: Vector2, image: Surface = None, hover: Surface = None, rect=None):
        self.Offset = offset
        self.Image = image if image is not None else self._getTexture()
        self.Hover = hover if hover is not None else self._getHoverTexture()
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

    def _getTexture(self):
        return None

    def _getHoverTexture(self):
        return None

    def GetDestinationPosition(self, pos: Vector2):
        return pos


class ArrowButtonUp(ArrowItem):
    def _getTexture(self):
        return pygame.image.load('images/arrows/ArrowDarkUp.png').convert_alpha()

    def _getHoverTexture(self):
        return pygame.image.load('images/arrows/ArrowLightUp.png').convert_alpha()

    def GetDestinationPosition(self, pos: Vector2):
        return Vector2(pos.X, pos.Y - 1)


class ArrowButtonUpRight(ArrowItem):
    def _getTexture(self):
        return pygame.image.load('images/arrows/ArrowDarkUpRight.png').convert_alpha()

    def _getHoverTexture(self):
        return pygame.image.load('images/arrows/ArrowLightUpRight.png').convert_alpha()

    def GetDestinationPosition(self, pos: Vector2):
        return Vector2(pos.X + 1, pos.Y - 1)


class ArrowButtonRight(ArrowItem):
    def _getTexture(self):
        return pygame.image.load('images/arrows/ArrowDarkRight.png').convert_alpha()

    def _getHoverTexture(self):
        return pygame.image.load('images/arrows/ArrowLightRight.png').convert_alpha()

    def GetDestinationPosition(self, pos: Vector2):
        return Vector2(pos.X + 1, pos.Y)


class ArrowButtonDownRight(ArrowItem):
    def _getTexture(self):
        return pygame.image.load('images/arrows/ArrowDarkDownRight.png').convert_alpha()

    def _getHoverTexture(self):
        return pygame.image.load('images/arrows/ArrowLightDownRight.png').convert_alpha()

    def GetDestinationPosition(self, pos: Vector2):
        return Vector2(pos.X + 1, pos.Y + 1)


class ArrowButtonDown(ArrowItem):
    def _getTexture(self):
        return pygame.image.load('images/arrows/ArrowDarkDown.png').convert_alpha()

    def _getHoverTexture(self):
        return pygame.image.load('images/arrows/ArrowLightDown.png').convert_alpha()

    def GetDestinationPosition(self, pos: Vector2):
        return Vector2(pos.X, pos.Y + 1)


class ArrowButtonDownLeft(ArrowItem):
    def _getTexture(self):
        return pygame.image.load('images/arrows/ArrowDarkDownLeft.png').convert_alpha()

    def _getHoverTexture(self):
        return pygame.image.load('images/arrows/ArrowLightDownLeft.png').convert_alpha()

    def GetDestinationPosition(self, pos: Vector2):
        return Vector2(pos.X - 1, pos.Y + 1)


class ArrowButtonLeft(ArrowItem):
    def _getTexture(self):
        return pygame.image.load('images/arrows/ArrowDarkLeft.png').convert_alpha()

    def _getHoverTexture(self):
        return pygame.image.load('images/arrows/ArrowLightLeft.png').convert_alpha()

    def GetDestinationPosition(self, pos: Vector2):
        return Vector2(pos.X - 1, pos.Y)


class ArrowButtonUpLeft(ArrowItem):
    def _getTexture(self):
        return pygame.image.load('images/arrows/ArrowDarkUpLeft.png').convert_alpha()

    def _getHoverTexture(self):
        return pygame.image.load('images/arrows/ArrowLightUpLeft.png').convert_alpha()

    def GetDestinationPosition(self, pos: Vector2):
        return Vector2(pos.X - 1, pos.Y - 1)
