from functools import reduce

import pygame

import Game
from Menu.PlayerMenu.PlayerMenuItems.EnterGame import EnterGame
from Vector2 import Vector2


class PlayerNames:

    def __init__(self, game: Game, background=None, logo=None, startMenuItems=None):
        self.Background = background if background is not None \
            else pygame.transform.scale(pygame.image.load('images/gameBackground.jpg'), [game.Settings.Resolution.X, game.Settings.Resolution.Y])

        self.Logo = logo if logo is not None \
            else pygame.transform.scale(pygame.image.load('images/gameLogo.png'), (230, 230))

        self.StartMenuItems = startMenuItems if startMenuItems is not None \
            else [EnterGame(Vector2(0, 0))]


    def Update(self, game: Game):
        newStartMenuItems = [smi.Update(game) for smi in self.StartMenuItems]

        newstate = reduce(lambda state, smi: smi.GetNewState() if smi.IsClickedByMouse(game) else state, newStartMenuItems, None)

        return newstate if newstate is not None \
            else PlayerNames(game, self.Background, self.Logo, newStartMenuItems)

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

        for menuItem in self.StartMenuItems:
            menuItem.Draw(game)
