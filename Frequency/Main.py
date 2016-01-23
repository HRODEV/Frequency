import pygame

from Game import Game

pygame.init()

def Main():
    pygame.display.init()
    pygame.display.set_caption('Frequency')

    game = Game()

    while True:
        game = game.Update(pygame.event.get())
        game.Draw()
        pygame.display.flip()

Main()
