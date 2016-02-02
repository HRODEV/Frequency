import pickle
import pygame
from pygame.surface import Surface

from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem
from Vector2 import Vector2


class SoundInGameButton(StartMenuItem):

    def __init__(self, offset: Vector2, image: Surface=None, hover: Surface=None, rect=None):
        image = image if image is not None else pygame.image.load('images/buttons/toggleSoundButton.png').convert_alpha()
        hover = hover if hover is not None else pygame.image.load('images/buttons/toggleSoundButtonHover.png').convert_alpha()
        super().__init__(offset, image, hover, rect)


    def Update(self, game):
        if self.IsClickedByMouse(game):
            game.Settings.SetSound()
        nself = super().Update(game)
        return SoundInGameButton(nself.Offset, nself.Image, nself.Hover, nself.Rect)


    def Draw(self, game):
        super().Draw(game)