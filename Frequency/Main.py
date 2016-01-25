import pygame
from sys import exit

from Game import Game
import Helpers

pygame.init()

def Main():
    pygame.display.init()
    pygame.display.set_caption('Frequency')

    game = Game()
    done = False

    while not done:
        events = pygame.event.get()
        if Helpers.EventHelpers.EventExist(events, pygame.QUIT):
            done = True
        game = game.Update(events)
        game.Draw()
        pygame.display.flip()
    pygame.quit()
    exit()
    

Main()
