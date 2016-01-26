from Menu.StartMenu.StartMenu import StartMenu
from Settings import GameSettings
from GameLogic.GameLogic import GameLogic

class Game(object):
    Events = None

    def __init__(self, state=None, settings: GameSettings=None, events=None, gameLogic=None):
        self.Settings = settings if settings is not None else GameSettings()
        self.State = state if state is not None else StartMenu(self)
        self.Events = events
        self.Logic = gameLogic if gameLogic is not None else GameLogic()


    def Update(self, events):
        return Game(self.State.Update(self), self.Settings, events, self.Logic.Update(self.Logic))


    def Draw(self):
        self.State.Draw(self)