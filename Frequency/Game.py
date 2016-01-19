class Game(object):
    """description of class"""

    def __init__(self, state):
        self.State = state

    def Update(self):
        return Game(self.State.Update())

    def Draw(self):
        self.State.Draw()