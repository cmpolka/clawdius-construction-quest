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
            
        menu_text = 'Snake Game'
        font = pygame.font.init()
        font = pygame.font.SysFont('Helvetica',size = 20)
        MENU_TEXT = font.render(menu_text, True, (0,0,0))
        MENU_RECT = MENU_TEXT.get_rect(center=(400,100))
        
        screen.blit(MENU_TEXT,MENU_RECT)
        
        button_surface = pygame.Surface((150, 50))
        text = font.render("Start Game",True,(0,0,0))
        text_rect = text.get_rect(center=(button_surface.get_width()/2,button_surface.get_height()/2))
        
        button_rect = pygame.Rect(125,125,150,50)
        
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(60)
            screen.fill((155,255,155))
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if button_rect.collidepoint(event.pos):
                        self.play_snake()
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
            else:
                pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
                pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
                pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
                pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)
            button_surface.blit(text,text_rect)
            
            screen.blit(button_surface,(button_rect.x,button_rect.y))
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
