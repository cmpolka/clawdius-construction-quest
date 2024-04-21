import sys
import os
import pygame
from clawdius import Clawdius
from minigame import Minigame

WIN_WIDTH = 800
WIN_HEIGHT = 560
NEW_SIZE = (76,68)
CLAWD_WIDTH = 60
CLAWD_HEIGHT = 60

#Loading in png files and resizing building/rubble icons
BASE_IMG = pygame.image.load(os.path.join("map", "base.png"))
YATES = pygame.transform.scale(pygame.image.load(os.path.join("resources","yates.png")),NEW_SIZE)
MONROE = pygame.transform.scale(pygame.image.load(os.path.join("resources","monroe.png")),NEW_SIZE)
ISC = pygame.transform.scale(pygame.image.load(os.path.join("resources","isc.png")),NEW_SIZE)
LEMON = pygame.transform.scale(pygame.image.load(os.path.join("resources","lemon.png")),NEW_SIZE)
RUBBLE = pygame.transform.scale(pygame.image.load(os.path.join("resources","rubble.png")),NEW_SIZE)

CLAWDIUS = pygame.image.load(os.path.join("resources", "clawdius_purple.png"))

IMGS = {
    0:  pygame.image.load("map/base.png"),
    8: pygame.image.load("map/base.png")    # TODO delete
    # 1:  pygame.image.load("resources/map_1.png"),
    # 2:  pygame.image.load("resources/map_2.png"),
    # 3:  pygame.image.load("resources/map_3.png"),
    # 4:  pygame.image.load("resources/map_4.png"),
    # 5:  pygame.image.load("resources/map_5.png"),
    # 6:  pygame.image.load("resources/map_6.png"),
    # 7:  pygame.image.load("resources/map_7.png"),
    # 8:  pygame.image.load("resources/map_8.png"),
    # 9:  pygame.image.load("resources/map_9.png"),
    # 10: pygame.image.load("resources/map_10.png"),
    # 11: pygame.image.load("resources/map_11.png"),
    # 12: pygame.image.load("resources/map_12.png"),
    # 13: pygame.image.load("resources/map_13.png"),
    # 14: pygame.image.load("resources/map_14.png"),
    # 15: pygame.image.load("resources/map_15.png"),
}

def check_building(x: int, y: int):
    """Checks if Clawdius is in any of the construction sites on the map. 
    
    Args: 
        x: Clawdius' x-position on the map (in pixels)
        y: Clawdius' y-position on the map (in pixels)

    Returns:
        The construction spot's index in the game state array
        if in a valid construction site, else returns -1.
    """

    # Check Claw's x and y on the map against each of the
    # construction sites. If overlap, press return that site's
    # index, else -1


def png_to_render(state):
    """ Returns which png to render.

    Calculates the game state value from the game state array 
    and returns the corresponding png from IMGS.

    Args: 
        state: game state array [4]

    Returns:
        png surface to render
    """

    # Get int value of game state by treating the values in the
    # list as a binary string
    yates = state[0] * 8
    monroe = state[1] * 4
    isc = state[2] * 2
    lemon = state[3]

    png = yates + monroe + isc + lemon

    return IMGS.get(png)
        

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
    clawdius = Clawdius(WIN_WIDTH/2 - CLAWD_WIDTH/2, WIN_HEIGHT/2 - CLAWD_HEIGHT/2, CLAWD_WIDTH, CLAWD_HEIGHT)
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
                        # TODO maybe remove if we make games a popup instead of their own window
                        rerender_map = True
        
        update_view(window, rerender_map, clawdius, game_state)
        rerender_map = False

            

