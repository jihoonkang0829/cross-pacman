from enums.ghost_color import GhostColor
from typing import Tuple
from constants import (
    GHOST_BLUE_DIR,
    GHOST_ORANGE_DIR,
    GHOST_PINK_DIR,
    GHOST_MINT_DIR,
    GHOST_RED_DIR
)
from enums.tiles import Tiles
from enums.directions import Directions
import random


class Ghost:
    def __init__(self, x, y, width, height, color: GhostColor = GhostColor.RED):
        """
        Initializes the ghost object.

        Params
        ------
        x : int
            x coordinate of the ghost
        y : int
            y coordinate of the ghost
        width : int
            width of the grid
        height : int
            height of the grid
        color : GhostColor
            color enum of the ghost. Default value is GhostColor.RED

        """

        # Add more member variables if needed
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.image_dir = [image_dir for image_dir in (
            GHOST_BLUE_DIR,
            GHOST_ORANGE_DIR,
            GHOST_PINK_DIR,
            GHOST_MINT_DIR,
            GHOST_RED_DIR
        ) if str(self.color) in image_dir][0]
        self.other_ghosts = [ghost.value for ghost in (
            Tiles.GHOST_RED,
            Tiles.GHOST_BLUE,
            Tiles.GHOST_ORANGE,
            Tiles.GHOST_PINK,
            Tiles.GHOST_MINT
        ) if ghost.value != int(self.color)]

    def draw(self):
        """
        Returns the position coordinate and the directory of the image to be drawn.\\
        The function does not actually call pygame.draw method.

        Returns:
            Tuple[
                Tuple[int, int] : x, y coordinates of the ghost
                str : directory of the image to be drawn
            ]
        """
        position_tuple = (self.x, self.y)
        return (position_tuple, self.image_dir)

    def move(self, game_map):
        """
        Move the ghost based on the pacman position.

        Params
        ------
        pacman_position : Tuple[int, int]
            x, y coordinates of the pacman

        """
        direction = random.randint(0, 3)
        if direction == Directions.UP.value:
            if self.isNotWall(self.x, self.y - 1, game_map) and\
                self.isNotOtherGhost(self.x, self.y - 1, game_map):
                self.y -= 1
        elif direction == Directions.DOWN.value:
            if self.isNotWall(self.x, self.y + 1, game_map) and\
                self.isNotOtherGhost(self.x, self.y + 1, game_map):
                self.y += 1
        elif direction == Directions.LEFT.value:
            if self.isNotWall(self.x - 1, self.y, game_map) and\
                self.isNotOtherGhost(self.x - 1, self.y, game_map):
                self.x -= 1
        else:
            if self.isNotWall(self.x + 1, self.y, game_map) and\
                self.isNotOtherGhost(self.x + 1, self.y, game_map):
                self.x += 1

    def isNotWall(self, x, y, game_map):
        return game_map[x][y] != Tiles.WALL.value

    def isNotOtherGhost(self, x, y, game_map):
        return game_map[x][y] not in self.other_ghosts

    def get_position(self):
        return (self.x, self.y)
