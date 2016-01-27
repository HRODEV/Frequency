class Building:

    def __init__(self, player, tile, textures):
        self.Player = player
        self.Tile = tile
        self.Textures


    def Update(self, game):
        return self


    def Draw(self, game):
        tileSize = min(self.Tile.Size.X, self.Tile.Size.Y)
        game.Settings.GetScreen().blit(self.Textures[self.Player.Character], ((self.Tile.Position.X * tileSize) + game.Settings.GetMenuLeftSize().X, self.Tile.Position.Y * tileSize))