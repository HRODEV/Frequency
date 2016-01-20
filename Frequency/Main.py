import pygame
import time

from Vector2 import *
from Menu.StartMenu.StartMenu import StartMenu
from Settings import GameSettings

pygame.init()

def Main():

    # Initialize the pygame display / set the shown caption
    pygame.display.init()
    pygame.display.set_caption('Frequency')

    # Basic Startmenu setup
    settings = GameSettings(Vector2(700, 540))
    screen = pygame.display.set_mode([settings.Resolution.X, settings.Resolution.Y])
    
    # Load & Scale background images
    gBackground = pygame.image.load('images/gameBackground.jpg')
    gBackground = pygame.transform.scale(gBackground, settings.Resolution.Position)
    gLogo = pygame.image.load('images/gameLogo.png')
    gLogo = pygame.transform.scale(gLogo, (230, 230))

    # List with the pygame loaded buttons.
    menuButtons = [
            pygame.image.load('images/buttons/playButton.png'),
            pygame.image.load('images/buttons/rulesButton.png'),
            pygame.image.load('images/buttons/exitButton.png')
    ]

    StartScreen = StartMenu(gBackground, gLogo, menuButtons, settings) 

    while True:
        StartScreen.Draw(screen)
        pygame.display.flip()
        time.sleep(0.2)

Main()