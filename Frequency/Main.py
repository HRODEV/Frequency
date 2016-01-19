import pygame
import time

def Main():

    pygame.display.init()
    pygame.display.set_caption('Frequency')
    screen = pygame.display.set_mode([500, 500])
    
    white = 255, 255, 255

    while True:
        screen.fill(white)

        kPress = pygame.key.get_pressed()
        quit = pygame.K_ESCAPE

        if kPress[quit]:
            exit()

        pygame.display.flip()
        time.sleep(0.2)

Main()