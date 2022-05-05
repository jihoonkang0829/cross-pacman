# Game component of the pacman game.
import pygame
import sys
from typing import List
from pygame.locals import *
from components.ghost import Ghost
from components.pacman import Pacman
from constants import (APPLE_DIR, BACKGROUND_COLOR, DOT_DIR, GRID_SIZE, MAP_DIR,
                       STRAWBERRY_DIR, WALL_COLOR, STRAWBERRY_POINT, APPLE_POINT, DOT_POINT,
                       PACMAN_INIT_X, PACMAN_INIT_Y, GHOST_RED_INIT_X, GHOST_RED_INIT_Y,
                       GHOST_BLUE_INIT_X, GHOST_BLUE_INIT_Y, GHOST_MINT_INIT_X, GHOST_MINT_INIT_Y,
                       GHOST_PINK_INIT_X, GHOST_PINK_INIT_Y, GHOST_ORANGE_INIT_X,
                       GHOST_ORANGE_INIT_Y)
from enums.ghost_color import GhostColor
from enums.tiles import Tiles
import numpy as np


class Game:
    def __init__(self, screen, width, height):
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
        self.screen = screen
        self.score = 0
        self.lives = 3
        self.level = 1
        self.boardarray = np.loadtxt(MAP_DIR, dtype=int).transpose()
        self.game_win = False
        self.game_over = False

        self.pacman = Pacman(
            x= PACMAN_INIT_X,
            y= PACMAN_INIT_Y,
            width=self.width,
            height=self.height,
            boardarray=self.boardarray

        )
        self.ghosts = {
            GhostColor.RED:
            Ghost(
                x=GHOST_RED_INIT_X,
                y=GHOST_RED_INIT_Y,
                width=self.width,
                height=self.height,
                color=GhostColor.RED,
            ),
            GhostColor.PINK:
            Ghost(
                x=GHOST_PINK_INIT_X,
                y=GHOST_PINK_INIT_Y,
                width=self.width,
                height=self.height,
                color=GhostColor.PINK,
            ),
            GhostColor.ORANGE:
            Ghost(
                x=GHOST_ORANGE_INIT_X,
                y=GHOST_ORANGE_INIT_Y,
                width=self.width,
                height=self.height,
                color=GhostColor.ORANGE,
            ),
            GhostColor.BLUE:
            Ghost(
                x=GHOST_BLUE_INIT_X,
                y=GHOST_BLUE_INIT_Y,
                width=self.width,
                height=self.height,
                color=GhostColor.BLUE,
            ),
            GhostColor.MINT:
            Ghost(
                x=GHOST_MINT_INIT_X,
                y=GHOST_MINT_INIT_Y,
                width=self.width,
                height=self.height,
                color=GhostColor.MINT,
            ),
        }
        self.dots = set([(x, y) for x in range(self.width) for y in range(
            self.height) if self.boardarray[x][y] == Tiles.DOT.value])
        self.strawberries = set([(x, y) for x in range(self.width) for y in range(
            self.height) if self.boardarray[x][y] == Tiles.STRAWBERRY.value])
        self.apples = set([(x, y) for x in range(self.width) for y in range(
            self.height) if self.boardarray[x][y] == Tiles.APPLE.value])
        self.walls = set([(x, y) for x in range(self.width) for y in range(
            self.height) if self.boardarray[x][y] == Tiles.WALL.value])
        self.ghost_prev_pos = {
            GhostColor.RED: ((GHOST_RED_INIT_X, GHOST_RED_INIT_Y), Tiles.EMPTY.value),
            GhostColor.PINK: ((GHOST_PINK_INIT_X, GHOST_PINK_INIT_Y), Tiles.EMPTY.value),
            GhostColor.ORANGE: ((GHOST_ORANGE_INIT_X, GHOST_ORANGE_INIT_Y), Tiles.EMPTY.value),
            GhostColor.BLUE: ((GHOST_BLUE_INIT_X, GHOST_BLUE_INIT_Y), Tiles.EMPTY.value),
            GhostColor.MINT: ((GHOST_MINT_INIT_X, GHOST_MINT_INIT_Y), Tiles.EMPTY.value)
        }
        self.pacman_prev_pos = ((PACMAN_INIT_X, PACMAN_INIT_Y), Tiles.EMPTY.value)

    def draw(self):
        """
        Draws each tile of the grid, using the draw method of pacman and ghost
        """

        for y in range(self.boardarray.shape[0]):
            for x in range(self.boardarray.shape[1]):

                id = self.boardarray[x, y]
                coord = (x * GRID_SIZE, y * GRID_SIZE)

                if id == Tiles.WALL.value:
                    pygame.draw.rect(self.screen, WALL_COLOR, (coord, (GRID_SIZE, GRID_SIZE)))

                elif id == Tiles.APPLE.value:
                    self.screen.blit(
                        pygame.image.load(APPLE_DIR), coord)

                elif id == Tiles.STRAWBERRY.value:
                    self.screen.blit(
                        pygame.image.load(STRAWBERRY_DIR), coord)

                elif id == Tiles.DOT.value:
                    self.screen.blit(pygame.image.load(DOT_DIR), coord)

                elif id in [ghost.value for ghost in self.ghosts.keys()]:
                    _, ghost_dir = self.ghosts[GhostColor(id)].draw()
                    self.screen.blit(pygame.image.load(
                        ghost_dir), coord)

                elif id == Tiles.PLAYER.value:
                    _, pacman_dir = self.pacman.draw()
                    self.screen.blit(pygame.image.load(
                        pacman_dir), coord)

    def handle_events(self, events: List[pygame.event.Event]):
        """
        Handles events for the game.

        Params
        ------
        events : List[pygame.event]
            list of events to be handled

        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                    self.pacman.move(event)

            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    def update(self):
        """
        Updates the game state.
        """

        for ghost in self.ghosts.values():
            ghost.move(self.boardarray)

        pacman_pos = self.pacman.get_position()
        ghosts_coords = [ghost.get_position()
                         for ghost in self.ghosts.values()]

        self.boardarray[self.pacman_prev_pos[0][0]][self.pacman_prev_pos[0][1]] = Tiles.EMPTY.value
        self.pacman_prev_pos = (pacman_pos, self.boardarray[pacman_pos[0]][pacman_pos[1]])
        self.boardarray[pacman_pos[0]][pacman_pos[1]] = Tiles.PLAYER.value
        
        for prev_pos, tile_type in self.ghost_prev_pos.values():
            self.boardarray[prev_pos[0]][prev_pos[1]] = Tiles.EMPTY.value if prev_pos not in self.dots else Tiles.DOT.value

        for color, ghost in self.ghosts.items():
            ghost_pos = ghost.get_position()
            self.ghost_prev_pos[color] = (ghost_pos, self.boardarray[ghost_pos[0]][ghost_pos[1]])
            self.boardarray[ghost_pos[0]][ghost_pos[1]] = int(color)


        if pacman_pos in ghosts_coords:
            self.lives -= 1

        if pacman_pos in self.strawberries:
            self.score += STRAWBERRY_POINT
            self.strawberries.remove(pacman_pos)
            self.boardarray[pacman_pos[0]][pacman_pos[1]] = Tiles.EMPTY.value

        if pacman_pos in self.apples:
            self.score += APPLE_POINT
            self.apples.remove(pacman_pos)
            self.boardarray[pacman_pos[0]][pacman_pos[1]] = Tiles.EMPTY.value

        if pacman_pos in self.dots:
            self.score += DOT_POINT
            self.dots.remove(pacman_pos)
            self.boardarray[pacman_pos[0]][pacman_pos[1]] = Tiles.EMPTY.value

        self.game_over = self.lives == 0
        self.game_win = sum([len(self.dots), len(
            self.strawberries), len(self.apples)]) == 0
