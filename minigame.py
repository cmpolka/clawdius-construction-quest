import pygame
import sys
sys.path.append("games/flappy_clawd")
import flappy_clawd
from games import snake
from games import connect4
from enum import Enum
from constants import *

class Minigame:

    def __init__(self):
        pass

    def play(self, minigame: int):
        """Begins the minigame for the building Clawdius is on.

        Args: 
            minigame: index in the game state array for that minigame

        Returns:
            1 if game was won,
            0 if game was quit  
        """

        match minigame:
            case Minigames.YATES.value:
                # Play minigame 1
                return self.play_snake()
            case Minigames.MONROE.value:
                # Play minigame 2
                return self.play_connect4()
            case Minigames.ISC.value:
                # Play minigame 3
                return self.play_flappy_clawd()
            case Minigames.LEMON.value:
                # Play minigame 4
                pass

        return 0
    

    # def minigame_title_screen(self, minigame):
    #     #minigame = pygame.display.init()
    #     rect = pygame.Rect(150, 30, 500, 500)
    #     minigame = pygame.display.set_mode(size=(800, 560))
    #     print(minigame)
    #     minigame.fill((255, 255, 255), rect)
    #     pygame.display.update()
    #     pygame.time.delay(3000)
    #     return self.play_snake(minigame, rect)


    # def create_minigame_surface(self, w, h):
    #     minigame_surface = pygame.Surface((w, h))
    #     minigame_surface.fill((0, 0, 0))
    #     return minigame_surface

    def play_connect4(self):
        """Plays the snake minigame. 
        
        Returns: 
            True if the user reaches a score of 10, 
            false if the player quits the game.
        """
        # snake_surface = self.create_minigame_surface(500, 500)
        # rect = pygame.Rect((800 - 500)/2, (560 - 500)/2, 500, 500)

        # TODO add loading screen
        return connect4()

    def play_snake(self):
        """Plays the snake minigame. 
        
        Returns: 
            True if the user reaches a score of 10, 
            false if the player quits the game.
        """
        # snake_surface = self.create_minigame_surface(500, 500)
        # rect = pygame.Rect((800 - 500)/2, (560 - 500)/2, 500, 500)

        # TODO add loading screen

        won = snake.main()
        return won


    def play_flappy_clawd(self):
        """Plays flappy bird (clawd) minigame.
        
        Returns:
            True if the user reaches a score of 10,
            false if the player quits the game.
        """
        won = flappy_clawd.main()
        return won