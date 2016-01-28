from Vector2 import Vector2


class Character:

    def __init__(self):
        self._id = id

    @property
    def Id(self) -> int:
        return 0


class ForestCharacter(Character):
    @property
    def Id(self) -> int:
        return 0

class IceCharacter(Character):
    @property
    def Id(self) -> int:
        return 1

class DesertCharacter(Character):
    @property
    def Id(self) -> int:
        return 2


class SwampCharacter(Character):
    @property
    def Id(self) -> int:
        return 3