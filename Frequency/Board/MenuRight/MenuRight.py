import pygame
import Game
from Vector2 import Vector2
from Helpers.popup import *
from Helpers.EventHelpers import *
from GameLogic.Player import import *

class playerInfoLabels:
    def __init__(self):
        pass

class PlayerMoney(playerInfoLabels):
    def __init__(self, player):
        self.Player = player

    def GetValue(self):
        return 'Money: ' + str(self.Player.Money)

class PlayerLands(playerInfoLabels):
    def __init__(self, player):
        self.Player = player

    def getValue(self):
        return 'Units: ' # TODO: Needs logic

class PlayerTurnIncome(playerInfoLabels):
    def __init__(self, player):
        self.Player = player

    def getValue(self):
        return 'Income this turn: ' + str(0) # TODO: Needs logic

class PlayerNextTurnIncome(playerInfoLabels):
    def __init__(self, player):
        self.Player = player

    def getValue(self):
        return 'Income this turn: ' + str(0) # TODO: Needs logic

class PlayerRemainingMoves(playerInfoLabels):
    def __init__(self, player):
        self.Player = player

    def getValue(self):
        return 'Remaining moves: ' + str(0) # TODO: Needs logic


class MenuRight:

    def __init__(self, game, size=None, position=None):
        #self.Options = ["Buy units", "Your money", "Lands", "Turn income", "Next turn income", "Remaining moves"]
        self.Size = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2, game.Settings.Resolution.Y)
        self.Position = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2 + game.Settings.GetMapSize().X, 0)
        game.Settings.SetMenuLeftSize(self.Size)
        self.Screen = game.Settings.GetScreen()

    def Update(self, game: Game):
        return MenuRight(game, self.Size, self.Position)

    def Draw(self, game : Game):
        self.Font = pygame.font.SysFont("Arial", 18)

        pygame.draw.rect(self.Screen,
                         (0, 0, 255),
                         (self.Position.X, self.Position.Y, self.Size.X, self.Size.Y))