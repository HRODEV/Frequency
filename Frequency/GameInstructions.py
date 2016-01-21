import xml.etree.ElementTree as ET

class GameInstructions:
    def __init__(self):
        pass

    def loadInstructions(instruction_number):
        tree = ET.parse("Resources/instructions.xml")
        root = tree.getroot()
        text = ""

        if instruction_number == 0:
            text += root[0][0][0].text
            text += root[0][1][0].text
            text += root[0][2][0].text
            text += root[0][3][0].text
            text += root[0][4][0].text
        return text

        '''start_rule = root[0][0][0].text
        turns_moves = root[0][1][0].text
        money = root[0][2][0].text
        capturing = root[0][3][0].text
        how_to_win = root[0][4][0].text'''

