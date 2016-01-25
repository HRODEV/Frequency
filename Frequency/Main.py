import pygame

from Game import Game

pygame.init()
clock = pygame.time.Clock()

def Main():
    pygame.display.init()

    game = Game()

    while True:
        game = game.Update(pygame.event.get())
        game.Draw()

        clock.tick()
        pygame.display.set_caption('Frequency | FPS: %i' % int(clock.get_fps()+100))
        pygame.display.flip()

Main()
