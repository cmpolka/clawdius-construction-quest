
import pygame 
import os
from enum import Enum

class Minigames(Enum):
    """ Corresponds to game state indeces. """
    YATES = 0
    MONROE = 1
    ISC = 2
    LEMON = 3

class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

WIN_WIDTH = 800
WIN_HEIGHT = 560
NEW_SIZE = (76,68)
CLAWD_W = 60

# Images
BASE_IMG = pygame.image.load(os.path.join("map", "base.png"))
YATES = pygame.transform.scale(pygame.image.load(os.path.join("resources","yates.png")),NEW_SIZE)
MONROE = pygame.transform.scale(pygame.image.load(os.path.join("resources","monroe.png")),NEW_SIZE)
ISC = pygame.transform.scale(pygame.image.load(os.path.join("resources","isc.png")),NEW_SIZE)
LEMON = pygame.transform.scale(pygame.image.load(os.path.join("resources","lemon.png")),NEW_SIZE)
RUBBLE = pygame.transform.scale(pygame.image.load(os.path.join("resources","rubble.png")),NEW_SIZE)
CLAWDIUS = pygame.transform.scale(pygame.image.load(os.path.join("resources", "clawdius_purple.png")), (CLAWD_W, CLAWD_W))
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("resources", "title_background.png")), (WIN_WIDTH, WIN_HEIGHT))

YATES_COORD = (100,105)
MONROE_COORD = (655,157)
ISC_COORD = (345,397)
LEMON_COORD = (513,465)
