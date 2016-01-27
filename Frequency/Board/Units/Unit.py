class Unit:

    def __init__(self, player, tile, textures):
        self.Player = player
        self.Tile = tile
        self.Textures = textures


    def Update(self, game):
        return self


    def Draw(self, game, tile):
        tileSize = min(self.Tile.Size.X, self.Tile.Size.Y)
        game.Settings.GetScreen().blit(self.Textures[self.Player.Character], ((tile.Position.X * tileSize) + game.Settings.GetMenuLeftSize().X, tile.Position.Y * tileSize))