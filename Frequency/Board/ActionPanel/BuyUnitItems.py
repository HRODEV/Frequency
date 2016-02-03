import pygame
from pygame.surface import Surface

from GameLogic.Unit import *
from Helpers.EventHelpers import EventExist
from Vector2 import Vector2


class BuyUnitItem:
    def __init__(self, offset: Vector2, id, image: Surface = None, rect=None):
        self.Offset = offset
        self.Image = image if image is not None else self._getTexture(id)
        self.Rect = rect
        self.clicked = False

    def Update(self, game):
        return self

    def Draw(self, game):
        # Extra screen-based properties

        margin = 38 + 20

        x = 10 + margin * self.Offset.X
        y = self.Offset.Y

        if self.IsHoverdByMouse() or self.clicked:
            game.Settings.GetScreen().blit(
                pygame.transform.scale(pygame.image.load('images/tiles/selected.png').convert_alpha(), (40, 40)),
                (x, y))

        self.Rect = game.Settings.GetScreen().blit(self.Image, (x, y))

    def IsHoverdByMouse(self):
        return self.Rect is not None and self.Rect.collidepoint(pygame.mouse.get_pos())

    def IsClickedByMouse(self, game):
        return self.IsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)

    def _getTexture(self, id):
        return None

    def GetUnitType(self):
        return Soldier


class SoldierButton(BuyUnitItem):
    def _getTexture(self, id):
        if id == 0:
            return pygame.transform.scale(pygame.image.load('images/units/soldierGreen.png').convert_alpha(), (38, 38))
        elif id == 1:
            return pygame.transform.scale(pygame.image.load('images/units/soldierBlue.png').convert_alpha(), (38, 38))
        elif id == 2:
            return pygame.transform.scale(pygame.image.load('images/units/soldierYellow.png').convert_alpha(), (38, 38))
        else:
            return pygame.transform.scale(pygame.image.load('images/units/soldierRed.png').convert_alpha(), (38, 38))

    def GetUnitType(self):
        return Soldier


class RobotButton(BuyUnitItem):
    def _getTexture(self, id):
        if id == 0:
            return pygame.transform.scale(pygame.image.load('images/units/robotGreen.png').convert_alpha(), (38, 38))
        elif id == 1:
            return pygame.transform.scale(pygame.image.load('images/units/robotBlue.png').convert_alpha(), (38, 38))
        elif id == 2:
            return pygame.transform.scale(pygame.image.load('images/units/robotYellow.png').convert_alpha(), (38, 38))
        else:
            return pygame.transform.scale(pygame.image.load('images/units/robotRed.png').convert_alpha(), (38, 38))

    def GetUnitType(self):
        return Robot


class TankButton(BuyUnitItem):
    def _getTexture(self, id):
        if id == 0:
            return pygame.transform.scale(pygame.image.load('images/units/tankGreen.png').convert_alpha(), (38, 38))
        elif id == 1:
            return pygame.transform.scale(pygame.image.load('images/units/tankBlue.png').convert_alpha(), (38, 38))
        elif id == 2:
            return pygame.transform.scale(pygame.image.load('images/units/tankYellow.png').convert_alpha(), (38, 38))
        else:
            return pygame.transform.scale(pygame.image.load('images/units/tankRed.png').convert_alpha(), (38, 38))

    def GetUnitType(self):
        return Tank


class BoatButton(BuyUnitItem):
    def _getTexture(self, id):
        if id == 0:
            return pygame.transform.scale(pygame.image.load('images/units/shipGreen.png').convert_alpha(), (38, 38))
        elif id == 1:
            return pygame.transform.scale(pygame.image.load('images/units/shipBlue.png').convert_alpha(), (38, 38))
        elif id == 2:
            return pygame.transform.scale(pygame.image.load('images/units/shipYellow.png').convert_alpha(), (38, 38))
        else:
            return pygame.transform.scale(pygame.image.load('images/units/shipRed.png').convert_alpha(), (38, 38))

    def GetUnitType(self):
        return Boat
