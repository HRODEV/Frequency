import xml.etree.ElementTree as ET
import pygame
import Game
from Board.Map.Map import *

class GameInstructions:
    def __init__(self):
        self.Text = ""
        self.Tree = tree = ET.parse("Resources/instructions.xml")
        self.Root = root = tree.getroot()

    def loadInstructions(self, instruction_number):

        if instruction_number == 0:
            self.Text = self.showMainInstructions()

        if instruction_number == 1:
            self.Text = self.showUnitInstructions()

        return self.Text

    def showUnitInstructions(self):
        self.Text = self.Root[0][0][1].text
        return self.Text

    def showMainInstructions(self):
        self.Text = self.Root[0][0][0].text
        self.Text += self.Root[0][1][0].text
        self.Text += self.Root[0][2][0].text
        self.Text += self.Root[0][3][0].text
        self.Text += self.Root[0][4][0].text

        return self.Text

    def Update(self, game: Game):
        return self.showMainInstructions

    def Draw(self, game: Game):
        pass

