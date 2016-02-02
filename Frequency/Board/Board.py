import pygame

import Game
from FinalScreen import FinalScreen
from Board.Map.Map import *
from Board.ActionPanel.ActionPanel import *
from Board.MenuRight.MenuRight import *
from Menu.InGameMenu.InGameMenu import InGameMenu

class Board:
    def __init__(self, game, actionPanel=None, menuright=None, map=None):
        self.Map = map if map is not None else Map(game)
        self.ActionPanel = actionPanel if actionPanel is not None else DefaultActionPanel(game)
        self.MenuRight = menuright if menuright is not None else MenuRight(game)

    def Update(self, game: Game):

        if(game.Logic.CheckWinner()):
            return FinalScreen(game.Settings.Resolution, None, None, game.Logic.CheckWinner().Name)

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
        # Turn background color in color of current player
        if game.Logic.PlayingPlayer.Character.Id == 0:
            game.Settings.GetScreen().fill(Colors.PLAYER_GREEN)
        elif game.Logic.PlayingPlayer.Character.Id == 1:
            game.Settings.GetScreen().fill(Colors.PLAYER_BLUE)
        elif game.Logic.PlayingPlayer.Character.Id == 2:
            game.Settings.GetScreen().fill(Colors.PLAYER_YELLOW)
        else:
            game.Settings.GetScreen().fill(Colors.PLAYER_RED)

        self.ActionPanel.Draw(game)
        self.MenuRight.Draw(game)
        self.Map.Draw(game)
