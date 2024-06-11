import numpy as np

class QLearningAgent:
    def __init__(self, player_number, learning_rate=0.1, discount_factor=0.9, epsilon=0.1):
        self.q_values = {}
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.player_number = player_number
        
    def get_q_value(self, state, action):
        state_tuple = tuple(map(tuple, state))  # Convert NumPy array to tuple
        if (state_tuple, action) not in self.q_values:
            self.q_values[(state_tuple, action)] = 0
        return self.q_values[(state_tuple, action)]
    
    def update_q_value(self, state, action, reward, next_state, legal_actions):
        state_tuple = tuple(map(tuple, state))  # Convert NumPy array to tuple
        next_state_tuple = tuple(map(tuple, next_state))  # Convert NumPy array to tuple
        max_next_q_value = max([self.get_q_value(next_state_tuple, next_action) for next_action in legal_actions])
        self.q_values[(state_tuple, action)] += self.learning_rate * (reward + self.discount_factor * max_next_q_value - self.get_q_value(state_tuple, action))
    
    def choose_action(self, state, legal_actions):
        state_tuple = tuple(map(tuple, state))  # Convert NumPy array to tuple
        if np.random.rand() < self.epsilon:
            return np.random.choice(legal_actions)
        else:
            q_values = [self.get_q_value(state_tuple, action) for action in legal_actions]
            max_q_value = max(q_values)
            best_actions = [action for action, q_value in zip(legal_actions, q_values) if q_value == max_q_value]
            return np.random.choice(best_actions)
