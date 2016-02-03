import pygame
from pygame.surface import Surface

from Menu.StartMenu.StartMenuItems.StartMenuItem import StartMenuItem
from Vector2 import Vector2


class ResumeButton(StartMenuItem):
    def __init__(self, offset: Vector2, oldState, image: Surface = None, hover: Surface = None, rect=None,
                 newState=None):
        image = image if image is not None else pygame.image.load('images/buttons/resumeButton.png').convert_alpha()
        hover = hover if hover is not None else pygame.image.load(
            'images/buttons/resumeButtonHover.png').convert_alpha()
        super().__init__(offset, image, hover, rect)
        self.OldState = oldState
        self._newState = newState

    def Update(self, game):
        if self.IsClickedByMouse(game):
            self._newState = self.OldState
        nself = super().Update(game)
        return ResumeButton(nself.Offset, self.OldState, nself.Image, nself.Hover, nself.Rect, self._newState)

    def Draw(self, game):
        super().Draw(game)

    def GetNewState(self):
        return self._newState
