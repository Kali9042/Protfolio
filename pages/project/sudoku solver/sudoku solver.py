import numpy as np
import tkinter as tk
from tkinter import messagebox

def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

def find_empty_location(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve_sudoku(board):
    find = find_empty_location(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def display_solution(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(tk.END, str(board[i][j]))

def solve_button_action():
    board = np.zeros((9, 9), dtype=int)
    for i in range(9):
        for j in range(9):
            if entries[i][j].get().isdigit():
                board[i][j] = int(entries[i][j].get())
            else:
                board[i][j] = 0
    if solve_sudoku(board):
        display_solution(board)
    else:
        messagebox.showerror("Error", "No solution exists for the given Sudoku puzzle")

# Create GUI
root = tk.Tk()
root.title("Sudoku Solver")

canvas = tk.Canvas(root, width=450, height=450)
canvas.grid(row=0, column=0, columnspan=9, rowspan=9)

entries = []
for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(root, width=2, font=('Arial', 18), justify='center')
        entry.grid(row=i, column=j, padx=5, pady=5)
        row_entries.append(entry)
    entries.append(row_entries)

for i in range(10):
    if i % 3 == 0:
        thickness = 2
        color = "red"  
    else:
        thickness = 1
        color = "black"  
    canvas.create_line(5 + i*50, 5, 5 + i*50, 455, width=thickness, fill=color)
    canvas.create_line(5, 5 + i*50, 455, 5 + i*50, width=thickness, fill=color)

solve_button = tk.Button(root, text="Solve", command=solve_button_action)
solve_button.grid(row=10, column=4, pady=10)

root.mainloop()
