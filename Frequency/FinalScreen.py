import pygame
import Game
from Menu.HeadMenu import HeadMenu
from Menu.StartMenu.StartMenuItems.ExitGame import ExitGame
from Vector2 import Vector2


class FinalScreen(HeadMenu):

    def __init__(self, resolution: Vector2, background=None, logo=None, winner=None):
        super().__init__(resolution, background, logo)

        self.ExitButton = ExitGame(Vector2(0, 210))
        self.ExitButtonHover = pygame.image.load('images/buttons/exitButtonHover.png').convert_alpha()
        self.Winner = winner

    def Update(self, game: Game):
        
        if(self.ExitButton.IsClickedByMouse(game)):
            self.ExitButton.GetNewState()

        super().Update(game)

    def Draw(self, game: Game):
        super().Draw(game)
        self.ExitButton.Draw(game)