import pygame
import random
import time
import threading
from itertools import product

BLACK,WHITE,GREEN,GRAY = (0,0,0),(255,255,255),(0,255,0),(128, 128, 128)
cell_size,grid_size,space = 20,20,25
size, cell2, x, y = cell_size * grid_size, cell_size*2, 25, 25
min_loc, max_loc = size, size+space
stack,visited,vec,solved = [], [], [], []

pygame.init()
pygame.display.set_caption("Maze Visualizer")

win = pygame.display.set_mode((size+(space*2),size+(space*2)))
win.fill(WHITE)
pygame.draw.rect(win, BLACK, [space,space,(size + 2),(size + 2)],3)


def build_grid():
    for i in range(1, grid_size):
        pygame.draw.line(win, BLACK, ((i * cell_size) + space, space), ((i * cell_size) + space, space + size), 2)
        pygame.draw.line(win, BLACK, (space, (i * cell_size) + space), (space + size, (i * cell_size) + space), 2)
        pygame.display.update()

def colourCell(x,y):
    pygame.draw.rect(win, GRAY, (x + 1,y + 1,cell_size - 1,cell_size - 1))
    pygame.display.update()

def cell_highlight(x,y):
    pygame.draw.rect(win, GREEN, (x + 1, y + 1, cell_size - 1, cell_size - 1))
    pygame.display.update()

def move(moves,x,y):
    if(moves == 'u'):
        pygame.draw.rect(win, GRAY, (x + 1, y + 1 - cell_size, cell_size - 1, (cell_size * 2) - 3))
    elif(moves == 'd'):
        pygame.draw.rect(win, GRAY, (x + 1, y + 1, cell_size - 1, (cell_size * 2) - 3))
    elif (moves == 'l'):
        pygame.draw.rect(win, GRAY, (x + 1, y + 1, (cell_size * 2) - 3, cell_size - 1))
    elif (moves == 'r'):
        pygame.draw.rect(win, GRAY, (x + 1-cell_size, y + 1, (cell_size*2) - 3, cell_size - 1))
    pygame.display.update()

for i in range(grid_size):
    vec.append(i*cell_size+25)
grid = list(product(vec,vec))

def create_maze(x,y):
    stack.append((x,y))
    visited.append((x,y))
    while len(stack) > 0:
        pygame.time.wait(25)
        direction = []
        if (x,y-cell_size) not in visited and (x,y-cell_size) in grid:
            direction.append("u")
        if (x,y+cell_size) not in visited and (x,y+cell_size) in grid:
            direction.append("d")
        if (x-cell_size,y) not in visited and (x-cell_size,y) in grid:
            direction.append("l")
        if (x+cell_size,y) not in visited and (x+cell_size,y) in grid:
            direction.append("r")

        if len(direction) > 0:
            random_direction = (random.choice(direction))

            if random_direction == "u":
                move('u',x, y)
                y = y - cell_size
                visited.append((x, y))
                stack.append((x, y))
            elif random_direction == "d":
                move('d',x, y)
                y = y + cell_size
                visited.append((x, y))
                stack.append((x, y))
            elif random_direction == "r":
                move('l',x, y)
                x = x + cell_size
                visited.append((x, y))
                stack.append((x, y))
            elif random_direction == "l":
                move('r',x, y)
                x = x - cell_size
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()
            cell_highlight(x,y)
            pygame.time.wait(25)
            colourCell(x,y)

build_grid()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    create_maze(x,y)
    pygame.display.update()