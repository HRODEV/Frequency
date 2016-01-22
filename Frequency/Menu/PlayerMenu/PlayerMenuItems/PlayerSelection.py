import pygame
import sys
from functools import reduce
from pygame.surface import Surface

import Game
from Menu.PlayerMenu.PlayerMenuItems.TwoPlayers import TwoPlayers
from Menu.PlayerMenu.PlayerMenuItems.ThreePlayers import ThreePlayers
from Menu.PlayerMenu.PlayerMenuItems.FourPlayers import FourPlayers
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem
from Vector2 import Vector2

class PlayerSelection(StartMenuItem):

    def __init__(self, resolution, background=None, logo=None, playerMenuItems=None):
        self.Resolution = resolution

        self.Background = background if background is not None \
            else pygame.transform.scale(pygame.image.load('images/gameBackground.jpg'), [self.Resolution.X, self.Resolution.Y])

        self.Logo = logo if logo is not None \
            else pygame.transform.scale(pygame.image.load('images/gameLogo.png'), (230, 230))

        self.PlayerMenuItems = playerMenuItems if playerMenuItems is not None \
            else [TwoPlayers(Vector2(0,0)), ThreePlayers(Vector2(0,70)), FourPlayers(Vector2(0, 140))]
 
    def Update(self, game: Game):
        newPlayerMenuItems = [pmi.Update(game) for pmi in self.PlayerMenuItems]

        newstate = reduce(lambda state, pmi: pmi.GetNewState() if pmi.IsClickedByMouse(game) else state, newPlayerMenuItems, None)

        return newstate if newstate is not None \
            else PlayerSelection(game.Settings.Resolution, self.Background, self.Logo, newPlayerMenuItems)

    def Draw(self, game):

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

        for menuItem in self.PlayerMenuItems:
            menuItem.Draw(game)

    def GetNewState(self):
        return None # will be the new state