import pygame
from Spot import *
from Gridworld import *
from Qlearning import *
import numpy as np

pygame.init()

win_size = 500
win = pygame.display.set_mode((win_size, win_size))
pygame.display.set_caption('Grid World')

def lookup_table(rows):
    table = np.arange(rows * rows).reshape(rows, -1)
    return table

def make_grid(win_size, rows):
    cell_size = win_size // rows
    grid = []

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, cell_size, rows)
            grid[i].append(spot)
    return grid

def draw_grid(win, rows):
    cell_size = win_size // rows
    for i in range(0, win_size, cell_size):
        pygame.draw.line(win, GREY, (0, i), (win_size, i))
    
    for i in range(0, win_size, cell_size):
        pygame.draw.line(win, GREY, (i, 0), (i, win_size))

def draw(win, rows, grid):
    win.fill(WHITE)
    
    for i in grid:
        for j in i:
            j.draw(win)

    draw_grid(win, rows)
    pygame.display.update()

def get_mouse_pos(pos, win_size, rows):
    cell_size = win_size // rows
    y, x = pos
    row = y // cell_size
    col = x // cell_size
    return row, col


def main(win, rows):
    grid = make_grid(win_size, rows)
    
    lookup = lookup_table(rows)
    q_learning = Qlearning(
        epsilon = 0.7,
        alpha = 0.5,
        gamma = 0.99,
        episodes = 10000,
        rows = rows
    )
    q_table = q_learning.q_table()

    start = None
    end = None
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_pos(pos, win_size, rows)
                spot = grid[row][col]
                
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != start and spot != end:
                    spot.make_barrier()
            
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_pos(pos, win_size, rows)
                spot = grid[row][col]
                spot.reset()

                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gridworld = Gridworld(grid, win_size, rows)
                    s, e, b = gridworld.get_start_end_barrier()
                    
                    print('Training the model')
                    q_table = q_learning.fit(s, e, q_table, gridworld)
                    
                    path = q_learning.return_path(s, e, q_table, gridworld)
                    print(path)

                    for p in path:
                        if p in b:
                            print('Tune the Hyperparameters')

                    for i in path[1 : -1]:
                        spot = grid[i[1]][i[0]]
                        spot.make_path()

            draw(win, rows, grid)


'''
Change the number of rows, higher number of rows would take longer for training as well as some tuning of Hyperparameters might be needed
Hyperparameteres are in the main function under q_learning object
Complex pattern may require more episodes

The first click is Starting point (Turquoise)
The second click is Ending point (Orange)
Further clicks are Barriers (Black)
Any of the Starting, Ending or Barrier locations can be deleted by right-clicks
Space Bar can be used to start training
The final path can be seen in Green
'''
main(win, 20)