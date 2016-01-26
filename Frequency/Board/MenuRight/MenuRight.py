import pygame
import Game
from Vector2 import Vector2
from Helpers.popup import *
from Helpers.EventHelpers import *

class MenuRight:

    def __init__(self, game, size=None, position=None):
        self.Money = 0
        self.TurnIncome = 0
        self.NextTurnIncome = 0
        self.RemainingMoves = 4
        self.Options = ["Buy units", "Your money", "Lands", "Turn income", "Next turn income", "Remaining moves"]
        self.Size = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2, game.Settings.Resolution.Y)
        self.Position = Vector2((game.Settings.Resolution.X - game.Settings.GetMapSize().X) // 2 + game.Settings.GetMapSize().X, 0)
        game.Settings.SetMenuLeftSize(self.Size)
        self.Screen = game.Settings.GetScreen()


    def Update(self, game: Game):
        return MenuRight(game, self.Size, self.Position)

    def Draw(self, game : Game):
        self.Count = 0
        self.Font = pygame.font.SysFont("Arial", 18)

        pygame.draw.rect(self.Screen,
                         (0, 0, 255),
                         (self.Position.X, self.Position.Y, self.Size.X, self.Size.Y))

        self.drawRightMenu()

    # Display the sidemenu
    def drawRightMenu(self):

        popup = Popup(self.Screen, "Message")

        # Loop through the given menu-items
        for rightMenuItem in self.Options:

            # Needed to append the items below each other (Y-axis)
            self.Count += 1

            if rightMenuItem == 'Your money':
                rightMenuItem += str(self.getMoney())

            if rightMenuItem == 'Turn income':
                rightMenuItem += str(self.getTurnIncome())

            if rightMenuItem == 'Remaining moves':
                rightMenuItem += str(self.getRemainingMoves())

            if rightMenuItem == 'Turn income':
                rightMenuItem += str(self.getTurnIncome())

            rectangle = self.Screen.blit(self.Font.render(rightMenuItem, True, (255, 255, 255)), (self.Position.X + 30, self.Position.Y + (self.Count * 50)))

    # Setters and getters
    def getMoney(self):
        return self.Money

    def setMoney(self, newMoney):
        self.Money = newMoney

    def getTurnIncome(self):
        return self.TurnIncome

    def setTurnIncome(self, newTurnIncome):
        self.TurnIncome = newTurnIncome

    def getNextTurnIncome(self):
        return self.NextTurnIncome

    def setNextTurnIncome(self, newTurnIncome):
        self.NextTurnIncome = newTurnIncome

    def getRemainingMoves(self):
        return self.RemainingMoves

