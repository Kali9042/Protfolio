import tkinter as tk
import random

class DiceGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Game")
        
        self.label = tk.Label(root, text="Welcome to the Dice Game!", font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.player1_label = tk.Label(root, text="Player 1, click to roll the dice", font=("Helvetica", 12))
        self.player1_label.pack()
        self.player1_button = tk.Button(root, text="Roll Dice", command=self.roll_player1)
        self.player1_button.pack(pady=5)
        
        self.player2_label = tk.Label(root, text="Player 2, click to roll the dice", font=("Helvetica", 12))
        self.player2_label.pack()
        self.player2_button = tk.Button(root, text="Roll Dice", command=self.roll_player2)
        self.player2_button.pack(pady=5)
        
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)
        
        self.restart_button = tk.Button(root, text="Restart Game", command=self.restart_game)
        self.restart_button.pack(pady=10)
        
        self.player1_roll = 0
        self.player2_roll = 0
    
    def roll_player1(self):
        self.player1_roll = random.randint(1, 6)
        self.player1_label.config(text=f"Player 1 rolled a {self.player1_roll}")
        self.check_winner()
    
    def roll_player2(self):
        self.player2_roll = random.randint(1, 6)
        self.player2_label.config(text=f"Player 2 rolled a {self.player2_roll}")
        self.check_winner()
    
    def check_winner(self):
        if self.player1_roll != 0 and self.player2_roll != 0:
            if self.player1_roll > self.player2_roll:
                self.result_label.config(text="Player 1 wins!")
            elif self.player2_roll > self.player1_roll:
                self.result_label.config(text="Player 2 wins!")
            else:
                self.result_label.config(text="It's a tie!")
    
    def restart_game(self):
        self.player1_roll = 0
        self.player2_roll = 0
        self.player1_label.config(text="Player 1, click to roll the dice")
        self.player2_label.config(text="Player 2, click to roll the dice")
        self.result_label.config(text="")
    
if __name__ == "__main__":
    root = tk.Tk()
    game = DiceGame(root)
    root.mainloop()
