import pygame
from GameLogic.Character import *


class Player:

    def __init__(self, name, character, money=500, moves=4):
        self.Name = name
        self.Character = character if type(character) is not int else Character(character)
        self.Money = money
        self.Moves = moves

    def Update(self):
        return Player(self.Name, self.Character, self.Money, self.Moves)