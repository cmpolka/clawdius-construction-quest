from minigame import Minigames
import pygame
from constants import * 

class Clawdius:
    def __init__(self, x: int, y: int, width: int, height: int):
        # TODO figure out params to take (x, y, anything else?) and init
        self.x = x
        self.y = y
        self.WIN_WIDTH = width
        self.WIN_HEIGHT = height
        self.rect = pygame.Rect(x,y,width,height)

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
        yates = pygame.Rect(YATES_COORD,NEW_SIZE)
        if self.rect.colliderect(yates):
            return Minigames.YATES.value
        
        monroe = pygame.Rect(MONROE_COORD,NEW_SIZE)
        if self.rect.colliderect(monroe):
            return Minigames.MONROE.value
        
        isc = pygame.Rect(ISC_COORD,NEW_SIZE)
        if self.rect.colliderect(isc):
            return Minigames.ISC.value
        
        lemon = pygame.Rect(LEMON_COORD,NEW_SIZE)
        if self.rect.colliderect(lemon):
            return Minigames.LEMON.value
        return 0

    def move(self):
        pass

    def draw(self, window):
        pass