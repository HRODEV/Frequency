import pygame
import Game
from Menu.HeadMenu import HeadMenu
from Menu.StartMenu.StartMenuItems.ExitGame import ExitGame
from Vector2 import Vector2


class FinalScreen(HeadMenu):

    def __init__(self, resolution: Vector2, background=None, logo=None, winner=''):
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

        screen_centerX = game.Settings.Resolution.X // 2.4
        screen_centerY = game.Settings.Resolution.Y // 2

        font = pygame.font.Font(None,30)
        winnerText = font.render(str(self.Winner)+" is the winner!", 0,(255,255,255))
        game.Settings.GetScreen().blit(winnerText, (screen_centerX, screen_centerY))

        self.ExitButton.Draw(game)