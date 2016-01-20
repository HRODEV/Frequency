import pygame
import time

from Game import Game
from Vector2 import Vector2
from Menu.StartMenu.StartMenu import StartMenu
from Settings import GameSettings


pygame.init()

def Main():
    # Load images
    #gameBackground = pygame.image.load('images/gameBackground.jpg')
    #gameBackground = pygame.transform.scale(gameBackground, (screen_width, screen_height))

    #gameLogo = pygame.image.load('images/gameLogo.png')
    

    white = 255, 255, 255

    settings = GameSettings(Vector2(700, 540))
    pygame.display.init()
    pygame.display.set_caption('Frequency')

    screen = settings.GetScreen()
    





    game = Game()

    StartScreen = StartMenu()

    while True:
        StartScreen.Draw(game)
        pygame.display.flip()
        pygame.event.wait()
        time.sleep(0.2)

Main()