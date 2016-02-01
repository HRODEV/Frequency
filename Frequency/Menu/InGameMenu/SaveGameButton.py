import pickle
import pygame
from pygame.surface import Surface

from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem
from Vector2 import Vector2


class SaveGameButton(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=None, hover: Surface=None, rect=None, newState=None):
        image = image if image is not None else pygame.image.load('images/buttons/startMenuButton.png').convert_alpha()
        hover = hover if hover is not None else pygame.image.load('images/buttons/StartMenuButtonHover.png').convert_alpha()
        super().__init__(offset, image, hover, rect)
        self._newState = newState


    def Update(self, game):
        if self.IsClickedByMouse(game):
            from Menu.StartMenu.StartMenu import StartMenu
            self._newState = StartMenu(game.Settings.Resolution)
            from datetime import datetime
            time = str(datetime.now().strftime('%Y-%m-%d-%H-%M'))
            with open("./savegames/%s.frgame" % time, "wb") as f:
                pickle.dump(game.Logic, f)
        nself = super().Update(game)
        return SaveGameButton(nself.Offset, nself.Image, nself.Hover, nself.Rect, self._newState)


    def Draw(self, game):
        super().Draw(game)

    def GetNewState(self):
        return self._newState