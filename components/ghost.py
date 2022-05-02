from enums.ghost_color import GhostColor
from typing import Tuple
from constants import (
   GHOST_BLUE_DIR,
   GHOST_ORANGE_DIR,
   GHOST_PINK_DIR,
   GHOST_MINT_DIR,
   GHOST_RED_DIR
)
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
       position_tuple = (self.x, self.y)
       return (position_tuple, self.image_dir)
       #raise NotImplementedError("Ghost.draw() is not implemented.")
 
   def move(self, game_map):
       """
       Move the ghost based on the pacman position.
 
       Params
       ------
       pacman_position : Tuple[int, int]
           x, y coordinates of the pacman
 
       """
       int direction = random.randInt(0, 3)
       bool isWall = False
       if(direction == UP):
           if(isNotUpWall(self)):
               self.y += 1
           else:
               isWall = True
       else if(direction == DOWN):
           if(isNotDownWall(self)):
               self.y -= 1
           else:
               isWall = True
       else if(direction == LEFT):
           if(isNotLeftWall(self)):
               self.x -= 1
           else:
               isWall = True
       else if(direction == RIGHT):
           if(isNotRightWall(self)):
               self.x += 1
           else:
               isWall = True
      
       if(isWall):
           move(self, game_map)
 
       #raise NotImplementedError("Ghost.move() is not implemented.")
 
   def isNotUpWall(self):
       return (game_map[self.x][self.y+1]!=WALL and self.x!=0)
  
   def isNotDownWall(self):
       return (game_map[self.x][self.y-1]!=WALL and self.x!=len(game_map)-1)
 
   def isNotLeftWall(self):
       return (game_map[self.x-1][self.y]!=WALL and self.y!=0)
 
   def isNotRightWall(self):
       return (game_map[self.x+1][self.y]!=WALL and self.y!=len(game_map[0])-1)
      
 
   def get_position(self):
       return (self.x, self.y)
 
   # Add more functions if needed
 
