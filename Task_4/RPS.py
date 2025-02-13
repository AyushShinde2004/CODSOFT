import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock, Paper, Scissors")
        self.master.geometry("400x400")  
        self.master.resizable(False, False)
        self.setup_style()
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.create_widgets()
        self.setup_layout()
    def setup_style(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Segoe UI', 12))
        self.style.configure('TButton', font=('Segoe UI', 12), foreground='black')
        self.style.map('Rock.TButton',
                      background=[('active', '#FF5733'), ('!disabled', '#FF0000')])
        self.style.map('Paper.TButton',
                      background=[('active', '#33FF57'), ('!disabled', '#00FF00')])
        self.style.map('Scissors.TButton',
                      background=[('active', '#3357FF'), ('!disabled', '#0000FF')])

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.master, padding=20)
        self.main_frame.pack(fill='both', expand=True)
        self.title_label = ttk.Label(
            self.main_frame,
            text="Rock, Paper, Scissors",
            font=('Segoe UI', 20, 'bold')
        )
        self.score_var = tk.StringVar(value="Wins: 0 | Losses: 0 | Ties: 0")
        self.score_label = ttk.Label(
            self.main_frame,
            textvariable=self.score_var,
            font=('Segoe UI', 12),
            background='#f0f0f0'
        )
        self.result_var = tk.StringVar(value="Make your choice!")
        self.result_label = ttk.Label(
            self.main_frame,
            textvariable=self.result_var,
            font=('Segoe UI', 14),
            wraplength=350,
            justify='center'
        )
        self.player_choice_var = tk.StringVar(value="Your Choice: ❓")
        self.computer_choice_var = tk.StringVar(value="Computer's Choice: ❓")
        
        self.player_choice_label = ttk.Label(
            self.main_frame,
            textvariable=self.player_choice_var,
            font=('Segoe UI', 12),
            background='#f0f0f0'
        )
        self.computer_choice_label = ttk.Label(
            self.main_frame,
            textvariable=self.computer_choice_var,
            font=('Segoe UI', 12),
            background='#f0f0f0'
        )
        self.rock_btn = ttk.Button(
            self.main_frame,
            text="🪨 Rock",
            command=lambda: self.play("rock"),
            style='Rock.TButton',
            width=10
        )
        self.paper_btn = ttk.Button(
            self.main_frame,
            text="📄 Paper",
            command=lambda: self.play("paper"),
            style='Paper.TButton',
            width=10
        )
        self.scissors_btn = ttk.Button(
            self.main_frame,
            text="✂️ Scissors",
            command=lambda: self.play("scissors"),
            style='Scissors.TButton',
            width=10
        )
        self.reset_btn = ttk.Button(
            self.main_frame,
            text="Reset Game",
            command=self.reset_game,
            style='TButton',
            width=15
        )

    def setup_layout(self):
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))
        self.score_label.grid(row=1, column=0, columnspan=3, pady=(0, 10))
        self.result_label.grid(row=2, column=0, columnspan=3, pady=(0, 10))
        
        self.player_choice_label.grid(row=3, column=0, columnspan=3, pady=(10, 5))
        self.computer_choice_label.grid(row=4, column=0, columnspan=3, pady=(5, 10))
        
        self.rock_btn.grid(row=5, column=0, padx=5, pady=5, sticky='ew')
        self.paper_btn.grid(row=5, column=1, padx=5, pady=5, sticky='ew')
        self.scissors_btn.grid(row=5, column=2, padx=5, pady=5, sticky='ew')
        
        self.reset_btn.grid(row=6, column=0, columnspan=3, pady=(20, 0), sticky='ew')

        for i in range(3):
            self.main_frame.columnconfigure(i, weight=1)

    def play(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        emoji_map = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
        self.player_choice_var.set(f"Your Choice: {emoji_map[player_choice]}")
        self.computer_choice_var.set(f"Computer's Choice: {emoji_map[computer_choice]}")

        if player_choice == computer_choice:
            result = "It's a tie!"
            self.ties += 1
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            self.wins += 1
        else:
            result = "You lose!"
            self.losses += 1
        self.result_var.set(f"Result: {result}")
        self.score_var.set(f"Wins: {self.wins} | Losses: {self.losses} | Ties: {self.ties}")
    def reset_game(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.score_var.set(f"Wins: {self.wins} | Losses: {self.losses} | Ties: {self.ties}")
        self.result_var.set("Make your choice!")
        self.player_choice_var.set("Your Choice: ❓")
        self.computer_choice_var.set("Computer's Choice: ❓")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
