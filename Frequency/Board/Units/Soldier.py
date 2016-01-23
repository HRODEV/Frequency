from Board.Units.Unit import Unit


class Soldier(Unit):
    def __init__(self, player, tile):
        super().__init__(player, tile)
        self.Texture = 'images/units/soldierGreen.png'