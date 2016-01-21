import pygame
import time

from Game import Game
from Vector2 import Vector2
from Menu.StartMenu.StartMenu import StartMenu
from Settings import GameSettings


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