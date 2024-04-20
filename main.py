import pygame
from games import snake

def play_snake():
    """Plays the snake minigame. Returns true if the user reaches
     a score of 10, false if the player quits the game."""
    won = snake.main()
    return won


if __name__ == "__main__":
    won = play_snake()
    print(won)