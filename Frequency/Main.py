import pygame
import time

import Menu.StartMenu.StartMenu
from Game import Game


def Main():

    # Initialize the pygame display / set the shown caption
    pygame.display.init()
    pygame.display.set_caption('Frequency')
    
    #game = Game(1,2)

    # Set the screen
    screen_width = 700
    screen_height = 540
    screen = pygame.display.set_mode([screen_width, screen_height])

    # Extra screen-based properties
    screen_centerX = int(screen_width / 2)
    screen_centerY = int(screen_height / 2)
    screen_marginX = int(screen_height / 18)
    
    # Load images
    gBackground = pygame.image.load('images/gameBackground.jpg')
    gBackground = pygame.transform.scale(gBackground, (screen_width, screen_height))

    gLogo = pygame.image.load('images/gameLogo.png')
    gLogo = pygame.transform.scale(gLogo, (230, 230))
    gLogoSize = gLogo.get_rect()
    gLogoCenter = (screen_centerX - gLogoSize.centerx, screen_marginX)

    white = 255, 255, 255

    while True:

        # Basic screen loaded elements
        screen.fill(white)
        screen.blit(gBackground, (0,0))
        screen.blit(gLogo, gLogoCenter)
        
        '''catchKeys(screen, pygame.event.get())

        for event in keyEvents:
            if( event.type == pygame.KEYDOWN and 
                event.key == (pygame.K_ESCAPE or pygame.QUIT) ):
                exit()'''

        pygame.display.flip()
        time.sleep(0.2)

Main()