import pygame


class Tile:

    def __init__(self, position, defaultMoney, enemyMoney, texture, size, units=None):
        self.Position = position
        self.DefaultMoney = defaultMoney
        self.EnemyMoney = enemyMoney
        self.Size = size
        self.Texture = texture
        self.Units = units

    def Update(self, game):
        return self


    def Draw(self, game):
        screen = game.Settings.GetScreen()
        marginX = self.Position.X * self.Size.X
        marginY = self.Position.Y * self.Size.Y

        screen.blit(self.Texture, (marginX, marginY))


        #pygame.draw.rect(screen, (255,0,0), (marginY, marginX, tile.Width, tile.Height))

        #font = pygame.font.Font(None, 40)
        #text = font.render("%s" %self.Map.index(tile), True, (255, 255, 255))
        #textRect = text.get_rect()
        #textRect.centerx = tile.Position.X * tile.Width + tile.Width / 2
        #textRect.centery = tile.Position.Y * tile.Height + tile.Height / 2

        #screen.blit(text, textRect)
