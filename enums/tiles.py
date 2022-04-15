from enum import Enum


class Tiles(Enum):
    """
    Enum for the different tiles in the game.
    """
    EMPTY = 0
    WALL = 1
    PLAYER = 2
    DOT = 3

    GHOST_RED = 4
    GHOST_PINK = 5
    GHOST_ORANGE = 6
    GHOST_BLUE = 7
    GHOST_MINT = 8

    APPLE = 9
    STRAWBERRY = 10
