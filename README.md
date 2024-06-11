# Connect4
Here's a description in the form of a README file for the three provided project files:

---

# Connect4 Q-Learning Project

This repository contains the implementation of a Connect4 game environment, a graphical user interface (GUI) for the game, and a Q-learning agent designed to play Connect4.

## Project Files

1. **connect4_environment.py**: 
   - This file defines the `Connect4Environment` class, which sets up the Connect4 game environment.
   - It includes methods for resetting the board, making moves, checking for a winner, and determining legal moves.

2. **connect4_gui.py**:
   - This file provides a graphical user interface for playing Connect4 using the `Connect4Environment` class.
   - It allows players to interact with the game through a simple CLI-based interface.

3. **q_learning_agent.py**:
   - This file defines the `QLearningAgent` class, which uses Q-learning to learn how to play Connect4.
   - It includes methods for updating Q-values, choosing actions based on the current state, and exploring/exploiting the environment.

## How to Run

1. **Connect4 Environment**:
   - To use the Connect4 environment, instantiate the `Connect4Environment` class with two player objects.

2. **Connect4 GUI**:
   - Run the `connect4_gui.py` file to start a game session with a simple CLI interface.

3. **Q-learning Agent**:
   - Use the `QLearningAgent` class to create an agent that can learn and play Connect4.
   - Train the agent by running simulations with the `Connect4Environment`.

## Requirements

- Python 3.x
- NumPy
- Additional libraries may be needed based on the specific implementation in the files.
