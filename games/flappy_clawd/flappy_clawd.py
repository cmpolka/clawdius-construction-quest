import pygame
import time
import os
import sys
import random
from imgs import *


pygame.font.init()
STAT_FONT = pygame.font.SysFont("comicsans", 50)

WIN_WIDTH = 500 # can tweak these later if we notice the screen doesn't fit well
WIN_HEIGHT = 800
FLOOR = 730

CLAWD_IMG = pygame.transform.scale(pygame.image.load(os.path.join("games/flappy_clawd/imgs", "clawdius_yellow.png")), (36, 36))
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("games/flappy_clawd/imgs", "pipe.png")))
FLOOR_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("games/flappy_clawd/imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("games/flappy_clawd/imgs", "bg.png")))

class Bird:
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y): # initialize the bird at starting location (x,y)
        self.x = x              # make x and y position attributes of the class
        self.y = y
        self.tilt = 0           # bird will be looking straight ahead
        self.tick_count = 0     
        self.vel = 0            # velocity = 0, bird starts at rest
        self.height = self.y    
        self.img = CLAWD_IMG

    def jump(self):
        self.vel = -10
        self.tick_count = 0
        self.height = 0

    def move(self):
        self.tick_count += 1
        d = self.vel*self.tick_count + 1.5*self.tick_count**2
        if d >= 16:
            d = 16

        if d < 0:
            d -= 2

        self.y += d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)

        win.blit(rotated_image, new_rect.topleft) 

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(40, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        bird_mask = bird.get_mask()

        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        t_point = bird_mask.overlap(top_mask, top_offset)
        b_point  = bird_mask.overlap(bottom_mask, bottom_offset)
        
        if t_point or b_point:
            return True

        return False

class Base:
    IMG = FLOOR_IMG
    WIDTH = IMG.get_width()
    VEL = 5

    def __init__(self, y):
        self.x1 = 0
        self.x2 = self.WIDTH
        self.y = y

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))
    

def draw_window(win, bird, pipes, base, score, run):
    win.blit(BG_IMG, (0,0))

    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)
    bird.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, (255,255,255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    if not run:
        text = STAT_FONT.render("You Lost!", 1, (255,0,0))
        win.blit(text, (WIN_WIDTH / 2 - text.get_width() / 2, WIN_HEIGHT / 2 - text.get_height() / 2))
    
    pygame.display.update()


def main():
    bird = Bird(230, 350)
    base = Base(FLOOR)
    pipes = [Pipe(600)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    score = 0
    won = False
    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        
        bird.move()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bird.jump()

        add_pipe = False
        rem = []
        for pipe in pipes:
            if pipe.collide(bird):
                run = False
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

            pipe.move()

        if add_pipe:
            score += 1
            pipes.append(Pipe(700))

        for r in rem:
            pipes.remove(r)

        if bird.y + bird.img.get_height() >= FLOOR or bird.y <= 0:
            run = False

        if score == 3:
            won = True
            run = False

        base.move()
        draw_window(win, bird, pipes, base, score, run)

    return won

