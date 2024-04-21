import sys
import os
import pygame
from clawdius import Clawdius
from minigame import Minigame
from constants import *


def update_view(window, rerender_map, clawdius, game_state):
    if rerender_map:
        pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        window.blit(BASE_IMG, (0, 0))
        window.blit(YATES,YATES_COORD) if game_state[0]== 1 else window.blit(RUBBLE,YATES_COORD)
        window.blit(MONROE,MONROE_COORD) if game_state[1] == 1 else window.blit(RUBBLE,MONROE_COORD)
        window.blit(ISC,ISC_COORD) if game_state[2] == 1 else window.blit(RUBBLE,ISC_COORD)
        window.blit(LEMON,LEMON_COORD) if game_state[3] == 1 else window.blit(RUBBLE,LEMON_COORD)
    clawdius.draw(window)
    pygame.display.update()

            

if __name__ == "__main__":
    # TODO add pygame.init and safety to make sure it runs like get_init
    # https://www.pygame.org/docs/ref/pygame.html#pygame.init 

    window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
    #window.blit(BASE_IMG, (0, 0))
    logic = Minigame()
    clawdius = Clawdius(0, 0, 0, 0)
    game_state = [0, 0, 0, 0]   # No buildings constructed yet
    #png = BASE_IMG       # TODO REPLACE WITH REAL MAP PNG NAMES
    rerender_map = True     # Window may get resized by minigames

    run = True
    while run:
        pygame.time.delay(50)   # wait 50ms between each game loop

        for event in pygame.event.get():

            keys = pygame.key.get_pressed()

            if keys[pygame.K_q] or event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            elif keys[pygame.K_LEFT]:
                # TODO move left
                pass
            elif keys[pygame.K_RIGHT]:
                # TODO move right
                pass
            elif keys[pygame.K_UP]:
                # TODO move up
                pass
            elif keys[pygame.K_DOWN]:
                # TODO move down
                pass
            elif keys[pygame.K_SPACE]:
                # Check if Clawdius is at a construction site
                minigame = clawdius.is_in_building(0, 0)    # TODO change this to clawd's coords
                # Play the minigame if at site and hasn't won that game before 
                if minigame > -1:
                    if game_state[minigame] != 1:
                        game_state[minigame] = logic.play(minigame)
                        #png = png_to_render(game_state)
                        # TODO maybe remove if we make games a popup instead of their own window
                        rerender_map = True
        
        update_view(window, rerender_map, clawdius, game_state)
        rerender_map = False

            

