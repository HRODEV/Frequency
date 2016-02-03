import Game
from Menu.HeadMenu import HeadMenu
from Menu.PlayerMenu.PlayerSelectionMenuItems import *
from Vector2 import Vector2


class PlayerSelection(HeadMenu):
    def __init__(self, resolution, background=None, logo=None, playerMenuItems=None):
        super().__init__(resolution, background, logo)

        self.PlayerMenuItems = playerMenuItems if playerMenuItems is not None \
            else [TwoPlayers(Vector2(0, 0)), ThreePlayers(Vector2(0, 70)), FourPlayers(Vector2(0, 140))]

    def Update(self, game: Game):
        newPlayerMenuItems = [pmi.Update(game) for pmi in self.PlayerMenuItems]

        newstate = next((smi.GetNewState() for smi in newPlayerMenuItems if smi.IsClickedByMouse(game)), None)

        return newstate if newstate is not None \
            else PlayerSelection(game, self.Background, self.Logo, newPlayerMenuItems)

    def Draw(self, game):
        super().Draw(game)

        for menuItem in self.PlayerMenuItems:
            menuItem.Draw(game)
