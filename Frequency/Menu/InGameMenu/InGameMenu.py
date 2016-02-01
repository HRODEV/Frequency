import Game
from Menu.HeadMenu import HeadMenu
from Menu.InGameMenu.ResumeButton import ResumeButton
from Menu.InGameMenu.StartMenuButton import StartMenuButton
from Menu.StartMenu.StartMenuItems.ExitGame import ExitGame
from Vector2 import Vector2


class InGameMenu(HeadMenu):

    def __init__(self, resolution: Vector2, oldState, background=None, logo=None, startMenuItems=None):
        super().__init__(resolution, background, logo)
        self.OldState = oldState

        self.StartMenuItems = startMenuItems if startMenuItems is not None \
            else [ResumeButton(Vector2(0, 0), self.OldState), StartMenuButton(Vector2(0, 70)), ExitGame(Vector2(0, 140))]

    def Update(self, game: Game):
        newStartMenuItems = [smi.Update(game) for smi in self.StartMenuItems]

        newstate = next((smi.GetNewState() for smi in newStartMenuItems if smi.IsClickedByMouse(game)), None)

        return newstate if newstate is not None \
            else InGameMenu(game.Settings.Resolution, self.OldState, self.Background, self.Logo, newStartMenuItems)

    def Draw(self, game: Game):
        super().Draw(game)

        for menuItem in self.StartMenuItems:
            menuItem.Draw(game)