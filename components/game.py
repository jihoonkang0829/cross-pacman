# Game component of the pacman game.
import pygame
from typing import List
from pygame.locals import *
from components.ghost import Ghost
from components.pacman import Pacman
from constants import APPLE_DIR, BACKGROUND_COLOR, DOT_DIR, GRID_SIZE, MAP_DIR, STRAWBERRY_DIR, WALL_COLOR
from enums.ghost_color import GhostColor
from enums.tiles import Tiles
import numpy as np



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
        self.gameDisplay = pygame.display.set_mode((width,height))

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
        self.gameDisplay.fill(BACKGROUND_COLOR)
        ghost0_coord, ghost0_dir = self.ghosts[0].draw()
        ghost1_coord, ghost1_dir = self.ghosts[1].draw()
        ghost2_coord, ghost2_dir = self.ghosts[2].draw()
        ghost3_coord, ghost3_dir = self.ghosts[3].draw()
        ghost4_coord, ghost4_dir = self.ghosts[4].draw()
        pacman_coord, pacman_dir = self.pacman.draw()
        boardarray = np.loadtxt(MAP_DIR, dtype=int)
        for y in range( boardarray.shape[0] ):
            for x in range( boardarray.shape[1] ):
                # draw tile at (x,y)
                id = boardarray[x,y]        # id of tile indicates which sprite to be printed on game
                if id == Tiles.WALL:        # if id is wall, print wall on designated grid
                    wall = Rect( x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE )
                    pygame.draw.rect( self.gameDisplay, WALL_COLOR, wall )
                elif id == Tiles.APPLE:
                    applecoord = [x * GRID_SIZE, y * GRID_SIZE]
                    self.gameDisplay.blit(pygame.image.load(APPLE_DIR), applecoord)
                elif id == Tiles.STRAWBERRY:
                    strawcoord = [x * GRID_SIZE, y * GRID_SIZE]
                    self.gameDisplay.blit(pygame.image.load(STRAWBERRY_DIR), strawcoord)
                elif id == Tiles.DOT:
                    dotcoord = [x * GRID_SIZE, y * GRID_SIZE]
                    self.gameDisplay.blit(pygame.image.load(DOT_DIR), dotcoord)
                elif id == Tiles.GHOST_RED:
                    self.gameDisplay.blit(pygame.image.load(ghost0_dir), ghost0_coord*GRID_SIZE)
                elif id == Tiles.GHOST_PINK:
                    self.gameDisplay.blit(pygame.image.load(ghost1_dir), ghost1_coord*GRID_SIZE)
                elif id == Tiles.GHOST_ORANGE:
                    self.gameDisplay.blit(pygame.image.load(ghost2_dir), ghost2_coord*GRID_SIZE)
                elif id == Tiles.GHOST_BLUE:
                    self.gameDisplay.blit(pygame.image.load(ghost3_dir), ghost3_coord*GRID_SIZE)
                elif id == Tiles.GHOST_MINT:
                    self.gameDisplay.blit(pygame.image.load(ghost4_dir), ghost4_coord*GRID_SIZE)
                elif id == Tiles.PLAYER:
                    self.gameDisplay.blit(pygame.image.load(pacman_dir), pacman_coord)

        #raise NotImplementedError("Game.draw() is not implemented.")

    def handle_events(self, events: List[pygame.event]):
        """
        Handles events for the game.

        Params
        ------
        events : List[pygame.event]
            list of events to be handled

        """
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                self.pacman.set_direction(Directions.LEFT)
            elif events.key == pygame.K_RIGHT:
                self.pacman.set_direction(Directions.RIGHT)
            elif events.key == pygame.K_UP:
                self.pacman.set_direction(Directions.UP)
            elif events.key == pygame.K_DOWN:
                self.pacman.set_direction(Directions.DOWN)
            elif events.key == pygame.K_ESCAPE
                pygame.quit()

    def update(self):
        """
        Updates the game state.
        """
        self.pacman.update()
        self.ghosts[0].update()
        self.ghosts[1].update()
        self.ghosts[2].update()
        self.ghosts[3].update()
        self.ghosts[4].update()

