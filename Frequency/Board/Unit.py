import pygame

_stextures = []
def soldierTextures():
    if _stextures == []:
        _stextures.append(pygame.transform.scale(pygame.image.load('images/units/soldierGreen.png').convert_alpha(), [35, 35]))
        _stextures.append(pygame.transform.scale(pygame.image.load('images/units/soldierBlue.png').convert_alpha(), [35, 35]))
        _stextures.append( pygame.transform.scale(pygame.image.load('images/units/soldierYellow.png').convert_alpha(), [35, 35]))
        _stextures.append(pygame.transform.scale(pygame.image.load('images/units/soldierRed.png').convert_alpha(), [35, 35]))
    return _stextures


class Unit:

    def __init__(self, player, tile, textures, size, logicUnit):
        self.Player = player
        self.Tile = tile
        self.Textures = textures
        self.Size = size
        self.LogicUnit = logicUnit

    def Update(self, game):
        return self

    def Draw(self, game):
        test = pygame.transform.scale(self.Textures[self.Player.Character.Id], [self.Size, self.Size])
        game.Settings.GetScreen().blit(test, (self.Tile.Position.X * self.Size + game.Settings.GetMenuLeftSize().X,
                                              self.Tile.Position.Y * self.Size))


class Soldier(Unit):
    def __init__(self, player, tile, size, logicUnit):
        self.Textures = soldierTextures()
        self.Cost = 100

        super().__init__(player, tile, self.Textures, size, logicUnit)


class UnitGroup(Unit):

    def __init__(self, player, tile, size, logicUnit):
        super().__init__(player, tile, None, size, logicUnit)
        self._Units = [self._getPossibleUnit(lunit) for lunit in logicUnit.Units]

    def _getPossibleUnit(self, lunit):
        import GameLogic.Unit
        if type(lunit) is GameLogic.Unit.Soldier:
            return Soldier(lunit.Owner, self, self.Size, lunit)
        # TODO after implementing the rest of the graphical units
        elif type(lunit) is GameLogic.Unit.Boat:
            return None
        elif type(lunit) is GameLogic.Unit.Robot:
            return None
        elif type(lunit) is GameLogic.Unit.Tank:
            return None

    def Draw(self, game):
        for i in range(0,len(self._Units)):
            test = pygame.transform.scale(self._Units[i].Textures[self.Player.Character.Id], [self.Size//2, self.Size//2])
            game.Settings.GetScreen().blit(test, (self.Tile.Position.X * self.Size + game.Settings.GetMenuLeftSize().X + (self.Size//2) * (i//2),
                                                self.Tile.Position.Y * self.Size + (self.Size//2) * (i%2)))