import pygame

from Menu.StartMenu.StartMenu import StartMenu
from Settings import GameSettings


class Game(object):
    def __init__(self, state = None, settings: GameSettings = None):
        self.Settings = settings if settings is not None else GameSettings()
        self.State = state if state is not None else StartMenu(self.Settings.Resolution)

    def Update(self):
        return Game(self.State.Update(self))

    def Draw(self):
        self.State.Draw(self)