import pygame

from Menu.StartMenu.StartMenu import StartMenu
from Settings import GameSettings


class Game(object):

    def __init__(self, state = None, settings: GameSettings = None):
        self.State = state if state is not None else StartMenu(self)
        self.Settings = settings if settings is not None else GameSettings()

    def Update(self):
        return Game(self.State.Update())

    def Draw(self):
        pass