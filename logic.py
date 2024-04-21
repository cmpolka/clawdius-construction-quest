import pygame
from games import snake
from enum import Enum
import os.path,subprocess
from subprocess import STDOUT,PIPE




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
    # edu.wm.cs.cs301.wordle.Wordle
    def play_wordle(self):
        print("playing Clawdius' Words")
        game = compile_java("games/clawdiuswords/src/edu/wm/cs/cs301/wordle/Wordle.java")
        won = execute_java(game)  # Pass the class name without extension
        return won

    def play_snake(self):
        """Plays the snake minigame. 
        
        Returns: 
            True if the user reaches a score of 10, 
            false if the player quits the game.
        """
        print("playing snake")
        won = snake.main()
        return won
    
def compile_java (java_file):
    subprocess.run(['javac', java_file])

def execute_java (java_file):
    cmd=['java', java_file]
    proc=subprocess.Popen(cmd, stdout = PIPE, stderr = STDOUT)
    input = subprocess.Popen(cmd, stdin = PIPE)
    print(proc.stdout.read())


# def play_wordle():
#     print("playing Clawdius' Words")
#     game = compile_java("C:\\games\clawdiuswords.java")
#     won = execute_java(game)  # Pass the class name without extension
#     return won

        # Call the play_wordle function
        # result = play_wordle()
        # print('Result:', result)
    # def compile_java(java_file):
    #     subprocess.check_call(['javac', java_file])

    # def execute_java(java_file, stdin):
    #     java_class,ext = os.path.splitext(java_file)
    #     cmd = ['java', java_class]
    #     proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    #     stdout,stderr = proc.communicate(stdin)
    #     print ('This was "' + stdout + '"')

    # def play_wordle(self):
    #     print("playing Clawdius' Words")
    #     compile_java('Hi.java')
    #     execute_java('Hi.java', 'Jon')
    #     return won
    
