class Tile:

    def __init__(self, type, position, defaultMoney, enemyMoney, texture, units=None):
        self.Type = type
        self.Position = position
        self.DefaultMoney = defaultMoney
        self.EnemyMoney = enemyMoney
        self.Texture = texture
        self.Units = units
        self.Width = 75
        self.Height = 75
