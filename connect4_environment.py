import numpy as np

class Connect4Environment:
    def __init__(self, player1, player2):
        self.board = np.zeros((6, 7))  # 6 rows, 7 columns
        self.current_player = 1  # Player 1 starts
        self.player1 = player1
        self.player2 = player2
        
    def reset(self):
        self.board = np.zeros((6, 7))
        self.current_player = 1
        
    def get_legal_moves(self):
        return [col for col in range(7) if self.board[0][col] == 0]
    
    def make_move(self, column):
        row = 5
        while row >= 0:
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                break
            row -= 1
        self.current_player = 3 - self.current_player  # Switch players
    
    def check_winner(self):
        for row in range(6):
            for col in range(4):
                if self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][col + 3] != 0:
                    return self.board[row][col]
        
        for row in range(3):
            for col in range(7):
                if self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col] != 0:
                    return self.board[row][col]
        
        for row in range(3):
            for col in range(4):
                if self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3] != 0:
                    return self.board[row][col]
        
        for row in range(3, 6):
            for col in range(4):
                if self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == self.board[row - 3][col + 3] != 0:
                    return self.board[row][col]
        
        return 0  # No winner yet
    
    def is_board_full(self):
        return np.all(self.board != 0)
    
    def play_game(self):
        while self.check_winner() == 0 and not self.is_board_full():
            if self.current_player == 1:
                action = self.player1.choose_action(self.board, self.get_legal_moves())
            else:
                action = self.player2.choose_action(self.board, self.get_legal_moves())
            prev_board = np.copy(self.board)  # Copy the board before the move
            self.make_move(action)
            new_board = np.copy(self.board)  # Copy the board after the move
            reward_player1, reward_player2 = self.calculate_rewards(prev_board, new_board)
            self.player1.update_q_value(prev_board, action, reward_player1, new_board, self.get_legal_moves())
            self.player2.update_q_value(prev_board, action, reward_player2, new_board, self.get_legal_moves())
        winner = self.check_winner()
        if winner != 0:
            reward_player1 = 1 if winner == 1 else -1
            reward_player2 = -reward_player1
            print("Player", winner, "wins!")
        else:
            reward_player1 = 0.5
            reward_player2 = 0.5
            print("It's a draw!")
        self.player1.update_q_value(prev_board, action, reward_player1, new_board, self.get_legal_moves())
        self.player2.update_q_value(prev_board, action, reward_player2, new_board, self.get_legal_moves())
    
    def calculate_rewards(self, prev_board, new_board):
        reward_player1 = 0
        reward_player2 = 0
        winner = self.check_winner()
        if winner == 1:
            reward_player1 = 1
            reward_player2 = -1
        elif winner == 2:
            reward_player1 = -1
            reward_player2 = 1
        elif self.is_board_full():
            reward_player1 = 0.5
            reward_player2 = 0.5
        return reward_player1, reward_player2

