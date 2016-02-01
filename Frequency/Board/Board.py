import pygame

import Game
from Board.Map.Map import *
from Board.MenuLeft.ActionPanel import *
from Board.MenuRight.MenuRight import *
from Menu.InGameMenu.InGameMenu import InGameMenu

class Board:
    def __init__(self, game, actionPanel=None, menuright=None, map=None):
        self.Map = map if map is not None else Map(game)
        self.ActionPanel = actionPanel if actionPanel is not None else DefaultActionPanel(game)
        self.MenuRight = menuright if menuright is not None else MenuRight(game)

    def Update(self, game: Game):

        def onSelectedTileChanged(lTile):
            if lTile is None:
                self.ActionPanel = DefaultActionPanel(game)
            elif lTile.Building is not None and lTile.Building.Owner == game.Logic.PlayingPlayer:
                self.ActionPanel = BarrackActionPanel(game, lTile)
            elif lTile.Unit is not None and lTile.Unit.Owner == game.Logic.PlayingPlayer:
                self.ActionPanel = UnitActionPanel(game, lTile)
            else:
                self.ActionPanel = InfoActionTile(game, lTile)

        new_map = self.Map.Update(game, onSelectedTileChanged)
        actionPanel = self.ActionPanel.Update(game)

        # check to change selected tile
        if type(actionPanel) is DefaultActionPanel:
            new_map.SetActiveTile(None)
        elif actionPanel.NewSelection is not None:
            new_map.SetActiveTile(actionPanel.NewSelection)
            onSelectedTileChanged(game.Logic.Map.GetTile(actionPanel.NewSelection))
            actionPanel = self.ActionPanel


        for event in game.Events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return InGameMenu(game.Settings.Resolution, self)

        return Board(game, actionPanel, self.MenuRight.Update(game), new_map)

    def Draw(self, game: Game):
        self.ActionPanel.Draw(game)
        self.MenuRight.Draw(game)
        self.Map.Draw(game)
