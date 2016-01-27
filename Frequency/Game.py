from Menu.StartMenu.StartMenu import StartMenu
from Settings import GameSettings
from GameLogic.GameLogic import GameLogic

class Game(object):
    Events = None

    def __init__(self, state=None, settings: GameSettings=None, events=None, gameLogic: GameLogic=None):
        self.Settings = settings if settings is not None else GameSettings()
        self.State = state if state is not None else StartMenu(self)
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
        logic = self.Logic.Update(self) if self.Logic is not None else None
        return Game(state, self.Settings, events, logic)

    def Draw(self):
        self.State.Draw(self)