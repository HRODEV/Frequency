import pygame
import time
from GameRules import *

def Main():
    pygame.display.init()
    pygame.display.set_caption('Frequency')

    screen_width = 960
    screen_height = 540
    screen = pygame.display.set_mode([screen_width, screen_height])

    button_1 = pygame.draw.rect(screen, (0, 0, 255), (200, 150, 100, 50))
    screen.blit(screen, button_1)
    
    # Load images
    #gameBackground = pygame.image.load('images/gameBackground.jpg')
    #gameBackground = pygame.transform.scale(gameBackground, (screen_width, screen_height))

    #gameLogo = pygame.image.load('images/gameLogo.png')
    

    white = 255, 255, 255

    while True:
        screen.fill(white)
        #screen.blit(gameBackground, (0,0))
        #screen.blit(gameLogo, (250, 250))
        
        '''catchKeys(screen, pygame.event.get())

        for event in keyEvents:
            if( event.type == pygame.KEYDOWN and 
                event.key == (pygame.K_ESCAPE or pygame.QUIT) ):
                exit()'''

        pygame.display.flip()
        time.sleep(0.2)

Main()