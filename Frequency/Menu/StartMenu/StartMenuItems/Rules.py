import pygame
from pygame.surface import Surface
import time

import Vector2
from Helpers.popup import Popup
from Settings import GameSettings
from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem
from Rules.GameInstructions import GameInstructions

class Rules(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=pygame.image.load('images/buttons/rulesButton.png'), rect=None, newState=None):
        super().__init__(offset, image, rect)
        self._newState = newState

    def Update(self, game):
        self.Show(game)
        return StartMenuItem.Update(self, game)

    def Draw(self, game):
        StartMenuItem.Draw(self, game)

    def GetNewState(self):
        return self._newState

    def Show(self, game):

        if self.IsClickedByMouse(game):
            popup = Popup(GameSettings().GetScreen(), '')
            open = True
            while(open):
                popup.Draw()

                if(popup.Update(pygame.event.get()) == None):
                    open = False
