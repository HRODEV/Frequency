from GameLogic.GameLogic import GameLogic
from Menu.StartMenu.StartMenu import StartMenu
from Settings import GameSettings


class Game(object):
    Events = None

    def __init__(self, state=None, settings: GameSettings = None, events=None, gameLogic: GameLogic = None):
        self.Settings = settings if settings is not None else GameSettings()
        self.State = state if state is not None else StartMenu(self.Settings.Resolution)
        self.Events = events
        self._logic = gameLogic

    @property
    def Logic(self) -> GameLogic:
        return self._logic

    @Logic.setter
    def Logic(self, value: GameLogic):
        self._logic = value

    def Update(self, events):
        state = self.State.Update(self)
        return Game(state, self.Settings, events, self.Logic)

    def Draw(self):
        self.State.Draw(self)
