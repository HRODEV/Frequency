import pygame

from Board.Buildings.Building import Building


class Base(Building):
    def __init__(self, player, tile):
        self.Textures = [
                        pygame.transform.scale(pygame.image.load('images/buildings/baseGreen.png'), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/buildings/baseBlue.png'), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/buildings/baseYellow.png'), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/buildings/baseRed.png'), [35, 35])
                        ]
        super().__init__(player, tile, self.Textures)