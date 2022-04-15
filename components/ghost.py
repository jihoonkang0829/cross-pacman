from enums.ghost_color import GhostColor
from typing import Tuple
from constants import (
    GHOST_BLUE_DIR,
    GHOST_ORANGE_DIR,
    GHOST_PINK_DIR,
    GHOST_MINT_DIR,
    GHOST_RED_DIR
)


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
        self.image_dir = (image_dir for image_dir in (
            GHOST_BLUE_DIR,
            GHOST_ORANGE_DIR,
            GHOST_PINK_DIR,
            GHOST_MINT_DIR,
            GHOST_RED_DIR
        ) if self.color.value in image_dir)[0]

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
        raise NotImplementedError("Ghost.draw() is not implemented.")

    def move(self, pacman_position: Tuple[int, int]):
        """
        Move the ghost based on the pacman position.

        Params
        ------
        pacman_position : Tuple[int, int]
            x, y coordinates of the pacman

        """
        raise NotImplementedError("Ghost.move() is not implemented.")

    def get_position(self):
        return (self.x, self.y)

    # Add more functions if needed
