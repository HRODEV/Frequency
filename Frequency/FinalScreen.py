import pygame
import Game
from Menu.HeadMenu import HeadMenu
from Menu.StartMenu.StartMenuItems.ExitGame import ExitGame
from Menu.InGameMenu.StartMenuButton import StartMenuButton
from Vector2 import Vector2


class FinalScreen(HeadMenu):
    def __init__(self, resolution: Vector2, background=None, logo=None, winner=''):
        super().__init__(resolution, background, logo)

        self.ExitButton = ExitGame(Vector2(0, 210))
        self.StartMenuButton = StartMenuButton(Vector2(0, 100))
        self.Winner = winner

    def Update(self, game: Game):
        if self.ExitButton.IsClickedByMouse(game):
            self.ExitButton.GetNewState()
        if self.StartMenuButton.IsClickedByMouse(game):
            from Menu.StartMenu.StartMenu import StartMenu
            return StartMenu(game.Settings.Resolution)

        return super().Update(game)

    def Draw(self, game: Game):
        super().Draw(game)

        screen_centerX = game.Settings.Resolution.X // 2.4
        screen_centerY = game.Settings.Resolution.Y // 2

        font = pygame.font.Font(None, 30)
        winnerText = font.render(str(self.Winner) + " is the winner!", 0, (255, 255, 255))
        game.Settings.GetScreen().blit(winnerText, (screen_centerX, screen_centerY))

        self.ExitButton.Draw(game)
        self.StartMenuButton.Draw(game)
