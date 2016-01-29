import pygame
from sys import exit

from Game import Game
import Helpers

pygame.init()
clock = pygame.time.Clock()

def Main():
    pygame.display.init()

    # Music
    pygame.mixer.init()
    pygame.mixer.music.load('Resources/menu.mp3')
    pygame.mixer.music.play()
    
    game = Game()

    while True:
        events = pygame.event.get()
        if Helpers.EventHelpers.EventExist(events, pygame.QUIT):
            pygame.quit()
            exit()
        game = game.Update(events)
        game.Draw()

        clock.tick()
        pygame.display.set_caption('Frequency | FPS: %i' % int(clock.get_fps()+100))
        pygame.display.flip()
    
    

Main()
