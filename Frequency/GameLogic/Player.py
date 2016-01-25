from GameLogic.Character import *


class Player:

    def __init__(self, name=None, character=None, money=0):
        self.Name = name
        self.Character = character if character is not None else Character(character)
        self.Money = money
