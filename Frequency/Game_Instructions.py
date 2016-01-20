import xml.etree.ElementTree as ET

class GameInstructions:
    def __init__(self):
        self.loadInstructions()

    def loadInstructions():
        tree = ET.parse("Resources/instructions.xml")
        root = tree.getroot()

        for child in root:
            print(child.tag, child.attrib)