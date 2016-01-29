import pygame

from Board.Buildings.Building import Building


class Base(Building):
    def __init__(self, player, tile):
        self.Textures = [
                        pygame.transform.scale(pygame.image.load('images/buildings/baseGreen.png').convert_alpha(), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/buildings/baseBlue.png').convert_alpha(), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/buildings/baseYellow.png').convert_alpha(), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/buildings/baseRed.png').convert_alpha(), [35, 35])
                        ]
        super().__init__(player, tile, self.Textures)