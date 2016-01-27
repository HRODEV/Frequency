import Game
from Menu.HeadMenu import HeadMenu
from Menu.PlayerMenu.PlayerMenuItems.EnterGame import EnterGame
from Vector2 import Vector2


class PlayerNamesMenu(HeadMenu):

    def __init__(self, resolution:Vector2, background=None, logo=None, startMenuItems=None):
        super().__init__(resolution, background, logo)

        self.StartMenuItems = startMenuItems if startMenuItems is not None \
            else [EnterGame(Vector2(0, 0))]

    def Update(self, game: Game):
        newStartMenuItems = [smi.Update(game) for smi in self.StartMenuItems]

        newstate = next((smi.GetNewState() for smi in newStartMenuItems if smi.IsClickedByMouse()), None)

        return newstate if newstate is not None \
            else PlayerNamesMenu(game, self.Background, self.Logo, newStartMenuItems)

    def Draw(self, game: Game):
        super().Draw(game)

        for menuItem in self.StartMenuItems:
            menuItem.Draw(game)
