import Game
from Menu.HeadMenu import HeadMenu
from Menu.StartMenu.StartMenuItems.ExitGame import ExitGame
from Menu.StartMenu.StartMenuItems.LoadGame import LoadGame
from Menu.StartMenu.StartMenuItems.Rules import Rules
from Menu.StartMenu.StartMenuItems.Settings import Settings
from Menu.StartMenu.StartMenuItems.StartGame import StartGame
from Vector2 import Vector2


class StartMenu(HeadMenu):
    def __init__(self, resolution: Vector2, background=None, logo=None, startMenuItems=None):
        super().__init__(resolution, background, logo)

        self.StartMenuItems = startMenuItems if startMenuItems is not None \
            else [StartGame(Vector2(0, 0)), Settings(Vector2(0, 70)), Rules(Vector2(0, 140)), LoadGame(Vector2(0, 210)),
                  ExitGame(Vector2(0, 280))]

    def Update(self, game: Game):
        newStartMenuItems = [smi.Update(game) for smi in self.StartMenuItems]

        newstate = next((smi.GetNewState() for smi in newStartMenuItems if smi.IsClickedByMouse(game)), None)

        return newstate if newstate is not None \
            else StartMenu(game, self.Background, self.Logo, newStartMenuItems)

    def Draw(self, game: Game):
        super().Draw(game)

        for menuItem in self.StartMenuItems:
            menuItem.Draw(game)
