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
    window.blit(YATES,(100,105)) if game_state[0]== 1 else window.blit(RUBBLE,(100,105))
    window.blit(MONROE,(655,157)) if game_state[1] == 1 else window.blit(RUBBLE,(655,157))
    window.blit(ISC,(345,397)) if game_state[2] == 1 else window.blit(RUBBLE,(345,397))
    window.blit(LEMON,(513,465)) if game_state[3] == 1 else window.blit(RUBBLE,(513,465))
    clawdius.draw(window)
    pygame.display.update()


if __name__ == "__main__":
    # TODO add pygame.init and safety to make sure it runs like get_init
    # https://www.pygame.org/docs/ref/pygame.html#pygame.init 

    window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
    #window.blit(BASE_IMG, (0, 0))
    logic = Minigame()
    clawdius = Clawdius(WIN_WIDTH/2 - CLAWD_W/2, WIN_HEIGHT/2 - CLAWD_W/2)
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
                clawdius.move(Direction.LEFT)
            elif keys[pygame.K_RIGHT]:
                clawdius.move(Direction.RIGHT)
            elif keys[pygame.K_UP]:
                clawdius.move(Direction.UP)
            elif keys[pygame.K_DOWN]:
                clawdius.move(Direction.DOWN)
            elif keys[pygame.K_SPACE]:
                # Check if Clawdius is at a construction site
                minigame = clawdius.is_in_building(0, 0)    # TODO change this to clawd's coords
                # Play the minigame if at site and hasn't won that game before 
                if minigame > -1:
                    if game_state[minigame] != 1:
                        game_state[minigame] = logic.play(minigame)
                        # TODO maybe remove if we make games a popup instead of their own window
                        rerender_map = True
        
        update_view(window, rerender_map, clawdius, game_state)
        rerender_map = False

            

