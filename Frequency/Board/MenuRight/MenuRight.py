import pygame

import Game
from GameLogic.Unit import UnitGroup
from Helpers import Colors
from Vector2 import Vector2


class PlayerInfoLabel:
    def PlayerIndicator(self, game: Game):

        ID = game.Logic.PlayingPlayer.Character.Id

        if ID == 0:
            return Colors.PLAYER_GREEN
        elif ID == 1:
            return Colors.PLAYER_BLUE
        elif ID == 2:
            return Colors.PLAYER_YELLOW
        elif ID == 3:
            return Colors.PLAYER_RED

    def GetValue(self, game: Game):
        return ""

    def Draw(self, game: Game, positionInRow):
        color = self.PlayerIndicator(game)
        font = pygame.font.SysFont("Arial", 20)
        position = Vector2(
            (game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2 + game.Settings.GetMapSize().X, 50)
        pygame.draw.rect(game.Settings.GetScreen(), color, pygame.Rect(position.X, position.Y + 400, 400, 50))
        game.Settings.GetScreen().blit(font.render("Turn: " + str(game.Logic.PlayingPlayer.Name), True, Colors.WHITE),
                                       (position.X + 100, position.Y + 400))
        game.Settings.GetScreen().blit(font.render(self.GetValue(game), True, Colors.BLACK),
                                       (position.X + 30, position.Y + (positionInRow * 50)))


class PlayerName(PlayerInfoLabel):
    def GetValue(self, game: Game):
        return 'Playername: ' + str(game.Logic.PlayingPlayer.Name)


class PlayerMoney(PlayerInfoLabel):
    def GetValue(self, game: Game):
        return 'Money: ' + str(game.Logic.PlayingPlayer.Money)


class PlayerNextTurnIncome(PlayerInfoLabel):
    def GetValue(self, game: Game):
        return 'Income next turn: ' + str(game.Logic.GetIncome())


class PlayerRemainingMoves(PlayerInfoLabel):
    def GetValue(self, game: Game):
        return 'Remaining moves: ' + str(game.Logic.PlayingPlayer.Moves)


class PlayerTotalUnits(PlayerInfoLabel):
    def GetValue(self, game: Game):
        units = game.Logic.PlayingPlayer.Units
        totalUnits = 0

        for unit in units:
            if type(unit) is not UnitGroup:
                totalUnits += 1
        return 'Total units: ' + str(totalUnits)


class MenuRight:
    def __init__(self, game, playerInfoLabels=None):
        self.Size = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2,
                            game.Settings.Resolution.Y)
        self.Position = Vector2(
            (game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2 + game.Settings.GetMapSize().X, 0)

        self.PlayerInfoLabels = playerInfoLabels if playerInfoLabels is not None \
            else [PlayerName(), PlayerMoney(), PlayerTotalUnits(), PlayerNextTurnIncome(), PlayerRemainingMoves()]

    def Update(self, game: Game):
        return MenuRight(game, self.PlayerInfoLabels)

    def Draw(self, game: Game):
        pygame.draw.rect(game.Settings.GetScreen(),
                         (255, 255, 255),
                         (self.Position.X, self.Position.Y, self.Size.X, self.Size.Y))
        font = pygame.font.Font(None, 20)
        game.Settings.GetScreen().blit(font.render("Press ESC for the menu", True, Colors.BLACK),
                                       (self.Position.X + 10, self.Position.Y + 15))

        for i in range(0, len(self.PlayerInfoLabels)):
            self.PlayerInfoLabels[i].Draw(game, i)
