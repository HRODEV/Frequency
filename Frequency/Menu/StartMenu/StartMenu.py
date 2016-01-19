
class StartMenu:

    def __init__(self, startMenuItems):
        self.StartMenuItems = startMenuItems

    def Update(self):
        return StartMenu(map((lambda smi: smi.Update()), self.StartMenuItems.map()))

    def Draw(self, screen):
        for smi in self.StartMenuItems:
            smi.Draw()