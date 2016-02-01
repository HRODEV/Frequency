import pygame

_soldier_textures = []
def SoldierTextures():
    if _soldier_textures == []:
        _soldier_textures.append(pygame.transform.scale(pygame.image.load('images/units/soldierGreen.png').convert_alpha(), [35, 35]))
        _soldier_textures.append(pygame.transform.scale(pygame.image.load('images/units/soldierBlue.png').convert_alpha(), [35, 35]))
        _soldier_textures.append( pygame.transform.scale(pygame.image.load('images/units/soldierYellow.png').convert_alpha(), [35, 35]))
        _soldier_textures.append(pygame.transform.scale(pygame.image.load('images/units/soldierRed.png').convert_alpha(), [35, 35]))
    return _soldier_textures

_robot_textures = []
def RobotTextures():
    if _robot_textures == []:
        _robot_textures.append(pygame.transform.scale(pygame.image.load('images/units/robotGreen.png').convert_alpha(), [35, 35]))
        _robot_textures.append(pygame.transform.scale(pygame.image.load('images/units/robotBlue.png').convert_alpha(), [35, 35]))
        _robot_textures.append( pygame.transform.scale(pygame.image.load('images/units/robotYellow.png').convert_alpha(), [35, 35]))
        _robot_textures.append(pygame.transform.scale(pygame.image.load('images/units/robotRed.png').convert_alpha(), [35, 35]))
    return _robot_textures

_tank_textures = []
def TankTextures():
    if _tank_textures == []:
        _tank_textures.append(pygame.transform.scale(pygame.image.load('images/units/tankGreen.png').convert_alpha(), [35, 35]))
        _tank_textures.append(pygame.transform.scale(pygame.image.load('images/units/tankBlue.png').convert_alpha(), [35, 35]))
        _tank_textures.append( pygame.transform.scale(pygame.image.load('images/units/tankYellow.png').convert_alpha(), [35, 35]))
        _tank_textures.append(pygame.transform.scale(pygame.image.load('images/units/tankRed.png').convert_alpha(), [35, 35]))
    return _tank_textures

_boat_textures = []
def BoatTextures():
    if _boat_textures == []:
        _boat_textures.append(pygame.transform.scale(pygame.image.load('images/units/shipGreen.png').convert_alpha(), [35, 35]))
        _boat_textures.append(pygame.transform.scale(pygame.image.load('images/units/shipBlue.png').convert_alpha(), [35, 35]))
        _boat_textures.append( pygame.transform.scale(pygame.image.load('images/units/shipYellow.png').convert_alpha(), [35, 35]))
        _boat_textures.append(pygame.transform.scale(pygame.image.load('images/units/shipRed.png').convert_alpha(), [35, 35]))
    return _boat_textures


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
        self.Textures = SoldierTextures()

        super().__init__(player, tile, self.Textures, size, logicUnit)


class Robot(Unit):
    def __init__(self, player, tile, size, logicUnit):
        self.Textures = RobotTextures()

        super().__init__(player, tile, self.Textures, size, logicUnit)


class Tank(Unit):
    def __init__(self, player, tile, size, logicUnit):
        self.Textures = TankTextures()

        super().__init__(player, tile, self.Textures, size, logicUnit)


class Boat(Unit):
    def __init__(self, player, tile, size, logicUnit):
        self.Textures = BoatTextures()

        super().__init__(player, tile, self.Textures, size, logicUnit)


class UnitGroup(Unit):

    def __init__(self, player, tile, size, logicUnit):
        super().__init__(player, tile, None, size, logicUnit)
        self._Units = [self._getPossibleUnit(lunit) for lunit in logicUnit.Units]

    def _getPossibleUnit(self, lunit):
        import GameLogic.Unit
        if type(lunit) is GameLogic.Unit.Soldier:
            return Soldier(lunit.Owner, self, self.Size, lunit)
        elif type(lunit) is GameLogic.Unit.Boat:
            return Boat(lunit.Owner, self, self.Size, lunit)
        elif type(lunit) is GameLogic.Unit.Robot:
            return Robot(lunit.Owner, self, self.Size, lunit)
        elif type(lunit) is GameLogic.Unit.Tank:
            return Tank(lunit.Owner, self, self.Size, lunit)

    def Draw(self, game):
        for i in range(0,len(self._Units)):
            unitTexture = pygame.transform.scale(self._Units[i].Textures[self.Player.Character.Id], [self.Size//2, self.Size//2])
            game.Settings.GetScreen().blit(unitTexture, (self.Tile.Position.X * self.Size + game.Settings.GetMenuLeftSize().X + (self.Size//2) * (i//2),
                                                self.Tile.Position.Y * self.Size + (self.Size//2) * (i%2)))