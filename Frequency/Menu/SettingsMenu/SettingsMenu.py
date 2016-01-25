from FormControlls.DropDown import DropDown
from Menu.HeadMenu import HeadMenu
from Vector2 import Vector2


class SettingsMenu(HeadMenu):

    def __init__(self, resolution, background=None, logo=None, dropDown=None):
        super().__init__(resolution, background, logo)

        self.ResolutionDropDown = dropDown if dropDown is not None else DropDown([Vector2(640,800),Vector2(1920,1080)], Vector2(400,200))

    def Update(self, game):
        newDropDown = self.ResolutionDropDown.Update(game)
        return SettingsMenu(game.Settings.Resolution, self.Background, self.Logo, newDropDown)

    def Draw(self, game):
        super().Draw(game)

        self.ResolutionDropDown.Draw(game)

