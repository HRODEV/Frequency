import Game
from GameLogic.Unit import UnitGroup
from Helpers import Colors
from GameLogic.Player import *

class PlayerInfoLabel:

    def GetValue(self, game:Game):
        return ""

    def Draw(self, game: Game, positionInRow):
        font = pygame.font.SysFont("Arial", 18)
        position = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2 + game.Settings.GetMapSize().X, 50)
        game.Settings.GetScreen().blit(font.render(self.GetValue(game), True, Colors.BLACK), (position.X + 30, position.Y + (positionInRow * 50)))

class PlayerName(PlayerInfoLabel):

    def GetValue(self, game:Game):
        return 'Playername: ' + str(game.Logic.PlayingPlayer.Name)

class PlayerMoney(PlayerInfoLabel):

    def GetValue(self, game:Game):
        return 'Money: ' + str(game.Logic.PlayingPlayer.Money)

class PlayerLands(PlayerInfoLabel):

    def GetValue(self, game:Game):
        return 'Units: ' # TODO: Needs logic

class PlayerTurnIncome(PlayerInfoLabel):

    def GetValue(self, game:Game):
        return 'Income this turn: ' + str(0) # TODO: Needs logic

class PlayerNextTurnIncome(PlayerInfoLabel):

    def GetValue(self, game: Game):
        return 'Income next turn: ' + str(game.Logic.GetIncome())

class PlayerRemainingMoves(PlayerInfoLabel):

    def GetValue(self, game:Game):
        return 'Remaining moves: ' + str(game.Logic.PlayingPlayer.Moves) # TODO: Needs logic

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
        #self.Options = ["Buy units", "Your money", "Lands", "Turn income", "Next turn income", "Remaining moves"]
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
        game.Settings.GetScreen().blit(font.render("Press escape to return to the ingame menu", True, Colors.BLACK), (self.Position.X+10, self.Position.Y+15))

        for i in range(0,len(self.PlayerInfoLabels)):
            self.PlayerInfoLabels[i].Draw(game, i)