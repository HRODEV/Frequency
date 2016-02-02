import pygame
import pickle
from os import walk

from Board.Board import Board
from Helpers import Colors
from Menu.HeadMenu import HeadMenu
from FormControlls.DropDown import DropDown
from Menu.LoadGameMenu.LoadButton import LoadButton
from Vector2 import Vector2


class LoadGameMenu(HeadMenu):

    def __init__(self, resolution, background=None, logo=None, dropDown=None, loadButton=None, savenames=None, newState=None):
        super().__init__(resolution, background, logo)

        if savenames is None:
            for (dirpath, dirnames, filenames) in walk("savegames"):
                    self.SaveNames = filenames
                    break
        else:
            self.SaveNames = savenames
        self.DropDown = dropDown if dropDown is not None else DropDown(self.SaveNames, Vector2(550, 430), "Select a savegame")
        self.LoadButton = loadButton if loadButton is not None else LoadButton()
        self._newState = newState


    def Update(self, game):
        if self.LoadButton.IsClickedByMouse(game):
            with open("savegames/%s" % self.DropDown.Selected, "rb") as f:
                game.Logic = pickle.load(f)
                return Board(game)
        nself = super().Update(game)
        newDropDown = self.DropDown.Update(game)
        saveButton = self.LoadButton.Update(game)
        return LoadGameMenu(game.Settings.Resolution, nself.Background, nself.Logo, newDropDown, saveButton, self._newState)

    def Draw(self, game):
        super().Draw(game)

        # Create a font
        font = pygame.font.Font(None, 25)
        # Render the text
        text = font.render("Select a saved game:", True, Colors.RED)
        # Create a rectangle
        textRect = text.get_rect()
        # Blit the text
        game.Settings.GetScreen().blit(text, [(game.Settings.Resolution.X // 2)-100, 405])

        self.DropDown.Draw(game)
        self.LoadButton.Draw(game)


    def GetNewState(self):
        return self._newState