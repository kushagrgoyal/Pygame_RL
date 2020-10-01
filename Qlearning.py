import numpy as np
from tqdm import tqdm

class Qlearning:
    def __init__(self, epsilon, alpha, gamma, episodes, rows):
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.episodes = episodes
        self.rows = rows
    
    def q_table(self):
        q = np.zeros((self.rows * self.rows, 4))
        return q
    
    def fit(self, start, end, q_table, gridworld):
        for episode in tqdm(range(self.episodes)):
            state = gridworld.convert_state(start)
            if episode > 0.5 * self.episodes:
                self.epsilon *= 0.99
            
            done = False
            
            while not done:
                if np.random.uniform(0, 1) <= self.epsilon:
                    action = np.random.randint(0, 4)
                else:
                    action = np.argmax(q_table[state])
                
                new_state, reward, done = gridworld.step(state, action)

                if not done:
                    current_q = q_table[state, action]
                    max_future_q = np.max(q_table[new_state])

                    new_q = (1 - self.alpha) * current_q + self.alpha * (reward + self.gamma * max_future_q)
                    q_table[state, action] = new_q
                    state = new_state
        return q_table

    def return_path(self, start, end, q, gridworld):
        table = np.arange(self.rows * self.rows).reshape(self.rows, -1)
        start_encoded = gridworld.convert_state(start)
        end_encoded = gridworld.convert_state(end)

        state = start_encoded

        path = []
        path.append(state)

        done = False
        while not done:
            action = np.argmax(q[state])
            new_state, _, done = gridworld.step(state, action)
            path.append(new_state)
            state = new_state
        
        for i, val in enumerate(path):
            pos = np.where(table == val)
            path[i] = (pos[0].item(), pos[1].item())
        
        return path
        