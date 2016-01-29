import pygame

class Unit:

    def __init__(self, player, tile, textures):
        self.Player = player
        self.Tile = tile
        self.Textures = textures


    def Update(self, game):
        return self


    def Draw(self, game, tile, size, position):
        test = pygame.transform.scale(self.Textures[self.Player.Character.Id], [size, size])
        game.Settings.GetScreen().blit(test, (position.X + game.Settings.GetMenuLeftSize().X, position.Y))