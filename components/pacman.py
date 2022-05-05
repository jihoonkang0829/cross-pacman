import pygame
from pygame import event
from typing import Tuple
from enums.directions import Directions
from constants import (PACMAN_DOWN_1_DIR, PACMAN_LEFT_1_DIR, PACMAN_RIGHT_1_DIR, PACMAN_UP_1_DIR)

# Pacman class


class Pacman:
    def __init__(self, x, y, width, height, direction=Directions.RIGHT, position):
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
        self.position = position
        self.directory = (directory for directory in (
            PACMAN_DOWN_1_DIR,
            PACMAN_LEFT_1_DIR,
            PACMAN_RIGHT_1_DIR,
            PACMAN_UP_1_DIR
        ) if self.direction.value in directory)[0]

    def move(self, event: event):
        """
        Move the pacman based on the user input.
        Params
        ------
        event : pygame.event
            event object from pygame. This is used to check which key is pressed from the user.
        """
        for event in pygame.event.get():
            if keys[pygame.K_LEFT] and x>0:
                self.x -= 1
            if keys[pygame.K_RIGHT] and x<width:
                self.x += 1
            if keys[pygame.K_UP] and y>0:
                self.y += 1
            if keys[pygame.K_DOWN] and y<height:
                self.y -= 1
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
        position_coord = Tuple(self.x,self.y)
        return (position_coord, self.directory)

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