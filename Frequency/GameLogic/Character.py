from Vector2 import Vector2


class Character:

    def __init__(self, id=None, startingLocation=None, color=None):
        self.Id = id
        self.StartingLocation = startingLocation if startingLocation is not None else self.GetStartingLocation()
        self.color = color


    def GetStartingLocation(self):
        if self.Id == 0:
            self.StartingLocation = Vector2(0, 0)
        elif self.Id == 1:
            self.StartingLocation = Vector2(0, 18)
        elif self.Id == 2:
            self.StartingLocation = Vector2(18, 0)
        else:
            self.StartingLocation = Vector2(18, 18)