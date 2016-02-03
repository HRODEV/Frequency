import Game
from GameLogic.Unit import UnitGroup
from Helpers import Colors
from GameLogic.Player import *

class PlayerInfoLabel:

    def PlayerIndicator(self, game: Game, current_player = None, color = None):

        current_player = game.Logic.PlayingPlayer.Name

        if current_player == 'Player0':
            color = Colors.PLAYER_GREEN
        elif current_player == 'Player1':
            color = Colors.PLAYER_BLUE
        elif current_player == 'Player2':
            color = Colors.PLAYER_YELLOW
        elif current_player == 'Player3':
            color = Colors.PLAYER_RED
        return color

    def GetValue(self, game:Game):
        return ""

    def Draw(self, game: Game, positionInRow):
        color = self.PlayerIndicator(game)
        font = pygame.font.SysFont("Arial", 24)
        position = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2 + game.Settings.GetMapSize().X, 50)
        pygame.draw.rect(game.Settings.GetScreen(), color, pygame.Rect(position.X, position.Y + 400, 400, 50))
        game.Settings.GetScreen().blit(font.render("Turn: " + str(game.Logic.PlayingPlayer.Name), True, Colors.WHITE), (position.X + 100, position.Y + 400))
        game.Settings.GetScreen().blit(font.render(self.GetValue(game), True, Colors.BLACK), (position.X + 30, position.Y + (positionInRow * 50)))

class PlayerName(PlayerInfoLabel):

    def GetValue(self, game:Game):
        return 'Playername: ' + str(game.Logic.PlayingPlayer.Name)

class PlayerMoney(PlayerInfoLabel):

    def GetValue(self, game:Game):
        return 'Money: ' + str(game.Logic.PlayingPlayer.Money)

class PlayerNextTurnIncome(PlayerInfoLabel):

    def GetValue(self, game: Game):
        return 'Income next turn: ' + str(game.Logic.GetIncome())

class PlayerRemainingMoves(PlayerInfoLabel):

    def GetValue(self, game:Game):
        return 'Remaining moves: ' + str(game.Logic.PlayingPlayer.Moves)

class PlayerTotalUnits(PlayerInfoLabel):

    def GetValue(self, game:Game):
        units = game.Logic.PlayingPlayer.Units
        totalUnits = 0

        for unit in units:
            if type(unit) is not UnitGroup:
                totalUnits += 1
        return 'Total units: ' + str(totalUnits)

class MenuRight:

    def __init__(self, game, size=None, position=None, playerInfoLabels = None):
        self.Size = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2, game.Settings.Resolution.Y)
        self.Position = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2 + game.Settings.GetMapSize().X, 0)

        self.PlayerInfoLabels = playerInfoLabels if playerInfoLabels is not None \
            else [PlayerName(), PlayerMoney(), PlayerTotalUnits(), PlayerNextTurnIncome(), PlayerRemainingMoves()]

    def Update(self, game: Game):
        return MenuRight(game, self.Size, self.Position)

    def Draw(self, game : Game):
        pygame.draw.rect(game.Settings.GetScreen(),
                         (255, 255, 255),
                         (self.Position.X, self.Position.Y, self.Size.X, self.Size.Y))
        font = pygame.font.Font(None, 20)
        game.Settings.GetScreen().blit(font.render("Press ESC for the menu", True, Colors.BLACK), (self.Position.X+10, self.Position.Y+15))

        for i in range(0,len(self.PlayerInfoLabels)):
            self.PlayerInfoLabels[i].Draw(game, i)