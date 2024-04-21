from constants import *
import pygame

class Clawdius:
    def __init__(self, x: int, y: int):
        # TODO figure out params to take (x, y, anything else?) and init
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, CLAWD_W, CLAWD_W)

    def is_in_building(self):
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
        
        return -1

    def move(self, dir: Direction):
        match dir:
            case Direction.LEFT:
                self.x -= 10
                self.rect.x = self.x
            case Direction.RIGHT:
                self.x += 10
                self.rect.x = self.x
            case Direction.UP:
                self.y -= 10
                self.rect.y = self.y
            case Direction.DOWN:
                self.y += 10
                self.rect.y = self.y

    def draw(self, window):
        window.blit(CLAWDIUS, self.rect)