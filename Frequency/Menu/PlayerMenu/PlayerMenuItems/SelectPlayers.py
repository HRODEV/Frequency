'''
import pygame
from pygame.surface import Surface

from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem
import Vector2

class SelectPlayers:

    def __init__(self, offset: Vector2, image: Surface=pygame.image, rect=None, newState = None):
        self.NewState = newState

    def Update(self, game):
        return StartMenuItem.Update(self, game)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

    def GetNewState(self):
        return None # will be the new state
    '''