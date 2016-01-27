import pygame

from Board.Buildings.Building2 import Building


class Barracks(Building):
    def __init__(self, player, tile):
        self.Texture = [
                        pygame.transform.scale(pygame.image.load('images/buildings/barracksGreen.png'), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/buildings/barracksBlue.png'), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/buildings/barracksYellow.png'), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/buildings/barracksRed.png'), [35, 35])
                        ]
        super().__init__(player, tile, self.Texture)