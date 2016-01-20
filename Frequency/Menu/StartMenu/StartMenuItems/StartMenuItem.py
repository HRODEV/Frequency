import pygame
from pygame.surface import Surface

import Vector2


class StartMenuItem:

    def __init__(self, offset: Vector2, image: Surface = pygame.image.load('images/buttons/playButton.png')):
        self.Image = image
        self.Offset = offset

    def Update(self):
        return self

    def Draw(self, game):
        # Extra screen-based properties
        screen_centerX = game.Settings.Resolution.X // 2
        screen_centerY = game.Settings.Resolution.Y // 2

        x = screen_centerX - self.Image.get_rect().centerx + self.Offset.X
        y = screen_centerY + 20 + self.Offset.Y

        game.Settings.GetScreen().blit(self.Image, (x, y))

