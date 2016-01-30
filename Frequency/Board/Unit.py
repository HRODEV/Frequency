import pygame

class Unit:

    def __init__(self, player, tile, textures, size):
        self.Player = player
        self.Tile = tile
        self.Textures = textures
        self.Size = size


    def Update(self, game):
        return self

    def Draw(self, game):
        test = pygame.transform.scale(self.Textures[self.Player.Character.Id], [self.Size, self.Size])
        game.Settings.GetScreen().blit(test, (self.Tile.Position.X * self.Size + game.Settings.GetMenuLeftSize().X,
                                              self.Tile.Position.Y * self.Size))


class Soldier(Unit):
    def __init__(self, player, tile, logicUnit, size):
        self.Textures = [
                        pygame.transform.scale(pygame.image.load('images/units/soldierGreen.png').convert_alpha(), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/units/soldierBlue.png').convert_alpha(), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/units/soldierYellow.png').convert_alpha(), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/units/soldierRed.png').convert_alpha(), [35, 35])
                        ]
        self.Cost = 100
        self.LogicUnit = logicUnit
        super().__init__(player, tile, self.Textures, size)