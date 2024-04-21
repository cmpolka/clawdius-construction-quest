from minigame import Minigames
import pygame

class Clawdius:
    def __init__(self, x: int, y: int, width: int, height: int):
        # TODO figure out params to take (x, y, anything else?) and init
        self.x = x
        self.y = y
        self.WIN_WIDTH = width
        self.WIN_HEIGHT = height
        self.rect = pygame.Rect(x, y, width, height)
        self.clawd_surface = pygame.display.

    def is_in_building(self, x: int, y: int):
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
        return 0

    def move(self):
        pass

    def draw(self, window):
        window.blit(self)