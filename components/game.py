# Game component of the pacman game.
import pygame
from typing import List
from components.ghost import Ghost
from components.pacman import Pacman
from enums.ghost_color import GhostColor


class Game:
    def __init__(self, width, height):
        """
        Initializes the game object.

        Params
        ------
        width : int
            width of the grid
        height : int
            height of the grid

        """
        # Add more member variables if needed
        self.width = width
        self.height = height
        self.score = 0
        self.lives = 3
        self.level = 1

        # TODO: Modify initial position coordinates of the pacman and the ghosts
        self.pacman = Pacman(
            x=self.width // 2,
            y=self.height // 2,
            width=self.width,
            height=self.height,
        )
        self.ghosts = [
            Ghost(
                x=self.width // 2,
                y=self.height // 2,
                width=self.width,
                height=self.height,
                color=GhostColor.RED,
            ),
            Ghost(
                x=self.width // 2,
                y=self.height // 2,
                width=self.width,
                height=self.height,
                color=GhostColor.PINK,
            ),
            Ghost(
                x=self.width // 2,
                y=self.height // 2,
                width=self.width,
                height=self.height,
                color=GhostColor.ORANGE,
            ),
            Ghost(
                x=self.width // 2,
                y=self.height // 2,
                width=self.width,
                height=self.height,
                color=GhostColor.BLUE,
            ),
            Ghost(
                x=self.width // 2,
                y=self.height // 2,
                width=self.width,
                height=self.height,
                color=GhostColor.MINT,
            ),
        ]
        self.dots = []
        self.strawberries = []
        self.apples = []
        self.walls = []

    def draw(self):
        """
        Draws each tile of the grid, using the draw method of pacman and ghost
        """
        self.ghosts[0].draw()
        self.ghosts[1].draw()
        self.ghosts[2].draw()
        self.ghosts[3].draw()
        self.ghosts[4].draw()
        self.pacman.draw()
        
        #raise NotImplementedError("Game.draw() is not implemented.")

    def handle_events(self, events: List[pygame.event]):
        """
        Handles events for the game.

        Params
        ------
        events : List[pygame.event]
            list of events to be handled

        """
        raise NotImplementedError("Game.handle_events() is not implemented.")

    def update(self):
        """
        Updates the game state.
        """
        raise NotImplementedError("Game.update() is not implemented.")
