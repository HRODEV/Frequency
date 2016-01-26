import pygame

from FormControlls.DropDown import DropDown
from Helpers import Colors
from Menu.HeadMenu import HeadMenu
from Vector2 import Vector2


class SettingsMenu(HeadMenu):

    def __init__(self, resolution, background=None, logo=None, dropDown=None):
        super().__init__(resolution, background, logo)

        self.ResolutionDropDown = dropDown if dropDown is not None else DropDown([Vector2(640,800),Vector2(1920,1080)], Vector2(500,400))

    def Update(self, game):
        newDropDown = self.ResolutionDropDown.Update(game)
        return SettingsMenu(game.Settings.Resolution, self.Background, self.Logo, newDropDown)

    def Draw(self, game):
        super().Draw(game)

        # Create a font
        font = pygame.font.Font(None, 25)
        # Render the text
        text = font.render("Resolution:", True, Colors.RED)
        # Create a rectangle
        textRect = text.get_rect()
        # Blit the text
        game.Settings.GetScreen().blit(text, [400, 405])

        self.ResolutionDropDown.Draw(game)

