import pygame
from games import snake
from enum import Enum



class Minigames(Enum):
    """ Corresponds to game state indeces. """
    YATES = 0
    MONROE = 1
    ISC = 2
    LEMON = 3

class Logic:

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
                return self.play_wordle()
            case Minigames.ISC.value:
                # Play minigame 3
                pass
            case Minigames.LEMON.value:
                # Play minigame 4
                pass

        return 0


    def play_snake(self):
        """Plays the snake minigame. 
        
        Returns: 
            True if the user reaches a score of 10, 
            false if the player quits the game.
        """
        print("playing snake")
        won = snake.main()
        return won
    
    def play_wordle(self):
        print("playing Clawd's ")
        pass
