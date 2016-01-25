import pygame

import Vector2
from Helpers import Colors
from Helpers.EventHelpers import EventExist


class DropDownItem:

    def __init__(self, item, rect=None):
        self.Item = item
        self.Rect = rect


    def Draw(self, game, position:Vector2):
        if self.IsHoverdByMouse():
            self.Rect = pygame.draw.rect(game.Settings.GetScreen(), Colors.DIMGREY, [position.X, position.Y, 150, 30])
        else:
            self.Rect = pygame.draw.rect(game.Settings.GetScreen(), Colors.GREY, [position.X, position.Y, 150, 30])


        # Create a font
        font = pygame.font.Font(None, 15)

        # Render the text
        text = font.render(str(self.Item), True, Colors.WHITE)

        # Create a rectangle
        textRect = text.get_rect()

        # Blit the text
        game.Settings.GetScreen().blit(text, [position.X+10, position.Y+15])

    def IsHoverdByMouse(self):
        return self.Rect is not None and self.Rect.collidepoint(pygame.mouse.get_pos())

    def IsClickedByMouse(self, game):
        return self.IsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONDOWN)