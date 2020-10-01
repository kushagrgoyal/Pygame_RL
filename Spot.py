import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:
    def __init__(self, row, col, cell_size, rows):
        self.row = row
        self.col = col
        self.x = row * cell_size
        self.y = col * cell_size
        self.cell_size = cell_size
        self.rows = rows
        self.color = WHITE

    def make_barrier(self):
        self.color = BLACK
    
    def is_barrier(self):
        self.color = BLACK
    
    def make_start(self):
        self.color = TURQUOISE
    
    def is_start(self):
        self.color = TURQUOISE
    
    def make_end(self):
        self.color = ORANGE
    
    def is_end(self):
        self.color = ORANGE
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.cell_size, self.cell_size))

    def make_path(self):
        self.color = GREEN
    
    def reset(self):
        self.color = WHITE