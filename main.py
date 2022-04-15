import pygame
from constants import BACKGROUND_COLOR, GRID_SIZE, WINDOW_SIZE, WINDOW_TITLE
from components.game import Game

# Main loop to run the pacman game

def main():
    # Initialize pygame
    pygame.init()

    # Set the window size
    window_size = WINDOW_SIZE
    screen = pygame.display.set_mode(window_size)

    # Set the window title
    pygame.display.set_caption(WINDOW_TITLE)

    # Set the clock
    clock = pygame.time.Clock()

    # Set the FPS
    fps = 60

    # Create the game object
    game = Game(width=window_size[0] // GRID_SIZE,
                height=window_size[1] // GRID_SIZE)

    # Set the game loop to run
    running = game.is_running()

    # Main game loop
    while running:
        # Set the FPS
        clock.tick(fps)

        # Check for events
        game.handle_events(pygame.event.get())

        # Update the screen
        screen.fill(BACKGROUND_COLOR)

        # Draw the game
        game.draw()

        # Update the screen
        pygame.display.flip()

        # Update the game
        game.update()

        # Check if the game is over
        running = game.is_running()

    # Quit pygame
    pygame.quit()


if __name__ == '__main__':
    main()
