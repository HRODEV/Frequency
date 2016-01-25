import pygame
from sys import exit

from Game import Game
import Helpers

pygame.init()

def Main():
    pygame.display.init()
    pygame.display.set_caption('Frequency')

    game = Game()

    while True:
        events = pygame.event.get()
        if Helpers.EventHelpers.EventExist(events, pygame.QUIT):
            pygame.quit()
            exit()
        game = game.Update(events)
        game.Draw()
        pygame.display.flip()
    
    

Main()
