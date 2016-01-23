import pygame

class Unit:

    def __init__(self, player, tile):
        self.Player = player
        self.Tile = tile


    def Update(self, game):
        return self


    def Draw(self, game):
        print("Drawed")