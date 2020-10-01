import numpy as np

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

class Gridworld:
    def __init__(self, grid, win_size, rows):
        self.grid = grid
        self.win_size = win_size
        self.rows = rows
        self.cell_size = win_size // rows
    
    def get_start_end_barrier(self):
        self.start = None
        self.end = None
        self.barrier = []

        for i, row in enumerate(self.grid):
            for j, spot in enumerate(row):
                if spot.color == TURQUOISE:
                    self.start = (j, i)
                elif spot.color == ORANGE:
                    self.end = (j, i)
                elif spot.color == BLACK:
                    self.barrier.append((j, i))
        return self.start, self.end, self.barrier
    
    def is_edge(self, state):
        # return bool of array[top_edge > 0, right_edge > 1, bottom_edge > 2, left_edge > 3]
        table = np.arange(self.rows * self.rows).reshape(self.rows, -1)
        # if state[0] == 0:
        if state in table[0]:
            return 0
        # elif state[0] == self.rows - 1:
        elif state in table[-1]:
            return 2
        # elif state[1] == 0:
        elif state in table[:, 0]:
            return 3
        # elif state[1] == self.rows - 1:
        elif state in table[:, -1]:
            return 1
        else:
            # If the state is not an edge state
            return 4
    
    def is_corner(self, state):
        # return bool of array[top_left > 0, top_right > 1, bottom_right > 2, bottom_left > 3]
        table = np.arange(self.rows * self.rows).reshape(self.rows, -1)
        # if state == (0, 0):
        if state == table[0, 0]:
            return 0
        # elif state == (self.rows - 1, 0):
        elif state == table[0, -1]:
            return 1
        # elif state == (self.rows - 1, self.rows - 1):
        elif state == table[-1, -1]:
            return 2
        # elif state == (0, self.rows - 1):
        elif state == table[-1, 0]:
            return 3
        else:
            # If the state is not a corner state
            return 4

    def convert_state(self, state):
        table = np.arange(self.rows * self.rows).reshape(self.rows, -1)
        if type(state) == list:
            state = [table[i] for i in state]
            return state
        else:
            return table[state]

    def reward_func(self, new_state):
        end = self.convert_state(self.end)
        barrier = self.convert_state(self.barrier)

        if new_state == end:
            reward = 20
            done = True
            return reward, done
        elif new_state in barrier:
            reward = -10
            done = False
            return reward, done
        else:
            reward = -1
            done = False
            return reward, done

    def step(self, state, action):
        '''
        Actions:
        0 > Top / Up
        1 > Right
        2 > Bottom / Down
        3 > Left
        '''
        if state == self.convert_state(self.end):
            print('Target Reached')
            done = True
            return done

        if self.is_edge(state) == 4:
            # state = convert_state(state)
            if action == 0:
                new_state = state - self.rows
                reward, done = self.reward_func(new_state)
            elif action == 1:
                new_state = state + 1
                reward, done = self.reward_func(new_state)
            elif action == 2:
                new_state = state + self.rows
                reward, done = self.reward_func(new_state)
            elif action == 3:
                new_state = state - 1
                reward, done = self.reward_func(new_state)
        
        elif self.is_edge(state) == 0 and self.is_corner(state) == 4:# Top edge and No corner
            # state = convert_state(state)
            if action == 0: # Going up
                new_state = state
                reward = -10
                done = False
            elif action == 1: # Going right
                new_state = state + 1
                reward, done = self.reward_func(new_state)
            elif action == 2: # Going down
                new_state = state + self.rows
                reward, done = self.reward_func(new_state)
            elif action == 3: # Going left
                new_state = state - 1
                reward, done = self.reward_func(new_state)
        
        elif self.is_edge(state) == 1 and self.is_corner(state) == 4:# Right edge and No corner
            # state = convert_state(state)
            if action == 0: # Going up
                new_state = state - self.rows
                reward, done = self.reward_func(new_state)
            elif action == 1: # Going right
                new_state = state
                reward = -10
                done = False
            elif action == 2: # Going down
                new_state = state + self.rows
                reward, done = self.reward_func(new_state)
            elif action == 3: # Going left
                new_state = state - 1
                reward, done = self.reward_func(new_state)
        
        elif self.is_edge(state) == 2 and self.is_corner(state) == 4:# Bottom edge and No corner
            # state = convert_state(state)
            if action == 0: # Going up
                new_state = state - self.rows
                reward, done = self.reward_func(new_state)
            elif action == 1: # Going right
                new_state = state + 1
                reward, done = self.reward_func(new_state)
            elif action == 2: # Going down
                new_state = state
                reward = -10
                done = False
            elif action == 3: # Going left
                new_state = state - 1
                reward, done = self.reward_func(new_state)
        
        elif self.is_edge(state) == 3 and self.is_corner(state) == 4:# Left edge and No corner
            # state = convert_state(state)
            if action == 0: # Going up
                new_state = state - self.rows
                reward, done = self.reward_func(new_state)
            elif action == 1: # Going right
                new_state = state + 1
                reward, done = self.reward_func(new_state)
            elif action == 2: # Going down
                new_state = state + self.rows
                reward, done = self.reward_func(new_state)
            elif action == 3: # Going left
                new_state = state
                reward = -10
                done = False
        
        elif self.is_corner(state) == 0:
            # state = convert_state(state)
            if action == 0: # Going up
                new_state = state
                reward = -10
                done = False
            elif action == 1: # Going right
                new_state = state + 1
                reward, done = self.reward_func(new_state)
            elif action == 2: # Going down
                new_state = state + self.rows
                reward, done = self.reward_func(new_state)
            elif action == 3: # Going left
                new_state = state
                reward = -10
                done = False
        
        elif self.is_corner(state) == 1:
            # state = convert_state(state)
            if action == 0: # Going up
                new_state = state
                reward = -10
                done = False
            elif action == 1: # Going right
                new_state = state
                reward = -10
                done = False
            elif action == 2: # Going down
                new_state = state + self.rows
                reward, done = self.reward_func(new_state)
            elif action == 3: # Going left
                new_state = state - 1
                reward, done = self.reward_func(new_state)
        
        elif self.is_corner(state) == 2:
            # state = convert_state(state)
            if action == 0: # Going up
                new_state = state - self.rows
                reward, done = self.reward_func(new_state)
            elif action == 1: # Going right
                new_state = state
                reward = -10
                done = False
            elif action == 2: # Going down
                new_state = state
                reward = -10
                done = False
            elif action == 3: # Going left
                new_state = state - 1
                reward, done = self.reward_func(new_state)
        
        elif self.is_corner(state) == 3:
            # state = convert_state(state)
            if action == 0: # Going up
                new_state = state - self.rows
                reward, done = self.reward_func(new_state)
            elif action == 1: # Going right
                new_state = state + 1
                reward, done = self.reward_func(new_state)
            elif action == 2: # Going down
                new_state = state
                reward = -10
                done = False
            elif action == 3: # Going left
                new_state = state
                reward = -10
                done = False
        
        return new_state, reward, done