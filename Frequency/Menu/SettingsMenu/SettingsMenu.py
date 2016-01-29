import pygame

from FormControlls.DropDown import DropDown
from Helpers import Colors
from Menu.HeadMenu import HeadMenu
from Menu.SettingsMenu.FullscreenButton import Fullscreen
from Menu.SettingsMenu.SaveButton import SaveButton
from Vector2 import Vector2


class SettingsMenu(HeadMenu):

    def __init__(self, resolution, background=None, logo=None, dropDown=None, saveButton=None, fullscreen=None):
        super().__init__(resolution, background, logo)

        resolutions = [Vector2(1000, 640), Vector2(1280, 800), Vector2(1440, 900), Vector2(1800, 1000), Vector2(2560, 1600)]

        self.ResolutionDropDown = dropDown if dropDown is not None else DropDown(resolutions, Vector2(resolution.X // 2, 400), resolution)

        self.SaveButton = saveButton if saveButton is not None else SaveButton()

        self.FullscreenButton = fullscreen if fullscreen is not None else Fullscreen()

    def Update(self, game):
        if self.SaveButton.IsClickedByMouse(game):
            game.Settings.SetResolution(self.ResolutionDropDown.Selected)
            from Menu.StartMenu.StartMenu import StartMenu
            return StartMenu(game.Settings.Resolution)
        elif self.FullscreenButton.IsClickedByMouse(game):
            game.Settings.SetResolution(self.ResolutionDropDown.Selected, True)
            from Menu.StartMenu.StartMenu import StartMenu
            return StartMenu(game.Settings.Resolution)
        else:
            newDropDown = self.ResolutionDropDown.Update(game)
            saveButton = self.SaveButton.Update(game)
            fullscreenButton = self.FullscreenButton.Update(game)
            return SettingsMenu(game.Settings.Resolution, self.Background, self.Logo, newDropDown, saveButton, fullscreenButton)

    def Draw(self, game):
        super().Draw(game)

        # Create a font
        font = pygame.font.Font(None, 25)
        # Render the text
        text = font.render("Resolution:", True, Colors.RED)
        # Create a rectangle
        textRect = text.get_rect()
        # Blit the text
        game.Settings.GetScreen().blit(text, [(game.Settings.Resolution.X // 2)-100, 405])

        self.ResolutionDropDown.Draw(game)

        self.FullscreenButton.Draw(game)
        self.SaveButton.Draw(game)