class Vector2:

    def __init__(self, x, y):
        self.X = x
        self.Y = y
        self.Position = (x, y)

    def __str__(self):
        return str(self.X) + " x " + str(self.Y)

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y
