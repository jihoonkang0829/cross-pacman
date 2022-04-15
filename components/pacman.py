from pygame import event
from typing import Tuple
from enums.directions import Directions

# Pacman class


class Pacman:
    def __init__(self, x, y, width, height, direction=Directions.RIGHT):
        """
        Initializes the pacman object.

        Params
        ------
        x : int
            x coordinate of the pacman
        y : int
            y coordinate of the pacman
        width : int
            width of the grid
        height : int
            height of the grid
        direction : Directions
            direction enum of the pacman. Default value is Directions.RIGHT
        """

        # Add more member variables if needed
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.game_running = True

    def move(self, event: event):
        """
        Move the pacman based on the user input.

        Params
        ------
        event : pygame.event
            event object from pygame. This is used to check which key is pressed from the user.
        """
        raise NotImplementedError("Pacman.move() is not implemented.")

    def draw(self) -> Tuple[Tuple[int, int], str]:
        """
        Returns the position coordinate and the directory of the image to be drawn.\\
        The function does not actually call pygame.draw method.

        Returns:
            Tuple[
                Tuple[int, int] : x, y coordinates of the pacman
                str : directory of the image to be drawn
            ]
        """
        raise NotImplementedError("Pacman.draw() is not implemented.")

    def get_position(self) -> Tuple[int, int]:
        return (self.x, self.y)

    def get_direction(self) -> Directions:
        return self.direction

    def set_direction(self, direction: Directions):
        self.direction = direction

    def is_game_end(self) -> bool:
        """
        Returns True if the game is over.
        """
        return not self.game_running

    # Add more member methods below.
