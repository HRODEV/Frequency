import pygame
import time

from Vector2 import *
from Menu.StartMenu.StartMenu import StartMenu
from Settings import GameSettings

def Main():

    # Initialize the pygame display / set the shown caption
    pygame.display.init()
    pygame.display.set_caption('Frequency')

    # Basic Startmenu setup
    settings = GameSettings(Vector2(700, 540))
    screen = pygame.display.set_mode([settings.Resolution.X, settings.Resolution.Y])
    
    # Load images
    gBackground = pygame.image.load('images/gameBackground.jpg')
    gBackground = pygame.transform.scale(gBackground, settings.Resolution.Position)
    gLogo = pygame.image.load('images/gameLogo.png')
    gLogo = pygame.transform.scale(gLogo, (230, 230))

    StartScreen = StartMenu(gBackground, gLogo, settings) 

    while True:
        StartScreen.Draw(screen)
        pygame.display.flip()
        time.sleep(0.2)

Main()