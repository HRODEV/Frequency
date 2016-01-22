import pygame

from Board.Map.Tile import Tile
from Vector2 import Vector2


class SeaTile(Tile):

    def __init__(self, position: Vector2, texture=None, size: Vector2=Vector2(35 ,35)):
        texture = texture if texture is not None else pygame.image.load("images/tiles/Sea.jpg")
        super().__init__(position, 50, 100, texture, size)
