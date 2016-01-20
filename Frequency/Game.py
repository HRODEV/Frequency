class Game(object):
    """description of class"""

    def __init__(self, state, screen, settings):
        self.State = state
        self.Screen = screen
        self.Settings = settings

    def Update(self):
        return Game(self.State.Update())

    def Draw(self):
        pass