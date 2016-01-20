import pygame

import Game
from Menu.StartMenu.StartMenuItems.ExitGame import ExitGame
from Menu.StartMenu.StartMenuItems.StartGame import StartGame
from Vector2 import Vector2

background = pygame.image.load('images/gameBackground.jpg')
# gBackground = pygame.transform.scale(gBackground, [settings.Resolution.X, settings.Resolution.Y])

logo = pygame.image.load('images/gameLogo.png')
logo = pygame.transform.scale(logo, (230, 230))



class StartMenu:

    def __init__(self, background= background, logo= logo, startMenuItems = None):
        self.Background = background
        self.Logo = logo
        self.StartMenuItems = startMenuItems if startMenuItems is not None \
            else [StartGame(Vector2(0, 0)), ExitGame(Vector2(0,140)),]

    def Update(self, game):
        return StartMenu(map((lambda smi: smi.Update()), self.StartMenuItems.map()))

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
