import sys
import os
import pygame
from clawdius import Clawdius
from logic import Logic

WIN_WIDTH = 800
WIN_HEIGHT = 560

#BASE_IMG = pygame.image.load(os.path.join("map", "base.png"))
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
        

def update_view(window, resized, map, clawdius):
    if resized:
        pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
    window.blit(map, (0, 0))
    # TODO implement
    clawdius.draw(window)
    pygame.display.update()

            

if __name__ == "__main__":
    window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
    logic = Logic()
    clawdius = Clawdius(0, 0, 0, 0)
    game_state = [0, 0, 0, 0]   # No buildings constructed yet
    png = IMGS[0]        # TODO REPLACE WITH REAL MAP PNG NAMES
    resized = False     # Window may get resized by minigames

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
                        png = png_to_render(game_state)
                        # TODO maybe remove if we make games a popup instead of their own window
                        resized = True
        
        update_view(window, resized, png, clawdius)
        resized = False

            

