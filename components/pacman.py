import pygame
from pygame import event
from typing import Tuple
from enums.directions import Directions
from constants import (PACMAN_DOWN_1_DIR, PACMAN_LEFT_1_DIR, PACMAN_RIGHT_1_DIR, PACMAN_UP_1_DIR)
from enums.tiles import Tiles

# Pacman class


class Pacman:
    def __init__(self, x, y, width, height, boardarray, direction=Directions.RIGHT):
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
        boardarray : np.ndarray
            2d numpy array of the board
        direction : Directions
            direction enum of the pacman. Default value is Directions.RIGHT
        """

        # Add more member variables if needed
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.position = (x, y)
        self.boardarray = boardarray

        self.direction_image_map = {
            Directions.UP: PACMAN_UP_1_DIR,
            Directions.DOWN: PACMAN_DOWN_1_DIR,
            Directions.LEFT: PACMAN_LEFT_1_DIR,
            Directions.RIGHT: PACMAN_RIGHT_1_DIR
        }

        self.directory = self.direction_image_map[self.direction]

    def move(self, event: event):
        """
        Move the pacman based on the user input.
        Params
        ------
        event : pygame.event
            event object from pygame. This is used to check which key is pressed from the user.
        """
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT and 
            0 <= self.x - 1 < self.width and
            self.boardarray[self.y][self.x - 1] != Tiles.WALL.value):
                self.x -= 1

            elif (event.key == pygame.K_RIGHT and
            0 <= self.x + 1 < self.width and
            self.boardarray[self.y][self.x + 1] != Tiles.WALL.value):
                self.x += 1

            elif (event.key == pygame.K_UP and
            0 <= self.y - 1 < self.height and
            self.boardarray[self.y - 1][self.x] != Tiles.WALL.value):
                self.y -= 1

            elif (event.key == pygame.K_DOWN and
            0 <= self.y + 1 < self.height and
            self.boardarray[self.y + 1][self.x] != Tiles.WALL.value):
                self.y += 1

        self.position = (self.x, self.y)

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
        return (self.position, self.directory)

    def get_position(self) -> Tuple[int, int]:
        return self.position

    def get_direction(self) -> Directions:
        return self.direction

    def set_direction(self, direction: Directions):
        self.direction = direction
