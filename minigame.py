import pygame
import sys
from button import Button
from games import snake
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
                return self.minigame_title_screen()
            case Minigames.MONROE.value:
                # Play minigame 2
                pass
            case Minigames.ISC.value:
                # Play minigame 3
                pass
            case Minigames.LEMON.value:
                # Play minigame 4
                pass
    

    # def minigame_title_screen(self, minigame):
    #     #screen = pygame.display.init()
    #     rect = pygame.Rect(150, 30, 500, 500)
    #     screen = pygame.display.set_mode(size=(800, 560))
    #     print(minigame)
    #     minigame.fill((255, 255, 255), rect)
    #     pygame.display.update()
    #     pygame.time.delay(3000)
    #     return self.play_snake(minigame, rect)

    def minigame_title_screen(self):
        screen = pygame.display.init()
        rect = pygame.Rect(150,30,500,500)
        screen = pygame.display.set_mode(size=(800,560))
        pygame.display.update()
        screen.fill((255,255,255),rect)
        pygame.display.update()
            
        MENU_MOUSE_POS = pygame.mouse.get_pos()
            
        text = 'Snake Game'
        button_text = 'Start Game'
        font = pygame.font.init()
        font = pygame.font.SysFont('Helvetica',size = 20)
        MENU_TEXT = font.render(text, True, (0,0,0))
        MENU_RECT = MENU_TEXT.get_rect(center=(400,100))
        
        button = font.render(button_text,True,(0,0,0))
        button_rect = button.get_rect(center = (400,400))
            
        screen.blit(MENU_TEXT,MENU_RECT)
            
        screen.blit(button,button_rect)
            
        pygame.display.update()  
        pygame.time.delay(3000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                self.play_snake()
        pygame.display.update()
            
            

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
