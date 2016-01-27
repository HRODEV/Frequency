import pygame
from GameLogic.Character import *


class Player:

    def __init__(self, name=None, character=None, money=None, moves=None):
        self.Name = name
        self.Character = character if character is not None else Character(character)
        self.Money = money if money is not None else 0
        self.Moves = moves if moves is not None else 0

    def Update(self):
        return Player(self.Name, self.Character, self.Money)