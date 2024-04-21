import sys
import pygame
from clawdius import Clawdius
from logic import Logic

WIN_WIDTH = 800
WIN_HEIGHT = 560

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
    """ Returns the name of which map png to render based on the game state. 

    Args: 
        state: game state array [4]
    
    Returns:
        name of png to render
    """

    # Get int value of game state by treating the values in the
    # list as a binary string
    yates = state[0] * 8
    monroe = state[1] * 4
    isc = state[2] * 2
    lemon = state[3]

    png = yates + monroe + isc + lemon

    match png:
        case 0:     # None
            #return ("map_none.png")        # TODO add png names
            pass
        case 1:     # Lemon 
            pass
        case 2:     # ISC
            pass
        case 3:     # ISC, Lemon
            pass
        case 4:     # Monroe
            pass
        case 5:     # Monroe, Lemon
            pass
        case 6:     # Monroe, ISC
            pass
        case 7:     # Monroe, ISC, Lemon
            pass
        case 8:     # Yates
            pass
        case 9:     # Yates, Lemon
            pass
        case 10:    # Yates, ISC
            pass
        case 11:    # Yates, ISC, Lemon
            pass
        case 12:    # Yates, Monroe
            pass
        case 13:    # Yates, Monroe, Lemon
            pass
        case 14:    # Yates, Monroe, ISC
            pass
        case 15:    # All
            pass
        

def update_view(window, map: str, clawdius: Clawdius):
    #window.blit(map, (0, 0))
    # TODO implement
    clawdius.draw(window)

            

if __name__ == "__main__":
    #won = play_snake()
    #print(won)
    window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
    logic = Logic()
    clawdius = Clawdius(0, 0, 0, 0)
    game_state = [0, 0, 0, 0]   # No buildings constructed yet
    png = "map_none.png"        # TODO REPLACE WITH REAL MAP PNG NAMES

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
                    print(minigame)
                    if game_state[minigame] != 1:
                        print(game_state)
                        print(game_state[minigame])
                        game_state[minigame] = logic.play(minigame)
                        print("after")
                        png = png_to_render(game_state)
        #print("before view")
        update_view(window, png, clawdius)
        #print("after view")

            

