from constants import *
import pygame

class Clawdius:
    def __init__(self, x: int, y: int):
        # TODO figure out params to take (x, y, anything else?) and init
        self.x = x
        self.y = y

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

    def move(self, dir: Direction):
        match dir:
            case Direction.LEFT:
                self.x -= 10
            case Direction.RIGHT:
                self.x += 10
            case Direction.UP:
                self.y -= 10
            case Direction.DOWN:
                self.y += 10

    def draw(self, window):
        window.blit(CLAWDIUS, (self.x, self.y))