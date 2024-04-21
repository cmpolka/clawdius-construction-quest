
# Constants
import pygame 

WIN_WIDTH = 800
WIN_HEIGHT = 560
NEW_SIZE = (76,68)

# Images
BASE_IMG = pygame.image.load(os.path.join("map", "base.png"))
YATES = pygame.transform.scale(pygame.image.load(os.path.join("resources","yates.png")),NEW_SIZE)
MONROE = pygame.transform.scale(pygame.image.load(os.path.join("resources","monroe.png")),NEW_SIZE)
ISC = pygame.transform.scale(pygame.image.load(os.path.join("resources","isc.png")),NEW_SIZE)
LEMON = pygame.transform.scale(pygame.image.load(os.path.join("resources","lemon.png")),NEW_SIZE)
RUBBLE = pygame.transform.scale(pygame.image.load(os.path.join("resources","rubble.png")),NEW_SIZE)

YATES_COORD = (100,105)
MONROE_COORD = (655,157)
ISC_COORD = (345,397)
LEMON_COORD = (513,465)
