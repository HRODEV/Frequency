import pygame
from Board.Map.Tile import *
from Vector2 import Vector2

class Map:

    def __init__(self, resolution):
        self.Resolution = resolution
        self.Map = None
        self.maxTilesX = None
        self.maxTilesY = None

        self.GenerateMap()


    def GenerateMap(self):
        tileForProperties = Tile(0, 0, 0, 100, 150, None)
        self.maxTilesX = self.Resolution.X // tileForProperties.Width
        self.maxTilesY = self.Resolution.Y // tileForProperties.Height
        map = []
        X = 0
        Y = 0

        for Y in range(0, self.maxTilesX):
            for X in range(0, self.maxTilesY):
                map.append(Tile(0, Vector2(X, Y), 100, 150, "images/tiles/Swamp.jpg"))

        self.Map = map


    def Update(self):
        return self


    def Draw(self, game):
        for tile in self.Map:
            screen = game.Settings.GetScreen()
            # Logo position
            marginX = tile.Position.X * tile.Width
            marginY = tile.Position.Y * tile.Height
            position = (marginX, marginY)


            img = pygame.transform.scale(pygame.image.load(tile.Texture), [tile.Width, tile.Height])
            game.Settings.GetScreen().blit(img, (marginX, marginY))

            #pygame.draw.rect(screen, (255,0,0), (marginY, marginX, tile.Width, tile.Height))

            #font = pygame.font.Font(None, 40)
            #text = font.render("%s" %self.Map.index(tile), True, (255, 255, 255))
            #textRect = text.get_rect()
            #textRect.centerx = tile.Position.X * tile.Width + tile.Width / 2
            #textRect.centery = tile.Position.Y * tile.Height + tile.Height / 2

            #screen.blit(text, textRect)
