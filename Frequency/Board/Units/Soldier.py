import pygame
from Board.Units.Unit import Unit


class Soldier(Unit):
    def __init__(self, player, tile):
        self.Textures = [
                        pygame.transform.scale(pygame.image.load('images/units/soldierGreen.png'), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/units/soldierBlue.png'), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/units/soldierYellow.png'), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/units/soldierRed.png'), [35, 35])
                        ]
        self.Cost = 100
        super().__init__(player, tile, self.Textures)