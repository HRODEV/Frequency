import pygame

from Board.Map.Tile import Tile
from Vector2 import Vector2


class IceTile(Tile):

    def __init__(self, position: Vector2, texture=None):
        texture = texture if texture is not None else pygame.image.load("images/tiles/Ice.jpg")
        super().__init__(position, 50, 100, texture)
