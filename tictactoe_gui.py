import tkinter as tk
from tkinter import messagebox
from tictactoe import check_winner

# Globale Variablen
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

def create_widgets(root):
    global buttons
    for row in range(3):
        for col in range(3):
            button = tk.Button(root, text="", font=('normal', 40, 'normal'), width=5, height=2,
                               command=lambda r=row, c=col: on_button_click(r, c))
            button.grid(row=row, column=col)
            buttons[row][col] = button

    label = tk.Label(root, text=f"Player {current_player}'s turn", font=('normal', 20, 'normal'))
    label.grid(row=3, column=0, columnspan=3)
    return label

def on_button_click(row, col):
    global current_player
    if board[row][col] == "" and not check_winner(board):
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        
        if check_winner(board):
            label.config(text=f"Spieler {current_player} gewinnt!")
            messagebox.showinfo("Game Over", f"Spieler {current_player} gewinnt!")
        elif all(all(cell != "" for cell in row) for row in board):
            label.config(text="Es ist ein Unentschieden!")
            messagebox.showinfo("Game Over", "Es ist ein Unentschieden")
        else:
            current_player = "O" if current_player == "X" else "X"
            label.config(text=f"Spieler {current_player} ist dran")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic Tac Toe")
    label = create_widgets(root)
    root.mainloop()
