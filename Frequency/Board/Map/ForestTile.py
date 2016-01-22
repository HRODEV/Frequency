import pygame

from Board.Map.Tile import Tile
from Vector2 import Vector2


class ForestTile(Tile):

    def __init__(self, position: Vector2, size: Vector2=None, texture=None, rectangle=None):
        texture = texture if texture is not None else pygame.transform.scale(pygame.image.load('images/tiles/Forest.jpg'), [size.X, size.Y])
        size = size if size is not None else Vector2(35, 35)

        super().__init__(position, 50, 100, texture, size, rectangle)


    def Update(self, game):
        nself = super().Update(game)

        return ForestTile(nself.Position, nself.Size, nself.Texture, nself.Rectangle)
