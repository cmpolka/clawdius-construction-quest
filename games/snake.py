import random
import pygame
import sys
import os

WIDTH = 500
ROWS = 20

SURFACE_COL = (0, 0, 0)
GRID_COL = (255, 255, 255)
SNAKE_COL = (255, 0, 255)
SNACK_COL = (0, 255, 0)
SCORE_COL = (255, 0, 0)

CLAWDIUS_SNAKE = pygame.transform.scale(pygame.image.load(os.path.join("resources", "clawdius_pink.png")), (WIDTH//ROWS, WIDTH//ROWS))

pygame.font.init()
STAT_FONT = pygame.font.SysFont("comicsans", 18)

class Cube:
    def __init__(self, start, dirx=1, diry=0, color=SNAKE_COL):
        self.pos = start
        self.dirx = dirx
        self.diry = diry
        self.color = color

    def move(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
        self.pos = (self.pos[0] + self.dirx, self.pos[1] + self.diry)

    def draw(self, surface, head=False):
        dis = WIDTH // ROWS
        i = self.pos[0]
        j = self.pos[1]

        rect = pygame.Rect(i * dis + 1, j * dis + 1, dis - 1, dis - 2)
        if head:
            surface.blit(CLAWDIUS_SNAKE, rect)
        else:
            pygame.draw.rect(surface, self.color, rect)


class Snake:

    def __init__(self, color, pos):
        self.body = []
        self.turns = {}
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()  # see which keys are being pressed

            if keys[pygame.K_LEFT]:
                # mark this space on the board with how the body should turn
                self.turns[self.head.pos] = [-1, 0]
            elif keys[pygame.K_RIGHT]:
                self.turns[self.head.pos] = [1, 0]
            elif keys[pygame.K_UP]:
                self.turns[self.head.pos] = [0, -1]
            elif keys[pygame.K_DOWN]:
                self.turns[self.head.pos] = [0, 1]

    def move(self):
        #self.get_input()

        for i, cube, in enumerate(self.body):
            p = cube.pos
            if p in self.turns:
                turn = self.turns[p]
                cube.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if cube.dirx == -1 and cube.pos[0] <= 0:
                    cube.pos = (ROWS, cube.pos[1])
                elif cube.dirx == 1 and cube.pos[0] >= ROWS - 1:
                    cube.pos = (-1, cube.pos[1])
                elif cube.diry == 1 and cube.pos[1] >= ROWS - 1:
                    cube.pos = (cube.pos[0], -1)
                elif cube.diry == -1 and cube.pos[1] <= 0:
                    cube.pos = (cube.pos[0], ROWS)

                cube.move(cube.dirx, cube.diry)

    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dirx, tail.diry

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirx = dx
        self.body[-1].diry = dy

    def draw(self, surface):
        for i, cube in enumerate(self.body):
            if i == 0:
                cube.draw(surface, True)
            else:
                cube.draw(surface)


def random_snack(snake):
    positions = snake.body

    while True:
        x = random.randrange(0, ROWS - 1)
        y = random.randrange(0, ROWS - 1)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return x, y


def redraw_surface(surface, snake, snack):
    surface.fill(SURFACE_COL)
    draw_grid(surface)
    draw_score(surface, len(snake.body))
    snake.draw(surface)
    snack.draw(surface)
    pygame.display.update()

def draw_score(surface, score):
    text = STAT_FONT.render("Score: " + str(score), 0, SCORE_COL)
    surface.blit(text, (WIDTH - 5 - text.get_width(), 0))

def draw_grid(surface):
    square_size = WIDTH // ROWS

    x = 0
    y = 0
    for _ in range(ROWS):
        x = x + square_size
        y = y + square_size

        pygame.draw.line(surface, GRID_COL, (x, 0), (x, WIDTH))  # vertical lines
        pygame.draw.line(surface, GRID_COL, (0, y), (WIDTH, y))  # horizontal lines


def main():
    surface = pygame.display.set_mode(size=(WIDTH, WIDTH))
    snake = Snake(SNAKE_COL, (10, 10))
    snack = Cube(random_snack(snake), color=SNACK_COL)

    won = False
    run = True
    while run:
        pygame.time.delay(80)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                won = False
                run = False
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()  # see which keys are being pressed

            if keys[pygame.K_ESCAPE]:
                won = False
                run = False
            elif keys[pygame.K_LEFT]:
                # mark this space on the board with how the body should turn
                snake.turns[snake.head.pos] = [-1, 0]
            elif keys[pygame.K_RIGHT]:
                snake.turns[snake.head.pos] = [1, 0]
            elif keys[pygame.K_UP]:
                snake.turns[snake.head.pos] = [0, -1]
            elif keys[pygame.K_DOWN]:
                snake.turns[snake.head.pos] = [0, 1]

        snake.move()

        head_pos = snake.head.pos
        if head_pos[0] >= 20 or head_pos[0] < 0 or head_pos[1] >= 20 or head_pos[1] < 0:
            print("Score:", len(snake.body))
            snake.reset((10, 10))

        for x in range(len(snake.body)):
            if snake.body[x].pos in list(map(lambda z: z.pos, snake.body[x + 1:])):
                print("Score:", len(snake.body))
                snake.reset((10, 10))
                break

        if snake.body[0].pos == snack.pos:
            snake.add_cube()
            snack = Cube(random_snack(snake), color=SNACK_COL)

        if len(snake.body) == 5:
            won = True
            run = False

        redraw_surface(surface, snake, snack)

    return won