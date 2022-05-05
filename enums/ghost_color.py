from enum import Enum


class GhostColor(int, Enum):
    """
    Enum for the different colors of ghosts.
    """
    RED = (4, "red")
    PINK = (5, "pink")
    ORANGE = (6, "orange")
    BLUE = (7, "blue")
    MINT = (8, "mint")

    def __new__(cls, value, description):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj._description_ = description
        return obj

    def __str__(self) -> str:
        return self._description_

    def __int__(self) -> int:
        return self._value_
