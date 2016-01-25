import pygame

import Game
from FormControlls.DropDownItem import DropDownItem
from Helpers import Colors
from Helpers.EventHelpers import EventExist
from Vector2 import Vector2


class DropDown:

    def __init__(self, items, position:Vector2, dropDownButtonRect = None, selcted:object="", active=False):
        self.DropDownItems = [item if isinstance(item, DropDownItem) else DropDownItem(item) for item in items]
        self.Position = position
        self.DropDownButtonRect = dropDownButtonRect
        self.Selected = selcted
        self.Active = active

    def Update(self, game:Game):
        if len([ddi for ddi in self.DropDownItems if ddi.IsClickedByMouse(game)]) == 1:
            return DropDown(self.DropDownItems, self.Position, self.DropDownButtonRect, [ddi for ddi in self.DropDownItems if ddi.IsClickedByMouse(game)][0].Item, False)
        if self.IsdropDownButtonRectClickedByMouse(game):
            return DropDown(self.DropDownItems, self.Position, self.DropDownButtonRect, self.Selected, not self.Active)
        else:
            return self

    def Draw(self, game:Game):
        screen = game.Settings.GetScreen()

        pygame.draw.rect(screen, Colors.BLACK, [self.Position.X, self.Position.Y, 150, 30])
        self.DropDownButtonRect = pygame.draw.rect(screen, Colors.RED, [self.Position.X + 150, self.Position.Y, 30, 30])

        if self.Active:
            for i in range(0,len(self.DropDownItems)):
                self.DropDownItems[i].Draw(game, Vector2(self.Position.X, self.Position.Y + 30 + (i * 30)))

        # Create a font
        font = pygame.font.Font(None, 15)
        # Render the text
        text = font.render(str(self.Selected), True, Colors.WHITE)
        # Create a rectangle
        textRect = text.get_rect()
        # Blit the text
        game.Settings.GetScreen().blit(text, [self.Position.X+10, self.Position.Y+15])

    def IsdropDownButtonRectHoverdByMouse(self):
        return self.DropDownButtonRect is not None and self.DropDownButtonRect.collidepoint(pygame.mouse.get_pos())

    def IsdropDownButtonRectClickedByMouse(self, game):
        return self.IsdropDownButtonRectHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONDOWN)