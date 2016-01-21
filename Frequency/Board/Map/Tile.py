import pygame


class Tile:

    def __init__(self, type, position, defaultMoney, enemyMoney, texture, units=None):
        self.Type = type
        self.Position = position
        self.DefaultMoney = defaultMoney
        self.EnemyMoney = enemyMoney
        self.Texture = pygame.image.load(texture).convert()
        self.Units = units
        self.Width = 75
        self.Height = 75


    def Draw(self, game):
        screen = game.Settings.GetScreen()
        marginX = self.Position.X * self.Width
        marginY = self.Position.Y * self.Height

        screen.blit(self.Texture, (marginX, marginY))


        #pygame.draw.rect(screen, (255,0,0), (marginY, marginX, tile.Width, tile.Height))

        #font = pygame.font.Font(None, 40)
        #text = font.render("%s" %self.Map.index(tile), True, (255, 255, 255))
        #textRect = text.get_rect()
        #textRect.centerx = tile.Position.X * tile.Width + tile.Width / 2
        #textRect.centery = tile.Position.Y * tile.Height + tile.Height / 2

        #screen.blit(text, textRect)
