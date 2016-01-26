from functools import reduce

import pygame

import Game
from Menu.StartMenu.StartMenuItems.ExitGame import ExitGame
from Menu.StartMenu.StartMenuItems.Rules import Rules
from Menu.StartMenu.StartMenuItems.Settings import Settings
from Menu.StartMenu.StartMenuItems.StartGame import StartGame
from Vector2 import Vector2


class StartMenu:

    def __init__(self, game, background=None, logo=None, startMenuItems=None):
        self.Background = background if background is not None \
            else pygame.transform.scale(pygame.image.load('images/gameBackground.jpg'), [game.Settings.Resolution.X, game.Settings.Resolution.Y])

        self.Logo = logo if logo is not None \
            else pygame.transform.scale(pygame.image.load('images/gameLogo.png'), (230, 230))

        self.StartMenuItems = startMenuItems if startMenuItems is not None \
            else [StartGame(Vector2(0, 0)), Settings(Vector2(0,70)), Rules(Vector2(0,140)), ExitGame(Vector2(0,210))]

    def Update(self, game: Game):
        newStartMenuItems = [smi.Update(game) for smi in self.StartMenuItems]

        newstate = reduce(lambda state, smi: smi.GetNewState() if smi.IsClickedByMouse(game) else state, newStartMenuItems, None)

        return newstate if newstate is not None \
            else StartMenu(game, self.Background, self.Logo, newStartMenuItems)

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
