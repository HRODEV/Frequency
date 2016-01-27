import pygame

from Board.Map.Tile import Tile
from Vector2 import Vector2


class ForestTile(Tile):

    def __init__(self, position: Vector2, size: Vector2=Vector2(35, 35), units=None, texture=None, rectangle=None, building=None):
        texture = texture if texture is not None else pygame.transform.scale(pygame.image.load('images/tiles/ForestSeamless.png'), [size.X, size.Y])


        super().__init__(position, 50, 100, texture, size, units, rectangle, building)


    def Update(self, game):
        nself = super().Update(game)

        return ForestTile(nself.Position, nself.Size, nself.Units, nself.Texture, nself.Rectangle, nself.Building)
