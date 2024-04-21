import pygame
from random import choice
from time import sleep


SCREEN_W = 500
TILE_W = 250

DARK_RED = (255, 0, 0)
RED = (255, 100, 100)
DARK_GREEN = (0, 255, 0)
GREEN = (150, 255, 150)
DARK_BLUE = (0, 0, 255)
BLUE = (80, 80, 255)
DARK_PURPLE = (155, 0, 200)
PURPLE = (200, 50, 250)
WHITE = (255, 255, 255)

TOP_LEFT = pygame.Rect(0, 0, TILE_W, TILE_W)
BOTTOM_LEFT = pygame.Rect(0, TILE_W, TILE_W, TILE_W)
BOTTOM_RIGHT = pygame.Rect(TILE_W, TILE_W, TILE_W, TILE_W),
TOP_RIGHT = pygame.Rect(TILE_W, 0, TILE_W, TILE_W),

pygame.font.init()
STAT_FONT = pygame.font.SysFont("comicsans", 18)

pattern = []
guesses = []
tiles = {
    "tl": (RED, DARK_RED),
    "bl": (GREEN, DARK_GREEN),
    "br": (BLUE, DARK_BLUE),
    "tr": (PURPLE, DARK_PURPLE),
}

def get_tile_rect(tile):
    match tile:
        case "tl":
            return TOP_LEFT
        case "bl":
            return BOTTOM_LEFT
        case "br":
            return BOTTOM_RIGHT
        case "tr":
            return TOP_RIGHT


def draw_grid(surface):
    """Draw grid of tiles."""
    pygame.draw.rect(surface, DARK_RED, get_tile_rect("tl"))
    pygame.draw.rect(surface, DARK_GREEN, get_tile_rect("bl"))
    pygame.draw.rect(surface, DARK_BLUE, get_tile_rect("br"))
    pygame.draw.rect(surface, DARK_PURPLE, get_tile_rect("tr"))


def flash(surface, tile, score):
    """Flash tile in grid."""
    tile_rect = get_tile_rect(tile)
    glow, dark = tiles[tile]
    surface.fill(glow, tile_rect)
    draw_text(surface, score)
    pygame.display.update(tile_rect)
    sleep(0.5)
    surface.fill(dark, tile_rect)
    draw_text(surface, score)
    pygame.display.update(tile_rect)
    sleep(0.5)


def grow(surface, score):
    """Grow pattern and flash tiles."""
    print(list(tiles))
    tile = choice(list(tiles))
    print(tile)
    pattern.append(tile)

    for tile in pattern:
        flash(surface, tile, score)

    print('Pattern length:', len(pattern))
    guesses.clear()


def tap(surface, tile, score):
    """Respond to screen tap."""
    index = len(guesses)

    if tile != pattern[index]:
        return False

    guesses.append(tile)
    flash(surface, tile, score)

    return True

def draw_text(surface, score):
    text = STAT_FONT.render(f"Score: {score}", 1, WHITE)
    surface.blit(text, (SCREEN_W - 5 - text.get_width(), 5))

def update_view(surface, score):
    """Draw objects on screen."""
    surface.fill(WHITE)
    draw_grid(surface)
    text = STAT_FONT.render(f"Score: {score}", 1, WHITE)
    surface.blit(text, (SCREEN_W - 5 - text.get_width(), 5))
    pygame.display.update()


def main():
    score = 0
    surface = pygame.display.set_mode(size=(SCREEN_W, SCREEN_W))
    draw_grid(surface)
    draw_text(surface, score)
    pygame.display.update()
    grow(surface, score)
    
    won = False
    run = True
    while run:
        event = pygame.event.wait() # Wait for user input

        if event.type == pygame.QUIT:
            run = False
            pattern.clear()
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if x < TILE_W and y < TILE_W:
                run = tap(surface, "tl", score)
            elif x < TILE_W and y > TILE_W:
                run = tap(surface, "bl", score)
            elif x > TILE_W and y > TILE_W:
                run = tap(surface, "br", score)
            elif x > TILE_W and y < TILE_W:
                run = tap(surface, "tr", score)

        if run == False:
            pattern.clear()
            break
        elif len(guesses) == 10:
            won = True
            run = False
            pattern.clear()
            break
        elif len(guesses) == len(pattern):
            score += 1
            grow(surface, score)

        update_view(surface, score)
        
    return won
        
    