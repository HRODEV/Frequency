import pygame
from Board.Units.Unit import Unit


class Soldier(Unit):
    def __init__(self, player, tile, logicUnit):
        self.Textures = [
                        pygame.transform.scale(pygame.image.load('images/units/soldierGreen.png').convert_alpha(), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/units/soldierBlue.png').convert_alpha(), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/units/soldierYellow.png').convert_alpha(), [35, 35]),
                        pygame.transform.scale(pygame.image.load('images/units/soldierRed.png').convert_alpha(), [35, 35])
                        ]
        self.Cost = 100
        self.LogicUnit = logicUnit
        super().__init__(player, tile, self.Textures)
