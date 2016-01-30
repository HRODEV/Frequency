import pygame

import Game


class HeadMenu:

    def __init__(self, resolution, background=None, logo=None):
        self.Background = background if background is not None \
            else pygame.transform.scale(pygame.image.load('images/gameBackground.jpg').convert(), [resolution.X, resolution.Y])

        self.Logo = logo if logo is not None \
            else pygame.transform.scale(pygame.image.load('images/gameLogo.png').convert_alpha(), (230, 230))

    def Update(self, game: Game):
        return self

    def Draw(self, game: Game):

        # Extra screen-based properties
        screen_centerX = int(game.Settings.Resolution.X // 2)
        screen_marginX = int(game.Settings.Resolution.Y / 18)

        # Logo position
        logoSize = self.Logo.get_rect()
        logoCenterX = screen_centerX - logoSize.centerx
        logoCenter = (logoCenterX, screen_marginX)

         # Basic screen loaded elements
        game.Settings.GetScreen().fill((255, 255, 255))
        game.Settings.GetScreen().blit(self.Background, (0, 0))
        game.Settings.GetScreen().blit(self.Logo, logoCenter)
