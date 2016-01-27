from Game import Game


class InputBox:

    def __init__(self, position, labelText, maxlength=20, value="", active=False):
        self.Position = position
        self.LabelText = labelText
        self.MaxLength = maxlength
        self.Value = value
        self.Active = active


    def Update(self, game:Game):
        # check for new textinput
        newchar = ''
        for event in game.Events:
            event

