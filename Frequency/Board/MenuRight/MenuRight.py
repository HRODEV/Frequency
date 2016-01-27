import pygame
import Game
from Helpers import Colors
from Vector2 import Vector2
from Helpers.popup import *
from Helpers.EventHelpers import *
from GameLogic.Player import *

class PlayerInfoLabel:

    def GetValue(self, player:Player):
        return ""

    def Draw(self, game: Game, positionInRow, player=None):
        font = pygame.font.SysFont("Arial", 18)
        position = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2 + game.Settings.GetMapSize().X, 50)
        game.Settings.GetScreen().blit(font.render(self.GetValue(player), True, Colors.WHITE), (position.X + 30, position.Y + (positionInRow * 50)))

class PlayerMoney(PlayerInfoLabel):

    def GetValue(self, player:Player):
        return 'Money: ' + str(0)

class PlayerLands(PlayerInfoLabel):

    def GetValue(self, player:Player):
        return 'Units: ' # TODO: Needs logic

class PlayerTurnIncome(PlayerInfoLabel):

    def GetValue(self, player:Player):
        return 'Income this turn: ' + str(0) # TODO: Needs logic

class PlayerNextTurnIncome(PlayerInfoLabel):

    def GetValue(self, player:Player):
        return 'Income next turn: ' + str(0) # TODO: Needs logic

class PlayerRemainingMoves(PlayerInfoLabel):

    def GetValue(self, player:Player):
        return 'Remaining moves: ' + str(0) # TODO: Needs logic

class MenuRight:

    def __init__(self, game, size=None, position=None, playerInfoLabels = None):
        #self.Options = ["Buy units", "Your money", "Lands", "Turn income", "Next turn income", "Remaining moves"]
        self.Size = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2, game.Settings.Resolution.Y)
        self.Position = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2 + game.Settings.GetMapSize().X, 0)

        self.PlayerInfoLabels = playerInfoLabels if playerInfoLabels is not None \
            else [PlayerMoney(), PlayerLands(), PlayerNextTurnIncome(), PlayerNextTurnIncome(), PlayerRemainingMoves()]

    def Update(self, game: Game):
        return MenuRight(game, self.Size, self.Position)

    def Draw(self, game : Game):
        pygame.draw.rect(game.Settings.GetScreen(),
                         (0, 0, 255),
                         (self.Position.X, self.Position.Y, self.Size.X, self.Size.Y))

        for i in range(0,len(self.PlayerInfoLabels)):
            self.PlayerInfoLabels[i].Draw(game, i)