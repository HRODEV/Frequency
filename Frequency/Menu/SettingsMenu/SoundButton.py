import pygame
from pygame.surface import Surface

from Helpers.EventHelpers import EventExist


class SoundButton:
    def __init__(self, image: Surface = None, hover: Surface=None, rect=None):
        self.Image = image if image is not None else pygame.image.load('images/buttons/toggleSoundButton.png').convert_alpha()
        self.Hover = hover if hover is not None else  pygame.image.load('images/buttons/toggleSoundButtonHover.png').convert_alpha()
        self.Rect = rect

    def Update(self, game):
        return self

    def Draw(self, game):
        # Extra screen-based properties
        screen_centerX = game.Settings.Resolution.X // 2

        x = screen_centerX - self.Image.get_rect().centerx
        y = game.Settings.Resolution.Y - 80

        if self.IsHoverdByMouse():
            self.Rect = game.Settings.GetScreen().blit(self.Hover, (x, y))
        else:
            self.Rect = game.Settings.GetScreen().blit(self.Image, (x, y))

    def IsHoverdByMouse(self):
        return self.Rect is not None and self.Rect.collidepoint(pygame.mouse.get_pos())

    def IsClickedByMouse(self, game):
        return self.IsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)
