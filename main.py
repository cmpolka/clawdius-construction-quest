import sys
import os
import pygame
from clawdius import Clawdius
from minigame import *
from constants import *
     

def update_view(window, rerender_map, clawdius, game_state):
    if rerender_map:
        pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
    window.blit(BASE_IMG, (0, 0))
    window.blit(YATES,(100,105)) if game_state[0]== 1 else window.blit(RUBBLE,(100,105))
    window.blit(MONROE,(655,157)) if game_state[1] == 1 else window.blit(RUBBLE,(655,157))
    window.blit(ISC,(345,397)) if game_state[2] == 1 else window.blit(RUBBLE,(345,397))
    window.blit(LEMON,(513,465)) if game_state[3] == 1 else window.blit(RUBBLE,(513,465))
    clawdius.draw(window)
    pygame.display.update()

def main_title_screen():
        screen = pygame.display.init()
        rect = pygame.Rect(150,30,500,500)
        screen = pygame.display.set_mode(size=(800,560))
        pygame.display.update()
            
        background_rect = pygame.Rect(0, 0, 500, 500)
        
        font = pygame.font.init()
        font = pygame.font.SysFont('Helvetica',size = 20)
        
        exit_button_surface = pygame.Surface((150,50))
        exit_text = font.render("Quit",True,(0,0,0))
        exit_text_rect = exit_text.get_rect(center=(exit_button_surface.get_width()/2,exit_button_surface.get_height()/2))
        exit_button_rect = pygame.Rect(325,400,150,50)
        
        start_button_surface = pygame.Surface((150, 50))
        start_text = font.render("Play",True,(0,0,0))
        start_text_rect = start_text.get_rect(center=(start_button_surface.get_width()/2,start_button_surface.get_height()/2))
        
        start_button_rect = pygame.Rect(325,350,150,50)
        
        clock = pygame.time.Clock()
        
        run = True
        while run:
            clock.tick(60)
            screen.fill((255,255,255))
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if start_button_rect.collidepoint(event.pos):
                        run = False
                    if exit_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
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
            
            screen.blit(BACKGROUND, background_rect) 
            screen.blit(start_button_surface,start_button_rect)
            screen.blit(exit_button_surface,exit_button_rect)
            pygame.display.update()
        return


if __name__ == "__main__":
    print(sys.path)
    # TODO add pygame.init and safety to make sure it runs like get_init
    # https://www.pygame.org/docs/ref/pygame.html#pygame.init 

    main_title_screen()

    window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
    minigame_handler = Minigame()
    clawdius = Clawdius(WIN_WIDTH/2 - CLAWD_W/2, WIN_HEIGHT/2 - CLAWD_W/2)
    game_state = [0, 0, 0, 0]   # No buildings constructed yet
    rerender_map = True     # Window may get resized by minigames

    pygame.key.set_repeat(10, 60)   # Allow keys to be repeated for movement
    run = True
    while run:
        #pygame.time.delay(50)   # wait 50ms between each game loop

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if keys[pygame.K_q] or event.type == pygame.QUIT:
                run = False
                break
            elif keys[pygame.K_LEFT]:
                clawdius.move(Direction.LEFT)
            elif keys[pygame.K_RIGHT]:
                clawdius.move(Direction.RIGHT)
            elif keys[pygame.K_UP]:
                clawdius.move(Direction.UP)
            elif keys[pygame.K_DOWN]:
                clawdius.move(Direction.DOWN)
            elif keys[pygame.K_SPACE]:
                # Check if Clawdius is at a construction site
                minigame = clawdius.is_in_building()    # TODO change this to clawd's coords
                # Play the minigame if at site and hasn't won that game before 
                if minigame > -1:
                    if game_state[minigame] != 1:
                        game_state[minigame] = minigame_handler.play(minigame)
                        # TODO maybe remove if we make games a popup instead of their own window
                        rerender_map = True
        
        update_view(window, rerender_map, clawdius, game_state)
        rerender_map = False
    
    pygame.quit()
    sys.exit()

            

