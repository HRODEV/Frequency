class Game(object):
    """description of class"""

    def __init__(self, state, properties):
        self.State = state
        self.Properties = properties

    def Update(self):
        return Game(self.State.Update())

    def Draw(self):
        self.State.Draw()