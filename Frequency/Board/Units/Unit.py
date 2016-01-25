import pygame

class Unit:

    def __init__(self, player, tile, texture):
        self.Player = player
        self.Tile = tile
        self.Texture


    def Update(self, game):
        return self


    def Draw(self, game):
        tileSize = min(game.Settings.Resolution.X // game.Settings.GetMaxTiles().X,
                       game.Settings.Resolution.Y // game.Settings.GetMaxTiles().Y)

        game.Settings.GetScreen().blit(self.Texture, ((self.Tile.Position.X * tileSize) + game.Settings.GetMenuLeftSize().X, self.Tile.Position.Y * tileSize))