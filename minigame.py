import pygame
import sys
from main import * 
from clawdius import *
sys.path.append("games/flappy_clawd")
import flappy_clawd
from games import snake, simon, connect4
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
                return self.minigame_title_screen(game='Snake Game',func = self.play_snake())
            case Minigames.MONROE.value:
                # Play minigame 2
                return self.minigame_title_screen(game='Connect Four',func = self.play_connect4())
            case Minigames.ISC.value:
                # Play minigame 3
                return self.minigame_title_screen(game='Flappy Clawd',func = self.play_flappy_clawd())
            case Minigames.LEMON.value:
                # Play minigame 4
                return self.play_simon()

        return 0
    


    def minigame_title_screen(self,game:str,func):
        screen = pygame.display.init()
        rect = pygame.Rect(150,30,500,500)
        screen = pygame.display.set_mode(size=(800,560))
        pygame.display.update()
            
            
        menu_text = game
        font = pygame.font.init()
        font = pygame.font.SysFont('Helvetica',size = 20)
        MENU_TEXT = font.render(menu_text, True, (0,0,0))
        MENU_RECT = MENU_TEXT.get_rect(center=(400,100))
        
        screen.blit(MENU_TEXT,MENU_RECT)
        
        exit_button_surface = pygame.Surface((150,50))
        exit_text = font.render("Quit Game",True,(0,0,0))
        exit_text_rect = exit_text.get_rect(center=(exit_button_surface.get_width()/2,exit_button_surface.get_height()/2))
        exit_button_rect = pygame.Rect(325,400,150,50)
        
        start_button_surface = pygame.Surface((150, 50))
        start_text = font.render("Start Game",True,(0,0,0))
        start_text_rect = start_text.get_rect(center=(start_button_surface.get_width()/2,start_button_surface.get_height()/2))
        
        start_button_rect = pygame.Rect(325,350,150,50)
        
        clock = pygame.time.Clock()
        
        won = False
        run = True
        while run:
            clock.tick(60)
            screen.fill((255,255,255))
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    screen.display.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(event.pos):
                        won = func
                        if won:
                            run = False
                            break
                    if exit_button_rect.collidepoint(event.pos):
                        run = False
                        break
            if start_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(start_button_surface, (127, 255, 212), (1, 1, 148, 48))
            else:
                pygame.draw.rect(start_button_surface, (0, 0, 0), (0, 0, 150, 50))
                pygame.draw.rect(start_button_surface, (255, 255, 255), (1, 1, 148, 48))
                pygame.draw.rect(start_button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
                pygame.draw.rect(start_button_surface, (0, 100, 0), (1, 48, 148, 10), 2)
            start_button_surface.blit(start_text,start_text_rect)
            
            if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(exit_button_surface, (127, 255, 212), (1, 1, 148, 48))
            else:
                pygame.draw.rect(exit_button_surface, (0, 0, 0), (0, 0, 150, 50))
                pygame.draw.rect(exit_button_surface, (255, 255, 255), (1, 1, 148, 48))
                pygame.draw.rect(exit_button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
                pygame.draw.rect(exit_button_surface, (0, 100, 0), (1, 48, 148, 10), 2)
            exit_button_surface.blit(exit_text,exit_text_rect)
            
            screen.blit(start_button_surface,start_button_rect)
            screen.blit(exit_button_surface,exit_button_rect)
            screen.blit(MENU_TEXT,MENU_RECT)
            pygame.display.update()
        return won
            
        

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
    

    def play_simon(self):
        won = simon.main()
        return won
    
    
    def play_connect4(self):
        won = connect4.main()
        return won