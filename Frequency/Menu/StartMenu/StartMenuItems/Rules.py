import pygame
from pygame.surface import Surface
import time

import Vector2
from Helpers.popup import Popup
from Settings import GameSettings
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem
from Rules.GameInstructions import GameInstructions

class Rules(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/buttons/rulesButton.png'), hover: Surface=pygame.image.load('images/buttons/rulesButtonHover.png'),  rect=None):
        super().__init__(offset, image, rect)

    def Update(self, game):
        self.Show(game)
        return StartMenuItem.Update(self, game)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

    def Show(self, game):

        if self.IsClickedByMouse(game):
            # Popup instance
            popup = Popup(game.Settings.GetScreen())
            # Define open as true for the while, we turn this into false if the close button is clicked
            open = True
            while(open):
                # Draw the popup
                popup.Draw('Resources/Instructions.txt')
                # If the update returns none (which is after you click on the exit button)
                if(popup.Update(pygame.event.get()) == None):
                    # Define open as false to stop showing the popup
                    open = False
