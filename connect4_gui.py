import tkinter as tk
from connect4_environment import Connect4Environment
from q_learning_agent import QLearningAgent

class Connect4GUI:
    def __init__(self):
        player1 = QLearningAgent(player_number=1)
        player2 = QLearningAgent(player_number=2)
        self.env = Connect4Environment(player1, player2)
        self.root = tk.Tk()
        self.root.title("Connect4")
        self.canvas = tk.Canvas(self.root, width=700, height=600)
        self.canvas.pack()
        self.init_buttons()
        self.restart_game()
        self.root.mainloop()
        
    def draw_board(self):
        self.canvas.delete("all")
        for row in range(6):
            for col in range(7):
                x1, y1 = col * 100, row * 100
                x2, y2 = x1 + 100, y1 + 100
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
                if self.env.board[row][col] == 1:
                    self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="red")
                elif self.env.board[row][col] == 2:
                    self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="yellow")
    
    def init_buttons(self):
        restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        restart_button.pack()
    
    def restart_game(self):
        self.env.reset()
        self.draw_board()
        self.play_game()
    
    def play_game(self):
        while self.env.check_winner() == 0 and not self.env.is_board_full():
            if self.env.current_player == 1:
                action = self.env.player1.choose_action(self.env.board, self.env.get_legal_moves())
            else:
                action = self.env.player2.choose_action(self.env.board, self.env.get_legal_moves())
            self.env.make_move(action)
            self.draw_board()
        winner = self.env.check_winner()
        if winner != 0:
            print("Player", winner, "wins!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    gui = Connect4GUI()
